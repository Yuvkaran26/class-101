import dropbox

class boxdrop:
    def __init__(self,accessToken):
        self.accessToken=accessToken

    def upload(self,fileFrom,fileTo):
        box = dropbox.Dropbox(self.accessToken)

        f = open(fileFrom,"rb")

        box.files_upload(f.read(),fileTo)

def start():
    token="UFeXqoTJ36gAAAAAAAAAAfBZMK5mYoqgsdaivzhMEZ8ioR3OZbunv4oQUmqgHF58"

    data1=boxdrop(token)

    fileFrom=input("enter the file name to upload:  ")
    fileTo=input("enter the file name and dropbox path to upload:  ")

    data1.upload(fileFrom, fileTo)
    print("Sucessful")

start()