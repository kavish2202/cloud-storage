import os
import dropbox
from dropbox.files import WriteMode
#
class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token
#
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

            # enumerate local files recursively
        for root, dirs, files in os.walk(file_from):

            for filename in files:
                    # construct the full local path
                local_path = os.path.join(root, filename)

                    # construct the full Dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                    # upload the file
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = "u3u9K1CYmqMAAAAAAAAAAaUCXk0J2NPm_gn_UZpmSiJ-ZFMhhk7x2Mo85M6OvMiw"
    transferData = TransferData(access_token)

    file_from = "C:/Users/akoda/Desktop/Python/Project101/xyz/"
    file_to = "/kavish/"

    # API v2
    transferData.upload_file(file_from,file_to)
    print("file has been moved !!!")

main()