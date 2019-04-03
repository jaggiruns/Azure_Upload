
from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings

block_blob_service = BlockBlobService(account_name='ticketclassification2386', account_key='Q+lCNbXlp7J2aH/lSTE2w8OeEtArk2L226OjSkVKHzBxRgf5JUi74Fr3TfY9AcsOijP+H23aH74Sn0tVaddnIg==')
#block_blob_service.create_container('mycontainer')

#Upload the CSV file to Azure cloud
def create_file():
    block_blob_service.create_blob_from_path(
        'Predictions',
        'myblockblob.csv',
        'test.csv',
        content_settings=ContentSettings(content_type='application/CSV')
                )

# Check the list of blob
# generator = block_blob_service.list_blobs('mycontainer')
# for blob in generator:
#     print(blob.name)
#
# # Download the CSV file From Azure storage
# block_blob_service.get_blob_to_path('mycontainer', 'myblockblob.csv', 'out-test.csv')
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/')
def index():
    create_file()
    return """
        <html>
        <body>
        Hello, World!<br>
        This is a sample web service written in Python using <a href=""http://flask.pocoo.org/"">Flask</a> module.<br>
        </body>
        </html>
        """
if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    regexArr1 = getRegexList1()
    regexArr2 = getRegexList2()

    app.run(HOST, PORT)
