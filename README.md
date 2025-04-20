# # 🏠 Smart-Home Electronic Safety and Monitoring System

Sistem **Smart-Home Electronic Safety and Monitoring System** adalah solusi otomatisasi rumah berbasis mikrokontroler yang dirancang untuk meningkatkan keamanan dan kenyamanan penghuni. Sistem ini memantau kondisi rumah secara real-time serta memberikan respons terhadap situasi darurat seperti kebocoran gas, suhu tinggi, atau kehadiran orang asing.

## 📌 Fitur Utama

- 🔥 **Deteksi Suhu dan Kebakaran**: Menggunakan sensor suhu (seperti DHT22/LM35) untuk mendeteksi suhu abnormal yang berpotensi menyebabkan kebakaran.
- 🛑 **Deteksi Gas Berbahaya**: Sensor gas (seperti MQ-2/MQ-135) mendeteksi adanya kebocoran gas LPG atau asap.
- 👁️ **Pemantauan Kehadiran**: Sensor PIR untuk mendeteksi pergerakan mencurigakan saat rumah dalam kondisi kosong.
- 💡 **Kontrol Perangkat Elektronik**: Otomatisasi lampu, kipas, dan alat elektronik lain berdasarkan kondisi lingkungan.
- 📟 **Antarmuka LCD / Web Monitoring**: Menampilkan status sensor secara real-time melalui LCD atau dashboard monitoring berbasis Python GUI / web.
- 📱 **Pemberitahuan Darurat**: Opsional untuk mengirim notifikasi ke HP atau email menggunakan modul tambahan (ESP8266 / GSM).

## 🧰 Teknologi dan Tools

- 🖥️ **Mikrokontroler**: Arduino (Uno/Nano)
- 🔌 **Sensor**: DHT22, MQ-2, PIR, Flame sensor, Sensor level air
- 📊 **Interface**: LCD I2C 16x2 / GUI Python (Tkinter) / Web (Flask - opsional)
- 🔁 **Komunikasi**: UART Serial, RF/ESP jika menggunakan jaringan
- ⚙️ **Bahasa Pemrograman**: Arduino C++, Python

## 🔧 Cara Kerja

1. Sensor-sensor aktif membaca kondisi lingkungan.
2. Data dikirim ke mikrokontroler.
3. Mikrokontroler memproses data dan mengambil aksi:
   - Menghidupkan buzzer jika terdeteksi bahaya.
   - Menampilkan data ke LCD atau GUI.
   - Mengaktifkan atau menonaktifkan perangkat elektronik.
4. (Opsional) Kirim notifikasi ke pemilik rumah melalui jaringan.

## 📷 Dokumentasi / Demo

> Tambahkan gambar skematik, foto alat, atau video demo jika tersedia di sini.

## 🚀 Cara Menjalankan

### 1. Arduino
- Upload kode ke Arduino melalui Arduino IDE.
- Sambungkan sensor ke pin yang sesuai.

### 2. Python GUI (opsional)
```bash
pip install pyserial tkinter
python monitoring_gui.py
