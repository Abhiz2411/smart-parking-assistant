import serial
import time
import tkinter as tk
from tkinter import ttk

# Set up the serial port connection
arduino_port = 'COM7'  # Change this to your Arduino port
baud_rate = 9600

ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Wait for the serial connection to initialize

# Create the GUI
root = tk.Tk()
root.title("Smart Parking Assistant")
root.geometry("800x600")  # Increased size to accommodate more sensors

# Set styles
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TFrame", background="#F5F5F5")
style.configure("Recommendation.TLabel", font=("Helvetica", 14, 'bold'), foreground="blue")

# Create frames
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill="both", expand=True)

sensor_frame = ttk.Frame(main_frame, padding="10", style="TFrame")
sensor_frame.pack(pady=20)

recommendation_frame = ttk.Frame(main_frame, padding="10", style="TFrame")
recommendation_frame.pack(pady=20)

# Labels to show sensor status
sensor_labels = []
for i in range(10):
    label = ttk.Label(sensor_frame, text=f"IR Sensor {i+1}: Checking...", style="TLabel")
    label.grid(row=i//2, column=i%2, pady=5, padx=10)  # Arrange labels in a 5x2 grid
    sensor_labels.append(label)

recommendation_label = ttk.Label(recommendation_frame, text="Recommendation: Checking...", style="Recommendation.TLabel")
recommendation_label.pack(pady=20)

def update_labels():
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        if line.startswith("Combined status: "):
            sensor_statuses = line.split(": ")[1].split(',')
            
            available_spots = []
            for i, status in enumerate(sensor_statuses):
                if status == '0':
                    sensor_labels[i].config(text=f"IR Sensor {i+1}: Object detected", foreground="red")
                else:
                    sensor_labels[i].config(text=f"IR Sensor {i+1}: No object detected", foreground="green")
                    available_spots.append(i+1)

            # AI-like decision making for parking recommendation
            if len(available_spots) == 0:
                recommendation_label.config(text="Recommendation: No spots available")
            elif len(available_spots) == 1:
                recommendation_label.config(text=f"Recommendation: Park at spot {available_spots[0]}")
            else:
                recommendation_label.config(text=f"Recommendation: Multiple spots available. Closest is spot {available_spots[0]}")

    root.after(500, update_labels)  # Schedule the function to run again after 500 ms

update_labels()

root.mainloop()