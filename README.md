# # 🏠 Smart-Home Electronic Safety and Monitoring System

**Smart-Home Electronic Safety and Monitoring System** adalah sistem otomatisasi rumah berbasis mikrokontroler AVR. Hal yang paling diutamakan dalam sistem ini adalah untuk menjaga dan memperpanjang umur alat elektronik seperti kulkas, ac, dll. Selain itu, pada sistem ini juga dilengkapi dengan fitur monitoring untuk memantau kondisi rumah secara real-time serta memberikan akses kontrol terhadap alat elektronik yang ada di rumah untuk menjaga keamanan dan efisiensi daya yang dikonsumsi, agar _Gerakan Hemat Energi Listrik_ dapat terealisasikan dengan baik.

Proyek ini bertujuan untuk mengembangkan sistem automasi Smart Home, menggunakan komponen utama seperti Arduino Mega, ACS712, ZMPT1010B dan berbagai sensor. Arduino mega bertindak sebagai mikroprosesor utama yang mengontrol komunikasi antar sensor dan perangkat, memungkinkan pemantauan dan pengontrolan secara real-time melalui jaringan UART TTL. Sistem ini dilengkapi dengan Auto cutt-off untuk menjaga alat elektronik rumah dari fluktuasi tegangan jala-jala PLN. Untuk memantau konsumsi energi, kami menggunakan sensor arus ACS712 dan sensor tegangan ZMPT101B yang secara akurat mengukur penggunaan arus listrik dan tegangan pada berbagai perangkat. Selain itu, Relay SPDT berfungsi sebagai saklar otomatis yang memungkinkan pengendalian perangkat elektronik seperti lampu. Selain itu, kami juga akan menambahkan fitur monitoring daya yang digunakan dan mengonversikannya secara otomatis sesuai dengan harga yang berlaku per-kWh.

## 📌 Fitur Utama

- 🛡️ **Menjaga Alat Elektronik Tetap Dalam Kondisi Baik** : Memutuskan arus saat terjadi fluktuasi tegangan jala-jala PLN
- 💡 **Kontrol Perangkat Elektronik**: Otomatisasi lampu, kipas, dan alat elektronik lain berdasarkan kondisi lingkungan.
- 📟 **Antarmuka LCD / Web Monitoring**: Menampilkan status sensor secara real-time melalui LCD atau dashboard monitoring berbasis Python GUI / web.
- 🧾 **Pencatatan Penggunaan Daya** : Menampilkan penggunaan daya secara otomatis
- 📱 **Pemberitahuan Darurat**: Opsional untuk mengirim notifikasi ke HP atau email menggunakan modul tambahan (ESP8266 / GSM).
- 🔥 **Deteksi Suhu dan Kebakaran**: Menggunakan sensor suhu (seperti DHT22/LM35) untuk mendeteksi suhu abnormal yang berpotensi menyebabkan kebakaran.
- 🛑 **Deteksi Gas Berbahaya**: Sensor gas (seperti MQ-2/MQ-135) mendeteksi adanya kebocoran gas LPG atau asap.
- 👁️ **Pemantauan Kehadiran**: Sensor PIR untuk mendeteksi pergerakan mencurigakan saat rumah dalam kondisi kosong.

## 🧰 Alat & Software yang Akan Kami Gunakan

- 🖥️ **Mikrokontroler**: Arduino (ATMega2560)
- 🔌 **Sensor**: DHT22, MQ-2, PIR, Flame sensor, Sensor level air
- 📊 **Interface**: LCD I2C 16x2 / GUI Python (Tkinter) / Web (Flask - opsional)
- 🔁 **Komunikasi**: UART Serial, RF/ESP jika menggunakan jaringan
- ⚙️ **Bahasa Pemrograman**: Arduino C++, Python

## 🔧 Cara Kerja



## 📷 Dokumentasi / Demo


## 🚀 Cara Menjalankan

### 1. Arduino

### 2. Python GUI (opsional)
```bash
pip install pyserial tkinter
python monitoring_gui.py
