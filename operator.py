akhlak = 30
nilai = int(input("masukan nilai anda : "))
hadir =  True

nilai_akhir = akhlak + nilai
print("nilai_akhir:", nilai_akhir)

lulus = nilai >= 75 and hadir
print("lulus:", lulus)

beasisiwa = nilai <= 90 or akhlak > 20
print("beasiswa:", beasisiwa)
