# Remove Subdomains Script

Skrip Python ini berfungsi untuk menyaring dan menghapus subdomain dari daftar domain berdasarkan ekstensi domain tertentu yang diizinkan. Hasilnya adalah daftar domain yang hanya memiliki ekstensi yang sudah ditentukan.

---

## Fitur

- Membaca daftar domain dari file input.
- Memfilter domain berdasarkan ekstensi yang diizinkan (default `.go.id`, `.ac.id`, `.sch.id`, `.co.id`, `.ponpes.id`, `.desa.id`).
- Menyimpan hasil domain yang sudah difilter ke file output.
- Penanganan error yang baik (file tidak ditemukan, izin baca/tulis, encoding, dll).

---

## Cara Menggunakan

1. Siapkan file teks yang berisi daftar domain, satu domain per baris.

2. Jalankan skrip:

   ```bash
   python remove_subdomains.py

3. Saat diminta, masukkan nama file input (file daftar domain) dan nama file output (untuk menyimpan hasil).

4. Hasil file output akan berisi domain yang sudah difilter berdasarkan ekstensi yang diizinkan.

---

## Parameter Ekstensi yang Diizinkan

Secara default, skrip hanya menerima domain dengan ekstensi:

```
.go.id, .ac.id, .sch.id, .co.id, .ponpes.id, .desa.id
```

Jika ingin menggunakan ekstensi lain, kamu dapat mengubah kode pada variabel `default_extensions` di fungsi `remove_subdomains`.

---

## Contoh

Misal `input.txt` berisi:

```
sub.example.co.id
example.com
kampus.ac.id
desa.sukasari.desa.id
```

Setelah dijalankan, dan memilih `input.txt` sebagai input dan `output.txt` sebagai output, `output.txt` akan berisi:

```
kampus.ac.id
desa.sukasari.desa.id
sub.example.co.id
```

---

## Error Handling

Skrip akan memberikan pesan kesalahan jika:

* File input tidak ditemukan.
* Tidak ada izin baca/tulis file.
* Encoding file bukan UTF-8.
* Error tak terduga lainnya.

---

## Requirements

* Python 3.x

---

## Lisensi

MIT License / Bebas digunakan dan dimodifikasi.

---

## Author

*Developed by alexithema*

```

