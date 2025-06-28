

import requests
import threading
import time

# --- Konfigurasi Klien ---
BASE_API_URL = "http://127.0.0.1:5000"

# Data untuk diuji oleh klien: Daftar plat nomor yang akan dicek status servisnya
PLAT_UNTUK_DICEK = ["B1234ABC", "F9012GHI", "Z9999XX", "D5678DEF"] # Satu plat nomor tidak ada

# ==============================================================================
# SOAL: Implementasi Fungsi untuk Cek Status Servis via API
# ==============================================================================
def client_cek_servis_via_api(plat_nomor, thread_name):
    """
    TUGAS ANDA:
    Lengkapi fungsi ini untuk mengambil informasi status servis kendaraan dari API
    dan mencetak hasilnya ke konsol.

    Langkah-langkah:
    1. Bentuk URL target: f"{BASE_API_URL}/servis/{plat_nomor}/status"
    2. Cetak pesan ke konsol bahwa thread ini ('thread_name') memulai pengecekan untuk 'plat_nomor'.
       Contoh: print(f"[{thread_name}] Mengecek status servis untuk: {plat_nomor}")
    3. Gunakan blok 'try-except' untuk menangani potensi error saat melakukan permintaan HTTP.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke URL target menggunakan 'requests.get()'. Sertakan timeout.
          ii. Periksa 'response.status_code':
              - Jika 200 (sukses):
                  - Dapatkan data JSON dari 'response.json()'.
                  - Cetak kendaraan dan status servisnya ke konsol.
                    Contoh: print(f"[{thread_name}] Kendaraan {data.get('kendaraan')} ({plat_nomor}): Status '{data.get('status')}'")
              - Jika 404 (kendaraan tidak ditemukan):
                  - Cetak pesan bahwa kendaraan tidak ada dalam antrean servis.
                    Contoh: print(f"[{thread_name}] Kendaraan {plat_nomor} tidak ditemukan di bengkel.")
              - Untuk status code lain:
                  - Cetak pesan error umum ke konsol.
       b. Di blok 'except requests.exceptions.Timeout':
          - Cetak pesan bahwa permintaan timeout ke konsol.
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Cetak pesan error permintaan umum ke konsol.
    4. Setelah blok try-except, cetak pesan ke konsol bahwa thread ini ('thread_name') selesai memproses 'plat_nomor'.
    """
    target_url = f"{BASE_API_URL}/servis/{plat_nomor}/status"
    print(f"[{thread_name}] Mengecek status servis untuk: {plat_nomor}")
    
    try:
        response = requests.get(target_url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            print(f"[{thread_name}] Kendaraan {data.get('kendaraan')} ({plat_nomor}): Status '{data.get('status')}'")
            
        elif response.status_code == 404:
            print(f"[{thread_name}] Kendaraan {plat_nomor} tidak ditemukan di bengkel.")
            
        else:
            print(f"[{thread_name}] Terjadi error (status code: {response.status_code}) saat memproses {plat_nomor}.")
            
    except requests.exceptions.Timeout:
         print(f"[{thread_name}] Timeout saat mengakses status servis {plat_nomor}.")
         
    except requests.exceptions.RequestException as e:
         print(f"[{thread_name}] Kesalahan koneksi saat mengakses {plat_nomor}: {e}")
         print(f"[{thread_name}] Selesai memproses plat {plat_nomor}.\n")            
    
    #
    # ====================================

# --- Bagian Utama Skrip (Tidak Perlu Diubah Peserta) ---
if __name__ == "__main__":
    print(f"Memulai Klien Pengecek Status untuk {len(PLAT_UNTUK_DICEK)} Kendaraan Secara Concurrent.")
    
    threads = []
    start_time = time.time()

    for i, plat_cek in enumerate(PLAT_UNTUK_DICEK):
        thread_name_for_task = f"Pelanggan-{i+1}" 
        thread = threading.Thread(target=client_cek_servis_via_api, args=(plat_cek, thread_name_for_task))
        threads.append(thread)
        thread.start()

    for thread_instance in threads:
        thread_instance.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\nSemua pengecekan status servis telah selesai diproses dalam {total_time:.2f} detik.")