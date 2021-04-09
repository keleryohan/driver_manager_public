from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secrets.json'
API_NAME = 'drive'
API_VERSION = 'v3'
#permissão total para todos os arquivos do drive:
SCOPES = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


#criando folders, poderia ser qualquer tipo de arquivo
someFolders = ["the first", "the second", "third wall"]

for folder in someFolders:
    file_metadata = {
        'name': folder,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': ["1VBcvjvheBczTwlQiG0s4JQLJyItMAlzK"] #id do folder pai
    }

    service.files().create(body=file_metadata).execute()

#mimeTypes:
#https://developers.google.com/drive/api/v3/mime-types #google
#https://learndataanalysis.org/commonly-used-mime-types/ #geral