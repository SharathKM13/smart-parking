import tkinter as tk
from tkinter import messagebox

# Initialize parking spots as a list, 0 represents empty, 1 represents occupied
parking_spots = [0] * 10  # 10 parking spots

# Function to get the first available parking spot
def get_available_spot():
    for i, spot in enumerate(parking_spots):
        if spot == 0:
            return i
    return None

# Function to update parking spot status in the GUI
def update_parking_gui():
    # Clear the previous display of parking spots
    for widget in frame_parking_spots.winfo_children():
        widget.destroy()

    # Create new display for parking spots
    for i, spot in enumerate(parking_spots):
        color = "green" if spot == 0 else "red"
        label = tk.Label(frame_parking_spots, text=f"Spot {i+1}", width=10, height=3, bg=color)
        label.grid(row=i//5, column=i%5, padx=5, pady=5)

# Function when a vehicle enters the parking lot
def vehicle_enter():
    spot = get_available_spot()
    if spot is not None:
        parking_spots[spot] = 1
        update_parking_gui()
        messagebox.showinfo("Parking Assignment", f"Vehicle assigned to spot {spot + 1}")
    else:
        messagebox.showwarning("No available spots", "Sorry, the parking lot is full.")

# Function when a vehicle exits the parking lot
def vehicle_exit():
    try:
        spot_id = int(spot_entry.get()) - 1  # Subtract 1 to match the index (0-based)
        if parking_spots[spot_id] == 1:
            parking_spots[spot_id] = 0
            update_parking_gui()
            messagebox.showinfo("Vehicle Exit", f"Vehicle left from spot {spot_id + 1}")
        else:
            messagebox.showwarning("Invalid Spot", "This spot is already empty.")
    except (ValueError, IndexError):
        messagebox.showwarning("Invalid Input", "Please enter a valid parking spot ID.")

# GUI Setup
root = tk.Tk()
root.title("Smart Parking System")

# Parking Spots Display
frame_parking_spots = tk.Frame(root)
frame_parking_spots.grid(row=0, column=0, padx=10, pady=10)

# Control Panel for Vehicle Entry and Exit
frame_controls = tk.Frame(root)
frame_controls.grid(row=1, column=0, padx=10, pady=10)

# Vehicle Exit Spot Entry
tk.Label(frame_controls, text="Enter Vehicle Spot ID (Exit):").grid(row=0, column=0)
spot_entry = tk.Entry(frame_controls)
spot_entry.grid(row=0, column=1)

# Buttons for Vehicle Entry and Exit
tk.Button(frame_controls, text="Vehicle Enter", command=vehicle_enter).grid(row=1, column=0, columnspan=2, pady=5)
tk.Button(frame_controls, text="Vehicle Exit", command=vehicle_exit).grid(row=2, column=0, columnspan=2, pady=5)

# Initial Parking Spot Setup
update_parking_gui()

# Start the GUI main loop
root.mainloop()
