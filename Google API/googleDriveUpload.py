from __future__ import print_function
import os

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = ['https://www.googleapis.com/auth/drive.file']  # SCOPES

store = file.Storage('storage.json')

with open('client_secret.json') as f:
    CLIENT_SECRET = f

creds = store.get()  # OUR APP TRIES TO GER VALID API TOKEN

if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)

with open('api key.txt') as f:
    API_KEY = f

TYPE = 'drive'

API = "api url"

VERSION = 'v3'

DRIVE = build(TYPE, VERSION, http=creds.authorize(Http()))

FILES = (
    ('hello1.txt', None),
    ('hello1.txt', 'application/vnd.google-apps.document'),
)

for filename, mimeType in FILES:
    metadata = {'name': filename}
    if mimeType:
        metadata['mimeType'] = mimeType
    res = DRIVE.files().create(body=metadata, media_body=filename).execute()
    if res:
        print('Uploaded "%s" (%s)' % (filename,res['mimeType']))



