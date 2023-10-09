import json
import quart
import quart_cors
from quart import request
import httpx
import os
from dotenv import load_dotenv
load_dotenv()

app = quart_cors.cors(quart.Quart(__name__),
                      allow_origin="https://chat.openai.com")

_TODOS = {}

CLIENT_URL = 'https://myanimelist.net/v1/oauth2/authorize'
AUTH_URL = 'https://myanimelist.net/v1/oauth2/token'
OPENAI_CLIENT_ID = os.getenv("OPENAI_CLIENT_ID")
OPENAI_CLIENT_SECRET = os.getenv("OPENAI_CLIENT_SECRET")
OPENAI_TOKEN = os.getenv("OPENAI_TOKEN")
OPENAI_CODE = os.urandom(43).hex()


@app.post("/todos/<string:username>")
async def add_todo(username):
    request = await quart.request.get_json(force=True)
    if username not in _TODOS:
        _TODOS[username] = []
    _TODOS[username].append(request["todo"])
    return quart.Response(response='OK', status=200)


@app.get("/todos/<string:username>")
async def get_todos(username):
    return quart.Response(response=json.dumps(_TODOS.get(username, [])), status=200)


@app.delete("/todos/<string:username>")
async def delete_todo(username):
    request = await quart.request.get_json(force=True)
    todo_idx = request["todo_idx"]
    # fail silently, it's a simple plugin
    if 0 <= todo_idx < len(_TODOS[username]):
        _TODOS[username].pop(todo_idx)
    return quart.Response(response='OK', status=200)


@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')


@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")


@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")


@app.get("/oauth")
async def oauth():
    query_string = request.query_string.decode('utf-8')
    parts = query_string.split('&')
    kvps = {}
    for part in parts:
        k, v = part.split('=')
        v = v.replace("%2F", "/").replace("%3A", ":")
        kvps[k] = v
    print("OAuth key value pairs from the ChatGPT Request: ", kvps)
    url = f"https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id={kvps['client_id']}&code_challenge={OPENAI_CODE}"
    print("URL: ", url)
    return quart.Response(
        f'<a href="{url}">Click to authorize</a>'
    )


@app.post("/auth/oauth_exchange")
async def oauth_exchange():
    request = await quart.request.get_json(force=True)
    print(f"oauth_exchange {request=}")

    if request["client_id"] != OPENAI_CLIENT_ID:
        raise RuntimeError("bad client ID")
    if request["client_secret"] != OPENAI_CLIENT_SECRET:
        raise RuntimeError("bad client secret")
    if request["code"] != OPENAI_CODE:
        raise RuntimeError("bad code")

    # Send request to the external URL using httpx
    async with httpx.AsyncClient() as client:
        response = await client.post(AUTH_URL, json=request)

    response = response.json()

    print(response)

    return {
        "access_token": OPENAI_TOKEN, # not the right token???
        "token_type": response["token_type"],
        "refresh_token": response["refresh_token"],
    }


def main():
    port = int(os.environ.get("PORT", 5003))
    app.run(debug=True, host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
