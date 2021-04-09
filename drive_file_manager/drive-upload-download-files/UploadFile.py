from Google import Create_Service
from googleapiclient.http import MediaFileUpload
from os import listdir
from os.path import isfile, join

#configurações gerais da API
CLIENT_SECRET_FILE = 'client_secrets.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ["https://www.googleapis.com/auth/drive"]
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#ID da pasta do Google Drive para onde serão enviados os arquivos
folderID = "1VBcvjvheBczTwlQiG0s4JQLJyItMAlzK"

fileList = [f for f in listdir("./upload_folder") if isfile(join("./upload_folder", f))]

file_names = fileList

for file_name in file_names:
    file_metadata = {
        'name': file_name,
        'parents' : [folderID]
    }

    media = MediaFileUpload('./upload_folder/'+file_name)
    
    service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id").execute()



