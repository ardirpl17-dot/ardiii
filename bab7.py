# Membuat list
nilai = [85, 92, 78, 95, 70] 
buah = ['apel', 'mangga', 'pisang']
campuran = [1, 'Python', 3.14, True] # boleh beda tipe!

# Indexing — mengakses elemen 
print(nilai[0])  # 85 (indeks pertama = 0) 
print(nilai[-1]) # 70 (indeks negatif = dari belakang)  
print(buah[1]) # 'mangga' 

# Slicing — mengambil sebagian list   
print(nilai[1:4]) # [92, 78, 95] (indeks 1 s.d. 3) 
print(nilai[:3]) # [85, 92, 78] (dari awal s.d. indeks 2) 
print(nilai[2:]) # [78, 95, 70] (dari indeks 2 s.d. akhir) 
print(nilai[::2]) # [85, 78, 70] (setiap 2 langkah)