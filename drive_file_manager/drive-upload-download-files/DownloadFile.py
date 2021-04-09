import os
import io


from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload

CLIENT_SECRET_FILE = 'client_secrets.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#mimeTypes:
#https://developers.google.com/drive/api/v3/mime-types #google
#https://learndataanalysis.org/commonly-used-mime-types/ #geral

#OBS: não dá para baixar arquivos com tipo específico do google com a mesma função para tipos genéricos
#para arquivos com tipo do google é necessário chamar o método files().export(), ao invés do files().list() tipo:
#service.files().export(fileId="thisfileId", mimeType="application/pdf").execute()
#onde os IDs dos files podem ser adquiridos através de querys

#documentação da API, com as Queries:
#https://developers.google.com/drive/api/v3/search-files

#id do folder parent(pasta em que o arquivo está)
folderId = '1VBcvjvheBczTwlQiG0s4JQLJyItMAlzK'

##exemplos de querys:

#filtrando pelo tipo
#driveQuery = "(mimeType = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or mimeType = 'text/plain')"

#dizendo que o tipo não é folder(não dá pra baixar folders inteiros, eles só servem para identificar onde estão os arquivos)
driveQuery = "mimeType != 'application/vnd.google-apps.folder'"

#filtrando pelo nome do arquivo
#driveQuery = driveQuery + "and name = 'someImage'"

#passando o folder em que o arquivo alvo está, e dizendo que não está deletado 
driveQuery = driveQuery + f" and parents = '{folderId}' and trashed = false"
fieldsString = 'files(id, mimeType, parents, name)'

response = service.files().list(
    pageSize = 1000,
    q=driveQuery,
    fields=fieldsString
).execute()

fileList = response['files']
nextPageToken = response.get('nextPageToken')


while nextPageToken:
    response = service.files().list(
        pageSize = 1000,
        q=driveQuery,
        fields=fieldsString,
        pageToken=nextPageToken
    ).execute()

    fileList.extend(response['files'])
    nextPageToken = response.get('nextPageToken')

for item in fileList:
    #verificando se n é um arquivo escondido
    if not item['name'].startswith('~$'):
        #if(item['mimeType'] == '')
        request = service.files().get_media(fileId=item['id'])
        
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)

        done = False
        while(not done):
            status, done = downloader.next_chunk()

        fh.seek(0)

        file_name = item['name']
        
        with open(os.path.join('./download_folder',file_name), 'wb') as f:
            f.write(fh.read())
            f.close()
        
        
        

