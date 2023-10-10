from quart import Blueprint, Response

bp = Blueprint('manifest', __name__)

@bp.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    with open("app/static/.well-known/ai-plugin.json") as f:
        text = f.read()
        return Response(text, mimetype="text/json")


@bp.get("/openapi.yaml")
async def openapi_spec():
    with open("app/openapi.yaml") as f:
        text = f.read()
        return Response(text, mimetype="text/yaml")


@bp.get("/legal")
async def legal():
    return Response(response='🤷‍♂️', status=200)
