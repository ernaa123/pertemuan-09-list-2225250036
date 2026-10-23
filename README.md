# Pertemuan 09 - List dan Pengolahan Data Numerik

Nama:Erna Hidayanti Nur Falah  
NIM: 2225250036
Kelas: 3B

## Tujuan
Mengolah kumpulan data numerik menggunakan list Python, meliputi menghitung jumlah data, total, rata-rata, nilai minimum, nilai maksimum, serta menganalisis kelulusan mahasiswa.

## Struktur Program
- `latihan/`: Berisi program latihan mengenai list dan pengolahan data numerik.
- `praktik/analisis_nilai_mahasiswa.py`: Program untuk menganalisis nilai mahasiswa, menghitung statistik nilai, dan menentukan jumlah mahasiswa yang lulus serta belum lulus.

## Cara Menjalankan
Jalankan perintah berikut melalui terminal VS Code dari folder utama proyek:

```bash
py praktik/analisis_nilai_mahasiswa.py
```

## Test Case

| No. | Data Uji | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | `[60, 70, 80]` | Rata-rata 70.00, minimum 60, maksimum 80, 3 mahasiswa lulus | Sesuai hasil pengujian | Lulus jika sesuai |
| 2 | `[59, 60, 61]` | 2 mahasiswa lulus dan 1 belum lulus | Sesuai hasil pengujian | Lulus jika sesuai |
| 3 | `[]` | Fungsi rata-rata tidak menghasilkan error | Sesuai hasil pengujian | Lulus jika sesuai |
| 4 | `[78, 55, 90, 67, 60, 82, 45, 71, 88, 59]` | 10 data, total 695, rata-rata 69.50, minimum 45, maksimum 90, 7 lulus, 3 belum lulus | Sesuai hasil pengujian | Lulus jika sesuai |

*Catatan: Isi kolom hasil aktual dan status berdasarkan pengujian yang benar-benar kamu lakukan.*

## Refleksi
Saya memahami bahwa list dapat digunakan untuk menyimpan banyak data dalam satu variabel dan setiap elemen dapat diakses menggunakan indeks yang dimulai dari 0. Saya juga belajar mengolah data menggunakan fungsi seperti `len()`, `sum()`, `min()`, dan `max()`. Kesalahan yang berhasil diperbaiki adalah ... (tuliskan kesalahan yang benar-benar kamu alami dan cara memperbaikinya).