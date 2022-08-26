semuaSiswa = {}

def createDaftarSiswa():
    while True:
        print('\nSelamat Datang di menu Create data siswa')
        print('1. Create Data Nilai Siswa')
        print('2. Kembali Ke Menu Sebelumnya')

        input_a = input('Masukkan menu yang ingin anda akses ')
        if input_a == '1':
            print('CREATE DAFTAR NILAI SISWA:')
            input_noInduk = input("masukkan nomor induk siswa:")
            if input_noInduk in semuaSiswa:
                print('Data Sudah Ada')
                continue
            else:
                input_nama = input("masukkan nama siswa:")
                input_kelas = input("masukkan kelas siswa:")
                input_uts = input("masukkan nilai UTS:")
                input_uas = input("masukkan nilai UAS:")
                input_a = input('Apakah anda yakin untuk menyimpan data ini? ya/tidak ')
                if input_a == 'ya':
                    semuaSiswa[input_noInduk] = {
                    "noInduk" : input_noInduk,
                    "nama" : input_nama,
                    "kelas" : input_kelas,
                    "uas" : input_uts,
                    "uts" : input_uas
                    }
                    print("|{} \t|{} \t|{} \t|{} \t|{}".format('NOMOR','NAMA','KELAS','UTS','UAS'))
                    for key in semuaSiswa.keys():
                        print("|{} \t|{} \t|{} \t|{} \t|{}".format(semuaSiswa[key]["noInduk"],semuaSiswa[key]["nama"],semuaSiswa[key]["kelas"],semuaSiswa[key]["uts"],semuaSiswa[key]["uas"]))

                    print('Data Tersimpan')
                else:
                    continue   
        elif input_a == '2':
            break;

def readDaftarSiswa():
    while True:
        print('\nSelamat Datang di menu List Daftar Siswa')
        print('1. List Semua Data Siswa')
        print('2. List Siswa Tertentu')
        print('3. Kembali Ke Menu Sebelumnya')

        input_a = input('Masukkan menu yang ingin anda akses ')
        if input_a == '1' and len(semuaSiswa) != 0:
            print('LIST SEMUA DATA SISWA:')
            print("|{} \t|{} \t|{} \t|{} \t|{}".format('NOMOR','NAMA','KELAS','UTS','UAS'))
            for key in semuaSiswa.keys():
                    print("|{} \t|{} \t|{} \t|{} \t|{}".format(semuaSiswa[key]["noInduk"],semuaSiswa[key]["nama"],semuaSiswa[key]["kelas"],semuaSiswa[key]["uts"],semuaSiswa[key]["uas"]))
        elif input_a == '2':
            input_a = input("Masukkan nomor induk siswa:")
            if input_a in semuaSiswa:
                print("|{} \t|{} \t|{} \t|{} \t|{}".format('NOMOR','NAMA','KELAS','UTS','UAS'))
                print("|{} \t|{} \t|{} \t|{} \t|{}".format(semuaSiswa[input_a]["noInduk"],semuaSiswa[input_a]["nama"],semuaSiswa[input_a]["kelas"],semuaSiswa[input_a]["uts"],semuaSiswa[input_a]["uas"]))
            else:
                print('Tidak Ada Data')
        elif input_a == '3':
            break;
        else:
            print('Tidak Ada Data')

def updateDaftarSiswa():
    while True:
        print('\nSelamat Datang di menu Update data siswa')
        print('1. Update Data Nilai Siswa')
        print('2. Kembali Ke Menu Sebelumnya')

        input_a = input('Masukkan menu yang ingin anda akses ')
        if input_a == '1':
            print('UPDATE DAFTAR NILAI SISWA:')
            input_noInduk = input("masukkan nomor induk siswa:")
            if input_noInduk in semuaSiswa:
                print("|{} \t|{} \t|{} \t|{} \t|{}".format('NOMOR','NAMA','KELAS','UTS','UAS'))
                print("|{} \t|{} \t|{} \t|{} \t|{}".format(semuaSiswa[input_noInduk]["noInduk"],semuaSiswa[input_noInduk]["nama"],semuaSiswa[input_noInduk]["kelas"],semuaSiswa[input_noInduk]["uts"],semuaSiswa[input_noInduk]["uas"]))
                input_a = input('Apakah anda yakin untuk mengupdate data ini? ya/tidak ')
                if input_a == 'ya':
                    input_kolom = input("Masukkan kolom yang akan diupdate:")
                    input_value_baru = input("Masukkan data terbaru:")
                    
                    input_a = input('Apakah anda yakin untuk mengupdate data ini? ya/tidak ')
                    if input_a == 'ya':
                        semuaSiswa[input_noInduk][input_kolom] = input_value_baru
                        print("|{} \t|{} \t|{} \t|{} \t|{}".format('NOMOR','NAMA','KELAS','UTS','UAS'))
                        print("|{} \t|{} \t|{} \t|{} \t|{}".format(semuaSiswa[input_noInduk]["noInduk"],semuaSiswa[input_noInduk]["nama"],semuaSiswa[input_noInduk]["kelas"],semuaSiswa[input_noInduk]["uts"],semuaSiswa[input_noInduk]["uas"]))
                        print('Data telah terupdate')
                    else:
                        continue
                else:
                    continue
            else:
                print('Data yang anda cari tidak ada') 
                continue
        elif input_a == '2':
            break;
        
def deleteDaftarSiswa():
    while True:
        print('\nSelamat Datang di menu Delete Daftar Siswa')
        print('1. Hapus Data Siswa')
        print('2. Kembali Ke Menu Sebelumnya')

        input_a = input('Masukkan menu yang ingin anda akses ')
        if input_a == '1':
            input_noInduk = input("Masukkan nomor induk siswa:")
            if input_noInduk in semuaSiswa:
                print("|{} \t|{} \t|{} \t|{} \t|{}".format('NOMOR','NAMA','KELAS','UTS','UAS'))
                print("|{} \t|{} \t|{} \t|{} \t|{}".format(semuaSiswa[input_noInduk]["noInduk"],semuaSiswa[input_noInduk]["nama"],semuaSiswa[input_noInduk]["kelas"],semuaSiswa[input_noInduk]["uts"],semuaSiswa[input_noInduk]["uas"]))

                input_a = input('Apakah anda yakin untuk menghapus data ini? ya/tidak ')
                if input_a == 'ya':
                    semuaSiswa.pop(input_noInduk)
                    print('Data deleted')
                else:
                    continue
            else:
                print('Data yang anda cari tidak ada')
        elif input_a == '2':
            break;

while True:
    print('\nSelamat Datang di Menu Akademik Scores - Data Nilai Siswa')
    print('1. Buat Data Siswa Baru')
    print('2. List Data Siswa')
    print('3. Update Data Siswa')
    print('4. Hapus Data Siswa')
    print('5. Exit')
    input_a = input('Masukkan menu yang ingin anda akses ')


    if input_a == '1':
        createDaftarSiswa()
    elif input_a == '2':
        readDaftarSiswa()        
    elif input_a == '3':
        updateDaftarSiswa()
    elif input_a == '4':
        deleteDaftarSiswa()
    elif input_a == '5':
        break;
    else:
        print('Pilihan yang anda masukkan salah')
