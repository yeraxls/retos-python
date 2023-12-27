import requests
import json
from requests.auth import HTTPBasicAuth

basic = HTTPBasicAuth("X-Riot-Token", "RGAPI-07749d10-3369-437a-a2f7-9ef5c93dac03")
# Define la URL del API de League of Legends
API_URL = "https://euw1.api.riotgames.com/lol/match/v5/matches/"

# Define el ID de la partida que quieres analizar
MATCH_ID = "6713759707"

# Realiza una solicitud al API
response = requests.get(f"{API_URL}{MATCH_ID}", auth=basic)
# Comprueba si la solicitud se realizó correctamente
if response.status_code == 200:

    # Decodifica la respuesta del API
    data = json.loads(response.content)

    # Imprime los datos de la partida
    print("ID de la partida:", data["matchId"])


response2 = requests.get("https://europe.api.riotgames.com/lol/match/v5/matches/6713759707", auth=basic)
if response2.status_code == 200:
    print("funciona")