akhlak = 30
nilai = int(input("Masukan Nilai Anda : "))
hadir = True

nilai_akhir = akhlak + nilai
print("Nilai akhir:", nilai_akhir)

lulus = nilai >= 75 and hadir
print("Lulus?", lulus)

beasiswa = nilai >= 90 or akhlak > 20
print("Dapat Beasiswa?", beasiswa)