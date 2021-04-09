#Passos antes de utilizar: 
Instalar as bibliotecas de autenticação para APIs do Google, através do comando:
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

Ao se executar um dos programas pela primeira vez, seja para download ou upload, uma janela vai abrir e será pedido para fazer login na conta do Google, 
esse processo vai criar um token de autenticação que permitirá a API acessar o Google Drive daquela conta. Isso só vai ser necessário uma vez, 
e é recomendado deletar o token, arquivos ‘token_drive_v3.pickle’ e ‘client_secrets.json’, ao se compartilhar o programa ou transferi-lo para um lugar público.


#Upload file
Pode ser feito através da execução do arquivo ‘UploadFile.py’
O programa vai subir todos os arquivos em ‘upload_folder’ para a pasta do Google Drive especificada.
A pasta do Google Drive para onde os arquivos serão enviados pode ser identificada pelo ID da pasta, que é visto na URL da página ao abrir a pasta no Google Drive.
A URL da página onde a pasta estiver aberta deve algo assim: ‘https://drive.google.com/drive/folders/1wzBh7E75ZlaBk3VJPACanUcTmZ58f’
Onde o ID está depois de ‘...folder/’.
OBS: Tal ID também pode ser adquirido através de uma Query, assunto que será abordado na parte de Download.

#Download file
Pode ser feito através da execução do arquivo ‘DownloadFile.py’
O programa vai fazer o download de todos os arquivos no Google Drive especificados através das queries, para a pasta ‘download_folder’.
Uma observação importante é o Google utiliza dois métodos diferentes para fazer o download de arquivos com tipos próprios do Google e arquivos com tipos genéricos, 
é recomendado fazer o download somente de arquivos com tipo genéricos, caso o contrário vai ser necessário explicitar o tipo (mime type) de cada arquivo alvo.
No mais, as Queries para identificar quais arquivos fazer o download utilizam fatores como a pasta em que o arquivo está (parent = “id da pasta”), 
até características do nome (se contém certa palavra), tipo, certa data de criação, etc… Eu deixei alguns exemplos de Queries com comentários explicando cada Query, 
mas a documentação da API é bem clara e contém todos os métodos de Query:
https://developers.google.com/drive/api/v3/search-files
