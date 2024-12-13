import tkinter as tk
from tkinter import messagebox
import sqlite3
import random
import time

# Setting up SQLite Database
def setup_database():
    conn = sqlite3.connect('smart_parking.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS parking_spots (
            id INTEGER PRIMARY KEY,
            is_occupied INTEGER
        )
    ''')
    # Initialize 10 parking spots (can adjust based on your need)
    for i in range(10):
        c.execute('INSERT OR IGNORE INTO parking_spots (id, is_occupied) VALUES (?, ?)', (i, 0))
    conn.commit()
    conn.close()

# Fetch available parking spots
def get_available_spot():
    conn = sqlite3.connect('smart_parking.db')
    c = conn.cursor()
    c.execute('SELECT id FROM parking_spots WHERE is_occupied = 0 LIMIT 1')
    spot = c.fetchone()
    conn.close()
    return spot

# Update parking spot status (occupied or available)
def update_parking_spot(spot_id, is_occupied):
    conn = sqlite3.connect('smart_parking.db')
    c = conn.cursor()
    c.execute('UPDATE parking_spots SET is_occupied = ? WHERE id = ?', (is_occupied, spot_id))
    conn.commit()
    conn.close()

# Vehicle enters the parking lot
def vehicle_enter():
    spot = get_available_spot()
    if spot:
        update_parking_spot(spot[0], 1)
        update_parking_gui()
        messagebox.showinfo("Parking Assignment", f"Vehicle assigned to spot {spot[0]}")
    else:
        messagebox.showwarning("No available spots", "Sorry, the parking lot is full.")

# Vehicle exits the parking lot
def vehicle_exit():
    spot_id = int(spot_entry.get())
    update_parking_spot(spot_id, 0)
    update_parking_gui()
    messagebox.showinfo("Vehicle Exit", f"Vehicle left the parking lot from spot {spot_id}")

# Function to update parking lot GUI
def update_parking_gui():
    conn = sqlite3.connect('smart_parking.db')
    c = conn.cursor()
    c.execute('SELECT id, is_occupied FROM parking_spots')
    spots = c.fetchall()
    conn.close()

    # Clear previous parking lot display
    for widget in frame_parking_spots.winfo_children():
        widget.destroy()

    # Display parking spots status
    for spot in spots:
        color = "green" if spot[1] == 0 else "red"
        label = tk.Label(frame_parking_spots, text=f"Spot {spot[0]}", width=10, height=3, bg=color)
        label.grid(row=spot[0]//5, column=spot[0]%5, padx=5, pady=5)

# GUI Setup
root = tk.Tk()
root.title("Smart Parking System")

# Setup parking lot display
frame_parking_spots = tk.Frame(root)
frame_parking_spots.grid(row=0, column=0, padx=10, pady=10)

# Control Panel
frame_controls = tk.Frame(root)
frame_controls.grid(row=1, column=0, padx=10, pady=10)

tk.Label(frame_controls, text="Enter Vehicle Spot ID (Exit):").grid(row=0, column=0)
spot_entry = tk.Entry(frame_controls)
spot_entry.grid(row=0, column=1)

tk.Button(frame_controls, text="Vehicle Enter", command=vehicle_enter).grid(row=1, column=0, columnspan=2, pady=5)
tk.Button(frame_controls, text="Vehicle Exit", command=vehicle_exit).grid(row=2, column=0, columnspan=2, pady=5)

# Initialize Database and Parking Lot
setup_database()
update_parking_gui()

# Start the GUI main loop
root.mainloop()
