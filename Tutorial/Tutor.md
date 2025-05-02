
# 🚀 Panduan Git Dasar untuk Kolaborasi

Dokumen ini berisi panduan langkah-langkah dasar menggunakan Git untuk clone repository, membuat branch, dan melakukan push ke GitHub menggunakan HTTPS.

---

## 🔧 Langkah Awal: Konfigurasi Git

Sebelum mulai bekerja dengan Git, lakukan konfigurasi berikut (cukup sekali saja di awal):

```bash
git config --global user.name "Nama Kamu"
git config --global user.email "email@example.com"
```

---

## 📥 Clone Repository Menggunakan HTTPS

1. Salin URL HTTPS dari repository GitHub.
2. Buka File Explorer, lalu klik kanan di folder tempat project akan disimpan dan pilih **"Git Bash Here"**.
3. Jalankan perintah berikut untuk meng-clone repository:

```bash
git clone [URL_HTTPS]
cd [nama_folder]
code .
```

---

## 🌿 Membuat dan Berpindah ke Branch Baru

### Lihat semua branch yang tersedia:
```bash
git branch
```

### Buat branch baru:
```bash
git branch [nama_branch]
```

### Pindah ke branch tersebut:
```bash
git checkout [nama_branch]
```

---

## ⬆️ Push Perubahan ke GitHub

### Cek status perubahan pada file:
```bash
git status
```
- **File merah**: belum ditambahkan ke staging.
- **File hijau**: sudah masuk staging.

### Tambahkan file ke staging:

**Semua file:**
```bash
git add .
```

**File tertentu:**
```bash
git add [nama_file]
```

### Commit perubahan dengan pesan:
```bash
git commit -m "[komentar]"
```

### Push ke GitHub:

**Jika baru pertama kali push branch:**
```bash
git push -u origin [nama_branch]
```

**Jika branch sudah pernah di-push sebelumnya:**
```bash
git push
```

---

Selamat berkolaborasi! 🚀
