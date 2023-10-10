import json
from quart import Blueprint, Response, g
import httpx

bp = Blueprint('mal', __name__)

URL = 'https://api.myanimelist.net/v2'

# Get suggested anime for the authorized user
# If the user is newcomer, this endpoint returns an empty list.
@bp.get("/anime/suggestions/<int:limit>")
async def suggest_anime(limit=10):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{URL}/anime/suggestions?limit={limit}', headers={'Authorization': f'Bearer {g.access_token}'})
    
    return Response(response=json.dumps(response.json()), status=200)

# Get seasonal anime
@bp.get("/anime/season/<int:year>/<string:season>/<int:limit>")
async def get_seasonal_anime(year, season, limit=10):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{URL}/anime/season/{year}/{season}?limit={limit}', headers={'Authorization': f'Bearer {g.access_token}'})
    
    return Response(response=json.dumps(response.json()), status=200)

# Get anime ranking
@bp.get("/anime/ranking/<string:ranking_type>/<int:limit>")
async def get_anime_ranking(ranking_type='all', limit=10):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{URL}/anime/ranking?ranking_type={ranking_type}&limit={limit}', headers={'Authorization': f'Bearer {g.access_token}'})
    
    return Response(response=json.dumps(response.json()), status=200)
    
# Get user anime list
@bp.get("/anime/list/<string:status>/<int:limit>")
async def get_anime_list(status='', limit=10):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{URL}/users/@me/animelist?fields={status}&limit={limit}', headers={'Authorization': f'Bearer {g.access_token}'})
    
    return Response(response=json.dumps(response.json()), status=200)
