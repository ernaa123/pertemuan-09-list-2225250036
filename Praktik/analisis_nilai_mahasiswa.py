
def rata_rata(data):
    # Menghitung rata-rata dan menangani list kosong
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    # Membuat list baru yang berisi nilai lulus
    lulus = []
    for nilai in data:
        if nilai >= batas:
            lulus.append(nilai)
    return lulus


# Menyiapkan list nilai mahasiswa
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Menghitung statistik
banyak_data = len(nilai)
total = sum(nilai)
minimum = min(nilai) if banyak_data > 0 else 0
maksimum = max(nilai) if banyak_data > 0 else 0
rata = rata_rata(nilai)

# Menghitung kelulusan
lulus = nilai_lulus(nilai)
jumlah_lulus = len(lulus)
jumlah_belum_lulus = banyak_data - jumlah_lulus

# Menampilkan hasil
print("=== ANALISIS NILAI MAHASISWA ===")
print(f"Seluruh nilai       : {nilai}")
print(f"Banyak data         : {banyak_data}")
print(f"Total nilai         : {total}")
print(f"Rata-rata           : {rata:.2f}")
print(f"Nilai minimum       : {minimum}")
print(f"Nilai maksimum      : {maksimum}")
print(f"Batas kelulusan     : 60")
print(f"Jumlah mahasiswa lulus       : {jumlah_lulus}")
print(f"Jumlah mahasiswa belum lulus : {jumlah_belum_lulus}")
print(f"Daftar nilai lulus  : {lulus}")