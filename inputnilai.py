a = {}

while True:
    x = input ("[T]tambah, [U]ubah, [H]hapus, [C]cari, [L]lihat, [K]keluar: ")

    if x.lower() == "t":
        print("Ubah Data")
        nama = input("Masukan Nama             : ")
        nim = int(input("Masukan NIM              : "))
        uts = int(input("Nilai UTS                : "))
        uas = int(input("Nilai UAS                : "))
        tugas = int(input("Nilai Tugas              : "))
        hasil = tugas * 0.30 + uts * 0.35 + uas * 0.35
        a[nama] = nim, uts, uas, tugas, hasil

    elif x.lower() == "u":
        print("Ubah Data")
        nama = input("Masukan Nama              : ")
        if nama in a.keys():
            nim = int(input("Masukan NIM          : "))
            uts = int(input("Nilai UTS            : "))
            uas = int(input("Nilai UAS            : "))
            tugas = int(input("Nilai Tugas          : "))
            hasil = tugas * 0.30 + uts * 0.35 + uas * 0.35
            a[nama] = nim, uts, uas, tugas, hasil
        else:
            print("Nama{0} Tidak ditentukan".format(nama))


    elif x.lower() == "h":
        print("Hapus Data")
        nama = input("Masukan Nama              : ")
        if nama in a.keys():
            del a[nama]
        else:
            print("Nama{0} Tidak di temukan".format(nama))


    elif x.lower() == "c":
        print("Cari Data")
        nama = input("Masukan nama              : ")
        if nama in a.keys():
            print("="*75)
            print("|                           DAFTAR MAHASISWA                           |")
            print("="*75)
            print("| {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                 .format(nama, nim, uts, uas, tugas, hasil))
            print("="*75)
        else:
            print("Nama{0} tidak di Tentukan".format(nama))

    elif x.lower() == "l" :
        if a.items():
            print("="*79)
            print("|                              DAFTAR MAHASISWA                           |")
            print("="*79)
            print("|No. | Nama      | NIM            | UTS | UAS | Tugas | Akhir |")
            print("="*79)
            i = 0
            for y in a.items():
                i += 1
                print("| {no:2d} | {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                     .format([0][:13], y[1][0], y[1][1], y[1][2], y[1][3], y[1][4], no =i))
        else:
            print("="*79)
            print("|                              DAFTAR MAHASISWA                           |")
            print("|No. | Nama            | NIM            | UTS | UAS | Tugas | Akhir |")
            print("="*79)
            print("|                              TIDAK ADA DATA                             |")
            print("="*79)

    elif x.lower() == "k":
        print("Anda Telah Keluar")
        break

    else:
        print("Pilih Menu Yang Tersedia")
            
