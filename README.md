Nama: Iqhsan Saleh  
NIM: 2225250021    
Kelas: 3A

## Tujuan

Menggunakan nested loop, membuat pola, serta menerapkan akumulasi dan pencacahan.

## Cara Menjalankan

```bash
python3 tugas/tabel_perkalian_dan_statistik.py
```

## Algoritma Tugas 3

- **Loop luar:** Mengatur baris atau nilai pertama yang diproses.
- **Loop dalam:** Mengulang proses untuk setiap kolom atau nilai kedua pada setiap iterasi loop luar.
- **Akumulator:** Menyimpan hasil penjumlahan atau nilai statistik yang dihitung secara bertahap.
- **Counter:** Menghitung jumlah data atau banyaknya kondisi yang terpenuhi.

## Hasil Pengujian

| n | Jumlah pasangan | Total semua | Banyak hasil genap |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 |
| 2 | 4 | 9 | 3 |
| 3 | 9 | 36 | 5 |
| 4 | 16 | 100 | 12 |
| 5 | 25 | 225 | 16 |

## Analisi Efisiensi

Jika loop luar dan loop dalam masing-masing berjalan sebanyak `n` kali, badan loop dalam berjalan sebanyak `n × n` atau `n²` kali. Kompleksitas waktunya adalah **O(n²)**.

## Refleksi

Kesalahan nested loop yang ditemukan: Variabel akumulator diinisialisasi ulang di dalam loop dalam, sehingga nilainya selalu kembali ke nol dan hasil penjumlahan tidak terkumpul.

Cara memperbaikinya: Inisialisasi akumulator sebelum loop dimulai, lalu perbarui nilainya di dalam loop.