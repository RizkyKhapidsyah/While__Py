Judul = ("BAGIAN 1", "BAGIAN 2", "BAGIAN 3", "BAGIAN 4", "BAGIAN 5")
Garis = ('-' * 8)


#BAGIAN 1
print(Garis, Judul[0], Garis)
Nilai = 0

while Nilai <= 5:
    print("Nilai Angka =", Nilai)
    Nilai = Nilai + 1

print('Diluar While', '\n' * 2)


#BAGIAN 2
print(Garis, Judul[1], Garis)
Nilai = 0
Mulai = True

while Mulai:
    print("Urutkan Angka Ke", Nilai)
    if Nilai is 17:
        Mulai = False
        print("Angka", Nilai, "Ditemukan!")
    Nilai += 1

#BAGIAN 3
print(Garis, Judul[2], Garis)
Data = ("Rizky Khapidsyah", "Dessy Puspita Sari", "Ayah", "Mamak", "Adek")
Nilai = 0
Mulai = True

while Mulai:
    print("Nama:", Data[Nilai])
    Mulai
    if Nilai is 2:
        print("Nama", Data[Nilai], "Ditemukan!")
        Mulai = False
        pass
    Nilai += 1
    
    
