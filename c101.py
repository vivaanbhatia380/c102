import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(), file_to)
        

def main():
    access_token='sl.A563MVFiPMmK9dzysiuJKWYaGnvlgPl_DJ6ncrf7ElRSWNAyOsvrsqG2dMjKhy_Xe9WrO0KI_0qc51BjJ62DScO4A8jPVPiCXRZtHAWr_8NzoAmGe3o-UgzxewBNAlSADBvsWsPSMECG'
    transferData=TransferData(access_token)
    file_from='abc.txt'
    file_to='/test_dropbox/abc.txt'
    transferData.upload_file(file_from,file_to)
    print('filemove')

main()

