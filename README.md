## 🔍 OSINT Tracking Forensics

Platform intelijen yang dirancang khusus untuk mengumpulkan data entitas publik secara cepat dan akurat. Alat ini mengotomatisasi pencarian geolokasi IP, analisis metadata seluler, serta penelusuran rekam jejak akun (alias footprint) menggunakan metode *asynchronous multi-threading*.

---

## Panduan Lengkap Instalasi
​Ikuti langkah-langkah di bawah ini sesuai dengan lingkungan perangkat yang kamu gunakan:

​A. Instalasi di Linux (Ubuntu / Debian / Arch / Kali Linux)

1. Update package manager dan instal Git serta Python3 jika belum ada :
```
sudo apt update && sudo apt install git python3 python3-pip -y
```
2. Clone repositori ke penyimpanan lokal :
```
git clone https://github.com/123tool/osint-tracking.git
cd osint-tracking
```
3. Instal seluruh library dependensi via pip :
```
pip3 install -r requirements.txt
```
4. Jalankan :
```bash
python3 main.py
```

B. Instalasi di Android via Termux
1. Buka aplikasi Termux, lalu izinkan akses repositori dan update sistem dasar :
```
pkg update && pkg upgrade -y
```
2. Instal dependensi esensial (Git, Python, dan clang compiler) :
```bash
pkg install git python python-pip -y
```
3. Clone
```
git clone https://github.com/123tool/osint-tracking.git
cd osint-tracking
```
4. dependensi Python :
```
pip install -r requirements.txt
```
5. Jalankan :
```
python main.py
```

C. Instalasi di Windows (PowerShell / CMD)
1. Pastikan Anda sudah mengunduh dan mencentang *"Add Python to PATH"* saat menginstal Python dari [python.org](https://www.python.org/).
2. Buka PowerShell atau Command Prompt, lalu jalankan :
```
git clone https://github.com/123tool/osint-tracking.git
cd osint-tracking
pip install -r requirements.txt
python main.py
```
## Alur Kerja :
- ​Opsi 1 & 2 (IP Intelligence) :
  Mengirimkan enkapsulasi payload request ke pelacak API geografi untuk membedah ASN jaringan target, koordinat presisi, dan nama ISP.
- ​Opsi 3 (Phone Telemetry) :
  Melakukan parsing data nomor telepon sesuai standar penomoran internasional ITU-T E.164 untuk membedah tipe operator seluler.
- Opsi 4 (Footprint Scraper) :
  Menggunakan ThreadPoolExecutor dengan alokasi max_workers=15 untuk melakukan pengecekan ketersediaan akun di berbagai situs web global secara simultan tanpa terkena antrean blocking rate limit.


## Disclaimer
​
**Alat ini dikembangkan murni untuk keperluan analisis digital forensik, penetration testing, audit keamanan jaringan, dan tujuan edukasi defensif. Penggunaan alat ini untuk aktivitas siber ilegal, mata-mata tanpa izin, atau doxing sepenuhnya merupakan tanggung jawab pengguna akhir.**
