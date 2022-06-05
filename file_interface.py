import os
import json
import base64
from glob import glob


class FileInterface:
    def __init__(self):
        os.chdir('files/')

    # ======== handle LIST request dan mengembalikan daftar file ========
    def list(self, params = []):
        try:
            filelist = glob('*.*')
            return dict(status = 'OK', data = filelist)
        except Exception as e:
            return dict(status = 'ERROR', data = str(e))

    # ======== handle GET request dari client dan mengembalikan data file ========
    def get(self, params = []):
        try:
            filename = str(params[0]).strip()
            if (filename == ''):
                return None
                
            fp = open(f"{filename}", 'rb')
            isifile = base64.b64encode(fp.read()).decode()
            return dict(status = 'OK', data_namafile = filename, data_file = isifile)
        except Exception as e:
            return dict(status = 'ERROR', data = str(e))

    # ======== handle POST request dari client dan menyimpan file di server ========
    def post(self, params = []):
        try:
            filename = str(params[0]).strip()
            if (filename == ''):
                return None
            fileData = str(params[1]).strip()
            if (fileData == ''):
                return None

            # Decode fileData kemudian menuliskan data ke file baru
            isiFile = base64.b64decode(fileData)
            fp = open(filename, 'wb+')
            fp.write(isiFile)
            fp.close()
            return dict(status = 'OK', data = f"File {filename} berhasil diunggah")
        except Exception as e:
            return dict(status = 'ERROR', data = str(e))

    # ======== handle DELETE request dari client dan menghapus file tersebut ========
    def delete(self, params = []):
        try:
            filename = str(params[0]).strip()
            if (filename == ''):
                return None

            # Menghapus file dengan nama file (filename)
            os.remove(filename)

            return dict(status = 'OK', data = f"File {filename} berhasil dihapus")
        except FileNotFoundError:
            return dict(status = 'ERROR', data = f"File {filename} tidak ditemukan")
        except Exception as e:
            return dict(status = 'ERROR', data = str(e))
                



# ======== MAIN FUNCTION TO TEST FILE FUNCTIONALITY ========
if __name__=='__main__':
    f = FileInterface()
    print(f.list())
    print(f.get(['pokijan.jpg']))
