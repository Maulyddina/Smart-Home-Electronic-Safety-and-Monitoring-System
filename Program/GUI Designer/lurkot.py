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
root.configure(bg="#0f172a")  # dark navy blue

# --- Global Variables ---
time_data = []
voltage_data = []
load_on = False
power_accumulated_kwh = 0.0
last_update_time = time.time()

# --- Styles ---
style = ttk.Style()
style.theme_use('clam')
style.configure("TLabel", background="#0f172a", foreground="white", font=("Segoe UI", 12))
style.configure("TButton", background="#1e293b", foreground="white", font=("Segoe UI", 10, "bold"))
style.configure("Custom.TLabelframe", background="#1e293b", foreground="white", font=("Segoe UI", 12, "bold"))
style.configure("Custom.TLabelframe.Label", background="#1e293b", foreground="white")

# --- Header ---
header_frame = tk.Frame(root, bg="#1e293b")
header_frame.pack(fill=tk.X, padx=0, pady=0)

app_title = tk.Label(header_frame, text="⚡ Lurcotte", font=("Segoe UI", 20, "bold"), fg="#00f5d4", bg="#1e293b")
app_title.pack(pady=10)
status_label = ttk.Label(header_frame, text=serial_status)
status_label.pack(pady=2)

# --- Main Frame ---
main_frame = tk.Frame(root, bg="#0f172a")
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# --- Chart Frame ---
frame_chart = tk.Frame(main_frame, bg="#1e293b")
frame_chart.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
main_frame.grid_rowconfigure(0, weight=3)
main_frame.grid_columnconfigure(0, weight=3)
main_frame.grid_columnconfigure(1, weight=1)

fig, ax = plt.subplots(figsize=(10, 4), facecolor='#1e293b')
fig.patch.set_facecolor('#1e293b')
ax.set_facecolor('#1e293b')
ax.tick_params(colors='white')
for spine in ax.spines.values():
    spine.set_color('white')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
line, = ax.plot([], [], color='#00ffcc', linewidth=2, label='Voltage PLN')
ax.legend(loc='upper left', facecolor='#1e293b', edgecolor='white', labelcolor='white')
canvas = FigureCanvasTkAgg(fig, master=frame_chart)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# --- Info Panel ---
info_panel = tk.Frame(main_frame, bg="#1e293b")
info_panel.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

current_voltage_label = ttk.Label(info_panel, text="Voltage Saat Ini: -- V", font=("Segoe UI", 16, "bold"))
current_voltage_label.pack(pady=15)

# --- Load Control Frame ---
load_frame = ttk.Labelframe(info_panel, text="Kontrol Beban", style="Custom.TLabelframe")
load_frame.pack(fill=tk.X, padx=10, pady=10)

def toggle_load():
    global load_on
    load_on = not load_on
    load_status_label.config(text="Lampu: 🔆 ON" if load_on else "Lampu: 💡 OFF")
    btn_load_toggle.config(text="Matikan" if load_on else "Nyalakan")

btn_load_toggle = ttk.Button(load_frame, text="Nyalakan", command=toggle_load)
btn_load_toggle.pack(pady=8)

load_status_label = ttk.Label(load_frame, text="Lampu: 💡 OFF", font=("Segoe UI", 14))
load_status_label.pack(pady=5)

# --- Energy Info Frame ---
info_energy_frame = ttk.Labelframe(info_panel, text="Informasi Daya", style="Custom.TLabelframe")
info_energy_frame.pack(fill=tk.X, padx=10, pady=10)

power_label = ttk.Label(info_energy_frame, text="Daya (kWh): 0.000")
power_label.pack(pady=8)

cost_label = ttk.Label(info_energy_frame, text="Biaya (Rp): 0")
cost_label.pack(pady=8)

# --- Footer Note ---
footer = tk.Label(root, text="Developed by Lurcotte Corporation | Politeknik Elektronika Negeri Surabaya", font=("Segoe UI", 10), bg="#0f172a", fg="#94a3b8")
footer.pack(pady=5)

# --- Update Graph ---
def update_graph():
    ax.clear()
    ax.set_facecolor('#1e293b')
    ax.tick_params(colors='white')
    for spine in ax.spines.values():
        spine.set_color('white')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    ax.plot(time_data, voltage_data, color='#00ffcc', linewidth=2, label='Voltage PLN')
    ax.set_title("Voltage PLN vs Waktu", color='white')
    ax.set_xlabel("Waktu", color='white')
    ax.set_ylabel("Tegangan (V)", color='white')
    ax.legend(loc='upper left', facecolor='#1e293b', edgecolor='white', labelcolor='white')
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
                current_power = voltage * 0.2
                energy = current_power * (elapsed / 3600.0)
                power_accumulated_kwh += energy
                biaya = power_accumulated_kwh * 1500

                power_label.config(text=f"Daya (kWh): {power_accumulated_kwh:.3f}")
                cost_label.config(text=f"Biaya (Rp): {int(biaya):,}".replace(',', '.'))

            time.sleep(1)

        except Exception as e:
            print("Error membaca data serial:", e)
            time.sleep(2)

# --- Start Thread ---
threading.Thread(target=read_serial, daemon=True).start()

# --- Run App ---
root.mainloop()
