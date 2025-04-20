import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates
import datetime
import serial
import threading
import time
import random

# --- Inisialisasi koneksi serial ---
try:
    ser = serial.serial_for_url('rfc2217://localhost:4000', baudrate=115200, timeout=1)
    serial_status = "✅ Serial connected!"
except Exception as e:
    serial_status = f"❌ Gagal terhubung serial: {e}"
    ser = None

# --- GUI Setup ---
root = tk.Tk()
root.title("Smart Voltage Monitor")
root.geometry("1350x800")
root.configure(bg="#1e1e2f")

# --- Global variables ---
time_data = []
voltage_data = []
load_on = False
power_accumulated_kwh = 0.0
last_update_time = time.time()

# --- Styles ---
style = ttk.Style()
style.theme_use('clam')
style.configure("TLabel", background="#1e1e2f", foreground="white", font=("Segoe UI", 12))
style.configure("TButton", background="#00bfa6", foreground="white", font=("Segoe UI", 10, "bold"))
style.configure("TLabelframe", background="#2b2d42", foreground="white")
style.configure("TLabelframe.Label", font=("Segoe UI", 12, "bold"))

# --- Title & Status ---
ttk.Label(root, text="Lurcotte Monitoring", font=("Segoe UI", 20, "bold")).pack(pady=15)
status_label = ttk.Label(root, text=serial_status)
status_label.pack()

# --- Main Frame (Chart + Sidebar) ---
main_frame = tk.Frame(root, bg="#1e1e2f")
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# --- Chart Frame ---
frame_chart = tk.Frame(main_frame, bg="#2b2d42")
frame_chart.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

fig, ax = plt.subplots(figsize=(9, 4), facecolor='#2b2d42')
fig.patch.set_facecolor('#2b2d42')
ax.set_facecolor('#2b2d42')
ax.tick_params(colors='white')
for spine in ax.spines.values():
    spine.set_color('white')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
line, = ax.plot([], [], color='#00ffcc', linewidth=2, label='Voltage PLN')
ax.legend(loc='upper left', facecolor='#2b2d42', edgecolor='white', labelcolor='white')
canvas = FigureCanvasTkAgg(fig, master=frame_chart)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# --- Sidebar Frame (Kanan) ---
sidebar = tk.Frame(main_frame, bg="#1e1e2f", width=300)
sidebar.pack(side=tk.LEFT, fill=tk.Y)

# --- Info Voltage Saat Ini ---
current_voltage_label = ttk.Label(sidebar, text="Voltage Saat Ini: -- V", font=("Segoe UI", 14, "bold"))
current_voltage_label.pack(pady=10)

# --- Load Control Frame ---
load_frame = ttk.Labelframe(sidebar, text="💡 Kontrol Beban")
load_frame.pack(pady=10, fill=tk.X, padx=10)

def toggle_load():
    global load_on
    load_on = not load_on
    load_status_label.config(text="Status: 🔆 ON" if load_on else "Status: 💡 OFF")
    btn_load_toggle.config(text="Matikan" if load_on else "Nyalakan")

btn_load_toggle = ttk.Button(load_frame, text="Nyalakan", command=toggle_load)
btn_load_toggle.pack(pady=10, padx=10)

load_status_label = ttk.Label(load_frame, text="Status: 💡 OFF", font=("Segoe UI", 12))
load_status_label.pack(pady=5)

# --- Energy Info Frame ---
info_energy_frame = ttk.Labelframe(sidebar, text="📊 Informasi Daya")
info_energy_frame.pack(pady=10, fill=tk.X, padx=10)

power_label = ttk.Label(info_energy_frame, text="Daya (kWh): 0.000", font=("Segoe UI", 12))
power_label.pack(pady=5)

cost_label = ttk.Label(info_energy_frame, text="Biaya (Rp): 0", font=("Segoe UI", 12))
cost_label.pack(pady=5)

# --- Footer (Credit) ---
ttk.Label(root, text="Dikembangkan oleh Lurcotte Cooperation | 2025", font=("Segoe UI", 10), foreground="gray").pack(pady=5)

# --- Update Chart Function ---
def update_graph():
    ax.clear()
    ax.set_facecolor('#2b2d42')
    ax.tick_params(colors='white')
    for spine in ax.spines.values():
        spine.set_color('white')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    ax.plot(time_data, voltage_data, color='#00ffcc', linewidth=2, label='Voltage PLN')
    ax.set_title("Voltage PLN vs Waktu", color='white')
    ax.set_xlabel("Waktu", color='white')
    ax.set_ylabel("Tegangan (V)", color='white')
    ax.legend(loc='upper left', facecolor='#2b2d42', edgecolor='white', labelcolor='white')
    canvas.draw()

# --- Serial Read Thread ---
def read_serial():
    global power_accumulated_kwh, last_update_time

    while True:
        try:
            if ser and ser.in_waiting:
                line = ser.readline().decode('utf-8').strip()
                if line.startswith("V:"):
                    voltage = float(line[2:].strip())
                else:
                    continue
            else:
                voltage = random.uniform(210.0, 230.0)

            now = datetime.datetime.now()
            time_data.append(now)
            voltage_data.append(voltage)
            if len(time_data) > 60:
                time_data.pop(0)
                voltage_data.pop(0)

            current_voltage_label.config(text=f"Voltage Saat Ini: {voltage:.2f} V")
            update_graph()

            current_time = time.time()
            elapsed = current_time - last_update_time
            last_update_time = current_time

            if load_on:
                current_power = voltage * 0.2  # Asumsi 200W (0.2 kW)
                energy = current_power * (elapsed / 3600.0)  # dalam kWh
                power_accumulated_kwh += energy
                biaya = power_accumulated_kwh * 1500  # asumsi Rp1500/kWh

                power_label.config(text=f"Daya (kWh): {power_accumulated_kwh:.3f}")
                cost_label.config(text=f"Biaya (Rp): {int(biaya):,}".replace(',', '.'))

            time.sleep(1)

        except Exception as e:
            print("Error membaca data serial:", e)
            time.sleep(2)

# --- Start Serial Thread ---
threading.Thread(target=read_serial, daemon=True).start()

# --- Run App ---
root.mainloop()
