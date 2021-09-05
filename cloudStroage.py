import dropbox
class Transferdata:
    def __init__(self,accessToken):
        self.accessToken = accessToken
    def upload_files(self,file_from,file_to):
        dbx= dropbox.Dropbox(self.accessToken)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
def main ():
    accessToken = "sl.A37kfjFy45nnjKAVMK2rHeY0YgWRJ5dKaDsqmBTfcQHkcog4n-tyf_eI08Y1yVeSi43vLSd_FH96nTMdmldyRmePbt-s5WmRvWhWNT2MuCk1uQTi_7coslHpucW6sJQm5c2RhMc"
    transferdata = Transferdata(accessToken)
    file_from = input('enter the file to trasfer ')
    file_to = input('enter the path to uplode to dropboxz: ')
    transferdata.upload_files(file_from,file_to)
    print('file has been prined successfully')
main()