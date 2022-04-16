import dropbox

class TransferData:
     def __init__(self,access_token):
         self.access_token =access_token

     def upload_file(self, file_from , file_to):
        dbx= dropbox.Dropbox(self.access_token)
        
        f=open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BF32I7KaYRJY_AthR4Am2N1A3W7lQ9hVhkwlOMqqIWSc0pa_kwYynNZ9Wv52iMwb7Fzv6xY-lsCguVvATSrceh61LLrJkgcOTEcNqXGJpAxg-5bMLbY-Mgi8cq7B9j5PiV8EAh0'
    transferData= TransferData(access_token)

    file_from = input("enter the path for transfer:")
    file_to = input("enter the path to upload to the dropbox:")
    transferData.upload_file(file_from,file_to)
    print("the file has been moved")

main()
