import dropbox
import os

class Uploadfiles:
    def __init__ (self,access_token):
        self.access_token = access_token

    def paths_file(self,local_path,file_from,file_to,relative_path,dropbox_path):
        for root, dirs , files in os.walk(file_from):
            relative_path = os.path.relpath(local_path,file_from)
            dropbox_path = os.path.join(file_to,relative_path)

    def upload_file(self,file_from,file_to):
            kk = dropbox.Dropbox(self.access_token)
            
            with open (file_to,'rb')as f:
                kk.files_upload(f.read(),dropbox_path,mode = WriteMode('overwrite'))

def main ():
    access_token = "sl.A2etaJ9cvfZiGbQSP34Db9dZjGzfqJCy6Yv7F0bAt-nmOUvSpxI3hFZjyBBEqkIlotQ5lfqqOjNu8A3Ecfu5yrfYI29DShgxuqw7MrFICWwFQ1o8yCBVhU4Mk2Dwc7y4Vq4o03A"
    uploadfiles = Uploadfiles(access_token)

    file_from = "C:/Users/akoda/Desktop/Python/Project101/xyz"
    file_to = "test"

    uploadfiles.upload_file(file_from,file_to)
    print("File has been uploaded")

main()