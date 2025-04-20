# 🔌 Smart Home Automation System with Real-Time Energy Monitoring

## 📘 Deskripsi Proyek

Proyek ini bertujuan untuk mengembangkan **sistem automasi rumah pintar (Smart Home Automation System)** yang dapat memantau dan mengontrol peralatan elektronik secara real-time. Sistem ini juga dilengkapi dengan fitur **auto cut-off** untuk menjaga peralatan rumah tangga dari fluktuasi tegangan yang berasal dari jaringan listrik PLN.

## 🎯 Tujuan

- Mengontrol peralatan elektronik rumah secara otomatis.
- Memantau konsumsi energi listrik secara akurat.
- Melindungi perangkat dari lonjakan atau drop tegangan melalui fitur auto cut-off.

## 🧠 Komponen Utama

| Komponen       | Fungsi                                                                 |
|----------------|------------------------------------------------------------------------|
| Arduino Mega   | Mikrokontroler utama yang mengatur komunikasi dan pengolahan data.     |
| ACS712         | Sensor arus untuk mengukur konsumsi arus listrik.                      |
| ZMPT101B       | Sensor tegangan AC untuk memantau tegangan dari sumber PLN.            |
| Relay SPDT     | Saklar otomatis untuk mengontrol perangkat listrik seperti lampu.      |
| Sensor Tambahan| Sensor-sensor lain untuk mendukung fungsi Smart Home tambahan.         |

## 🔗 Komunikasi Sistem

Sistem menggunakan **komunikasi UART TTL** untuk mentransmisikan data antar perangkat dan sensor secara real-time. Arduino Mega memproses input dari sensor, lalu mengambil tindakan sesuai logika program.

## ⚡ Fitur Utama

- **Auto Cut-Off:** Memutus sambungan perangkat jika terjadi fluktuasi tegangan di luar ambang batas aman.
- **Monitoring Energi:** Penggunaan sensor ACS712 dan ZMPT101B untuk memantau konsumsi arus dan tegangan secara real-time.
- **Kontrol Perangkat Otomatis:** Menggunakan Relay SPDT yang dikendalikan berdasarkan data dari sensor.

## 📊 Diagram Blok dan Flowchart

![Diagram Blok Sistem](./block_diagram.png)
*Ilustrasi koneksi antar komponen utama.*

![Flowchart Logika Program](./flowchart_program.png)
*Logika pengambilan keputusan untuk auto cut-off.*

![Diagram Hardware Yang Akan Digunakan]
![Diagram Hardware](https://github.com/user-attachments/assets/b0157a11-7a6a-47e7-8a83-55169e7f089e)


## 🚀 Pengembangan Selanjutnya

- Integrasi dengan koneksi WiFi (ESP8266/ESP32) untuk kontrol via aplikasi mobile.
- Dashboard berbasis web untuk pemantauan konsumsi daya secara grafis.
- Otomatisasi berdasarkan waktu, cuaca, atau sensor gerak.

## 📁 Struktur Direktori (Opsional)
```bash
SmartHome-Automation/
│
├── src/                      # Kode program Arduino
├── images/                   # Diagram dan flowchart sistem
│   ├── block_diagram.png
│   └── flowchart_program.png
├── README.md                 # Dokumentasi proyek
└── docs/                     # Panduan penggunaan & pengembangan
