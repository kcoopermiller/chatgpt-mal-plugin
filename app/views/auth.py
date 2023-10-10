from quart import Blueprint, request, jsonify, Response, g
import httpx
import os

bp = Blueprint('auth', __name__)

CLIENT_URL = 'https://myanimelist.net/v1/oauth2/authorize'
AUTH_URL = 'https://myanimelist.net/v1/oauth2/token'
MAL_CODE = os.urandom(43).hex()

@bp.get("/oauth")
async def oauth():
    query_string = request.query_string.decode('utf-8')
    parts = query_string.split('&')
    kvps = {}
    for part in parts:
        k, v = part.split('=')
        v = v.replace("%2F", "/").replace("%3A", ":")
        kvps[k] = v
    
    url = f"{CLIENT_URL}?response_type=code&client_id={kvps['client_id']}&state={kvps['state']}&code_challenge={MAL_CODE}"
        
    return Response(
        f'<a href="{url}">Click to authorize</a>'
    )


@bp.post("/auth/oauth_exchange")
async def oauth_exchange():
    request_data = await request.get_json(force=True)
    data = {
        'client_id': request_data['client_id'],
        'client_secret': request_data['client_secret'],
        'grant_type': request_data['grant_type'],
        'code': request_data['code'],
        'code_verifier': MAL_CODE,
    }

    # Send request to the external URL using httpx
    async with httpx.AsyncClient() as client:
        response = await client.post(AUTH_URL, data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})

    # Update the global access token so that it can be used in other endpoints
    response = response.json()
    g.access_token = response['access_token']
    
    return jsonify(response)