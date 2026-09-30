# 1. Iterasi List
nilai = [85, 92, 78, 95]
print("--- Iterasi List ---")
for n in nilai:
    print(n, end=' ')
print("\n")  # Membuat baris baru

# 2. Iterasi dengan Indeks
print("--- Iterasi dengan Indeks ---")
for i, n in enumerate(nilai):
    print(f"Nilai ke-{i+1}: {n}")
print()

# 3. Iterasi Dictionary
print("--- Iterasi Dictionary ---")
siswa = {"Budi": 85, "Ani": 92, "Candra": 78}
for nama, skor in siswa.items():
    print(f"{nama}: {skor}")
print()

# 4. List Comprehension
print("--- List Comprehension ---")
nilai_ganda = [n * 2 for n in nilai]
nilai_lulus = [n for n in nilai if n >= 80]

print(f"Nilai Ganda: {nilai_ganda}")
print(f"Nilai Lulus (>= 80): {nilai_lulus}")