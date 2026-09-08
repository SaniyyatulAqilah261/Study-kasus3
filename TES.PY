# PROGRAM PENGELOMPOKAN NILAI UJIAN MAHASISWA

# Tuple batas nilai
batas_nilai = (65, 100)

# List untuk menyimpan nilai
nilai_masuk = []
lulus = []
remedi = []

print("=" * 50)
print("PENGELOMPOKAN NILAI UJIAN MAHASISWA")
print("=" * 50)

# Input nilai menggunakan perulangan
while True:
    nilai = input("Masukkan nilai (ketik 'selesai' untuk berhenti): ")

    if nilai.lower() == "selesai":
        if len(nilai_masuk) < 5:
            print("Minimal harus memasukkan 5 nilai.")
            continue

        if len(lulus) == 0 or len(remedi) == 0:
            print("Harus ada nilai LULUS dan REMEDI.")
            continue

        break

    try:
        nilai = int(nilai)

        if nilai < 0 or nilai > 100:
            print("Nilai harus antara 0 sampai 100.")
            continue

        # Menyimpan semua nilai
        nilai_masuk.append(nilai)

        # Mengelompokkan nilai
        if nilai >= batas_nilai[0]:
            lulus.append(nilai)
            print("Nilai", nilai, "masuk ke LULUS.")
        else:
            remedi.append(nilai)
            print("Nilai", nilai, "masuk ke REMEDI.")

    except ValueError:
        print("Input tidak valid. Masukkan angka.")


# Menampilkan data sebelum penghapusan
print("\n" + "=" * 50)
print("DATA NILAI")
print("=" * 50)

print("Nilai masuk :", nilai_masuk)
print("Nilai lulus :", lulus)
print("Nilai remedi:", remedi)


# Fitur menghapus nilai yang salah input
hapus = input("\nApakah ada nilai yang ingin dihapus? (y/n): ")

if hapus.lower() == "y":

    try:
        nilai_hapus = int(input("Masukkan nilai yang ingin dihapus: "))

        if nilai_hapus in nilai_masuk:

            nilai_masuk.remove(nilai_hapus)

            if nilai_hapus in lulus:
                lulus.remove(nilai_hapus)

            elif nilai_hapus in remedi:
                remedi.remove(nilai_hapus)

            print("Nilai", nilai_hapus, "berhasil dihapus.")

        else:
            print("Nilai", nilai_hapus, "tidak ditemukan.")

    except ValueError:
        print("Input tidak valid.")


# Menampilkan hasil akhir
print("\n" + "=" * 50)
print("HASIL AKHIR PENGELOMPOKAN NILAI")
print("=" * 50)

print("Seluruh nilai yang diinput :", nilai_masuk)
print("Nilai LULUS                :", lulus)
print("Nilai REMEDI               :", remedi)

print("=" * 50)