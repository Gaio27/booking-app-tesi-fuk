# Product Requirements Document (PRD) - Booking App Tesi-Fuk

## 1. Project Overview
**Booking App Tesi-Fuk** adalah aplikasi web pemesanan (booking) layanan tesi fuk (potong rambut) berbasis Flask yang dirancang ringan, responsif, dan mendukung fitur Progressive Web App (PWA). Aplikasi ini dirancang untuk memudahkan pelanggan melakukan pemesanan jadwal potong rambut serta mempermudah admin dalam mengelola status janji temu.

---

## 2. Tech Stack
- **Backend Framework:** Python 3.9 (Flask 3.0)
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Features:** PWA (Service Worker & Web App Manifest)
- **Database:** SQLite / In-memory storage
- **Testing:** Pytest
- **Containerization:** Docker
- **CI/CD:** GitHub Actions Workflow

---

## 3. Key Features

### A. Customer Features (Hujun / Pelanggan)
1. **Formulir Agendamentu (Booking Form):**
   - Mengisi Nama Lengkap (*Naran Kompletu*).
   - Mengisi Nomor Telepon / WhatsApp (*Telemóvel*).
   - Memilih Jenis Layanan (*Hili Servisu*):
     - Tesi Fuk Ba'an (Potong Biasa)
     - Tesi Fuk + Kompletu (Potong + Paket Lengkap)
     - KOR / Peinte (Pewarnaan / Styling)
   - Memilih Tanggal & Jam (*Data & Oras*).
2. **Respon / Notifikasi Flash:**
   - Menampilkan konfirmasi bahwa pendaftaran berhasil.
3. **PWA Support:**
   - Aplikasi dapat di-install di smartphone/desktop pelanggan.

### B. Admin Features (Administrador)
1. **Login Admin:**
   - Otentikasi sederhana untuk masuk ke dashboard admin.
2. **Dashboard Agendamentu:**
   - Melihat semua daftar pemesanan dari pelanggan.
3. **Manajemen Status:**
   - Mengubah status pemesanan (*Pendente*, *Konfirmadu*, *Kansela*).
4. **Logout:**
   - Sesi keluar dari panel admin.

---

## 4. User Flow
1. **Pelanggan:** Buka Web App -> Isi Form Booking -> Klik 'Kria Agendamentu' -> Muncul Notifikasi Sukses.
2. **Admin:** Akses `/admin/login` -> Masuk Password -> Lihat Daftar Janji Temu -> Konfirmasi / Batalkan Booking.

---

## 5. Non-Functional Requirements
- **Performance:** Halaman utama harus muat kurang dari 2 detik.
- **Responsiveness:** Tampilan optimal di perangkat Mobile (Android/iOS) dan Desktop.
- **Portability:** Dapat dijalankan di mana saja menggunakan Docker container (`Dockerfile`).
