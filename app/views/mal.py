import json
from quart import Blueprint, Response, g
import httpx

bp = Blueprint('mal', __name__)

URL = 'https://api.myanimelist.net/v2'

# Get suggested anime for the authorized user
# If the user is newcomer, this endpoint returns an empty list.
bp.get("/anime/suggestions/<int:limit>")
async def suggest_anime(limit=10):
    print('headers')
    print(g.access_token)
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{URL}/anime/suggestions?limit={limit}', headers={'Authorization': f'Bearer {g.access_token}'})
    
    return Response(response=json.dumps(response.json()), status=200)

# Get seasonal anime
bp.get("/anime/season/<int:year>/<string:season>/<int:limit>")
async def anime_season(year, season, limit=10):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{URL}/anime/season/{year}/{season}?limit={limit}', headers={'Authorization': f'Bearer {g.access_token}'})
    
    return Response(response=json.dumps(response.json()), status=200)
    
