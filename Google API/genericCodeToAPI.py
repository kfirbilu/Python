# generic code!!!
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

with open('api key.txt') as f:
    API_KEY = f
API = "api url"
VERSION = 'v3'
SERVICE = build(API, VERSION, API_KEY)

SCOPES = []  # SCOPES

with open('client_secret.json') as f:
    CLIENT_SECRET = f

store = file.Storage('storage.json')

creds = store.get()  # OUR APP TRIES TO GER VALID API TOKEN

if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets(CLIENT_SECRET, SCOPES)
    credz = tools.run(flow, store)

SERVICE = build(API, VERSION, http=creds.authorize(Http()))
