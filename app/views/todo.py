import json
from quart import Blueprint, Response, request

bp = Blueprint('todo', __name__)

_TODOS = {}

@bp.post("/todos/<string:username>")
async def add_todo(username):
    request_data = await request.get_json(force=True)
    if username not in _TODOS:
        _TODOS[username] = []
    _TODOS[username].append(request_data["todo"])
    return Response(response='OK', status=200)


@bp.get("/todos/<string:username>")
async def get_todos(username):
    return Response(response=json.dumps(_TODOS.get(username, [])), status=200)


@bp.delete("/todos/<string:username>")
async def delete_todo(username):
    request_data = await request.get_json(force=True)
    todo_idx = request_data["todo_idx"]
    # fail silently, it's a simple plugin
    if 0 <= todo_idx < len(_TODOS[username]):
        _TODOS[username].pop(todo_idx)
    return Response(response='OK', status=200)