

# 🚗 Soal Pemrograman Cerita: Pengecek Status Servis Kendaraan di Bengkel "OtoJaya"

## 📖 Latar Belakang Cerita

Bengkel "OtoJaya" selalu ramai dengan pelanggan. Bagian *customer service* seringkali harus bolak-balik ke area bengkel hanya untuk menanyakan status pengerjaan mobil kepada mekanik. Hal ini tidak efisien dan membuat pelanggan menunggu lama. Manajemen ingin membuat aplikasi *mobile* untuk pelanggan agar mereka bisa mengecek status servis mobilnya sendiri.

Anda sebagai *backend developer* ditugaskan untuk membuat **klien pengujian** untuk API status servis yang baru. Klien ini harus mampu:

- Mensimulasikan banyak pelanggan yang mengecek status servis mobil mereka secara **concurrent (paralel)**.
- **Menangani kemungkinan error**, seperti plat nomor yang salah, kendaraan sudah selesai servis dan keluar dari sistem, atau server bengkel yang sedang sibuk.
- Memberikan output yang jelas untuk setiap hasil pengecekan.

---

## 🎯 Tujuan Tugas

Lengkapi fungsi `client_cek_servis_via_api()` agar program dapat:

- Melakukan permintaan HTTP ke endpoint API status servis.
- Menangani respons dengan benar (berhasil, tidak ditemukan, atau error lain).
- Menampilkan hasil pengecekan status servis ke konsol secara terstruktur per thread (per pelanggan).