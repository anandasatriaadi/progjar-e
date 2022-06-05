## FILE SERVER  
TUJUAN: Melayani client dalam request file dari server<br/><br/>

## ATURAN PROTOKOL:
- Client harus mengirimkan request dalam bentuk string dan diakhiri dengan karakter "\r\n" yang menandakan bahwa request tersebut sudah berakhir
- String harus dalam format
  REQUEST spasi PARAMETER
- PARAMETER dapat berkembang menjadi PARAMETER1 spasi PARAMETER2 dan seterusnya<br/><br/>

## REQUEST YANG DILAYANI:
- Informasi Umum:
  * Jika request tidak dikenali akan menghasilkan pesan
    - status: ERROR
    - data: request tidak dikenali
  * Semua result akan diberikan dalam bentuk JSON dan diakhiri
    dengan character ascii code #13#10#13#10 atau "\r\n\r\n"
  * Semua nama file bersifat case sensitive

## LIST
* TUJUAN: untuk mendapatkan daftar seluruh file yang dilayani oleh file server
* PARAMETER: tidak ada
* RESULT:
  - BERHASIL:
    - status: OK
    - data: list file
  - GAGAL:
    - status: ERROR
    - data: (pesan kesalahan)

## GET
* TUJUAN: untuk mendapatkan isi file dengan menyebutkan nama file dalam parameter
* PARAMETER:
  - PARAMETER1: nama file
* RESULT:
  - BERHASIL:
    - status: OK
    - data_namafile: nama file yang diminta
    - data_file: isi file yang diminta (dalam bentuk base64)
  - GAGAL:
    - status: ERROR
    - data: (pesan kesalahan)

## POST
* TUJUAN: untuk mengunggah atau mengirimkan isi file ke server dengan nama file dalam parameter
* PARAMETER:
  - PARAMETER1: nama file
  - PARAMETER2: isi file yang akan dikirimkan (dalam bentuk base64)
* RESULT:
  - BERHASIL:
    - status: OK
    - data: File (nama_file) berhasil diunggah
  - GAGAL:
    - status: ERROR
    - data: (pesan kesalahan)

## DELETE
* TUJUAN: untuk menghapus sebuah file yang berada di sisi server dengan nama file dalam parameter
* PARAMETER:
  - PARAMETER1: nama file
* RESULT:
  - BERHASIL:
    - status: OK
    - data: File (nama_file) berhasil dihapus
  - GAGAL:
    - status: ERROR
    - data: (pesan kesalahan)
