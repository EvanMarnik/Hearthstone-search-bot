import json
import asyncio
import os
async def card_search(text):
    # OAuth

    #uncomment out for local editing
    #client_id = open("bnet-bot-id").read()
    #client_secret = open("bnet-bot-secret").read()

    #uncomment for heroku
    client_id = os.environ["CLIENT_ID"]
    client_secret = os.environ["CLIENT_SECRET"]
    token_url = 'https://oauth.battle.net/token'

        #optimize token access
    from oauthlib.oauth2 import BackendApplicationClient
    from requests_oauthlib import OAuth2Session
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=token_url, client_id=client_id,
            client_secret=client_secret)

    # Game API
    blizzard_game_api = "https://us.api.blizzard.com"
    card_search_endpoint = "/hearthstone/cards"
    baseRequest = {":region":"us", "locale":"en_US"} # all requests should include this, so lets define it here

    request = baseRequest
    request["textFilter"] = text
    response = oauth.get(url=blizzard_game_api + card_search_endpoint, params=request)

    jsonResponse = json.loads(response.content)
    return jsonResponse