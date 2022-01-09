import os, dropbox

class Project:
    def __init__(self, accessToken):
        self.accessToken=accessToken

    def upload(self, fileFrom, fileTo):
        box = dropbox.Dropbox(self.accessToken)

        for root, dirs, files in os.walk(fileFrom):
            for name in files:
                localFile = os.path.join(root, name)
            for name in dirs:
                localDir = os.path.join(root, name)
            relative_path = os.path.relpath(localFile, fileFrom)
            dropbox_path = os.path.join(fileTo, relative_path)
            f = open(fileFrom, "rb")
            box.files_upload(f.read(), dropbox_path)

def start():
    token = "UFeXqoTJ36gAAAAAAAAAAfBZMK5mYoqgsdaivzhMEZ8ioR3OZbunv4oQUmqgHF58"
    token1 = Project(token)

    send = input("Enter the folder path to transfer: ")
    transfer = input("Enter the dropbox path: ")
    token1.upload(send, transfer)
    print("Successfully uploaded")
start()

        
