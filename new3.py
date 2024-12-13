import tkinter as tk
from tkinter import messagebox

# Initialize parking spots as a list, 0 represents empty, 1 represents occupied
parking_spots = [0] * 1  # 10 parking spots

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
        color = "#B6E3A1" if spot == 0 else "#F5B7B1"  # Light green for empty, Light red for occupied
        label = tk.Label(frame_parking_spots, text=f"Spot {i+1}", width=15, height=5, bg=color, font=('Arial', 12, 'bold'), relief="solid", bd=2)
        label.grid(row=i//5, column=i%5, padx=15, pady=15)

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
root.geometry("600x500")  # Window size to make it spacious

# Set the background color for the window
root.configure(bg="#F0F0F0")

# Parking Spots Display (Grid)
frame_parking_spots = tk.Frame(root, bg="#F0F0F0")
frame_parking_spots.grid(row=0, column=0, padx=20, pady=20)

# Control Panel for Vehicle Entry and Exit
frame_controls = tk.Frame(root, bg="#F0F0F0")
frame_controls.grid(row=1, column=0, padx=20, pady=20)

# Label for Vehicle Exit Spot Entry
tk.Label(frame_controls, text="Enter Vehicle Spot ID (Exit):", font=('Arial', 12), bg="#F0F0F0").grid(row=0, column=0, pady=10)

# Entry field for spot number
spot_entry = tk.Entry(frame_controls, font=('Arial', 12))
spot_entry.grid(row=0, column=1, pady=10)

# Buttons for Vehicle Entry and Exit
tk.Button(frame_controls, text="Vehicle Enter", command=vehicle_enter, width=20, height=2, font=('Arial', 12, 'bold'), bg="#4CAF50", fg="white", relief="raised").grid(row=1, column=0, columnspan=2, pady=15)
tk.Button(frame_controls, text="Vehicle Exit", command=vehicle_exit, width=20, height=2, font=('Arial', 12, 'bold'), bg="#FF5733", fg="white", relief="raised").grid(row=2, column=0, columnspan=2, pady=15)

# Initial Parking Spot Setup
update_parking_gui()

# Start the GUI main loop
root.mainloop()
