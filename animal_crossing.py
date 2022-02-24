import nintendo, sys
import requests

ACNH_URL = nintendo.games_url[nintendo.ACNH]

app_head = {
    'X-IsAppAnalyticsOptedIn': 'false',
    'Accept':                  'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':         'gzip,deflate',
    'Content-Type': 'application/json; charset=utf-8',
    'X-IsAnalyticsOptedIn':    'false',
    'Connection':              'keep-alive',
    'DNT':                     '0',
    'User-Agent':              'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Mobile Safari/537.36',
    'X-Requested-With':        'com.nintendo.znca'
}

tokens = {}

def login() :
    nickname, lang, webservice_token = nintendo.login()
    game_cookie = nintendo.get_cookie(webservice_token,nintendo.ACNH, lang)
    bearer, park_session = get_tokens(game_cookie)
    tokens = {'game' : game_cookie, 'bearer':bearer, 'session': park_session }
    return tokens

def get_tokens(game_cookie) :
    # get cookie
    

    r = requests.get(ACNH_URL + "/api/sd/v1/users", headers=app_head, cookies={'_gtoken' : game_cookie})
    r = requests.post(ACNH_URL + "/api/sd/v1/auth_token", headers=app_head, cookies={'_gtoken' : game_cookie}, data={'userId' : r.json['users'][0]['id']})
    bearer = r.json['token']
    #TODO Add checks that bearer is not empty
    park_session = r.cookies['_park_session']

    return bearer, park_session

def send(text, type='keyboard', tokens=tokens) :
    app_head['Bearer'] = tokens['bearer']
    r = requests.post(ACNH_URL + "/sd/v1/messages", headers=app_head, cookies={'_gtoken' : tokens['game']}, data={'body' : text, 'type': type})