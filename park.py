import tkinter as tk
from tkinter import messagebox

# Initialize parking spots for each vehicle type
parking_spots_bike = [0] * 5  # 5 parking spots for Bike
parking_spots_semi_sedan = [0] * 5  # 5 parking spots for Semi-Sedan
parking_spots_sedan = [0] * 5  # 5 parking spots for Sedan
parking_spots_suv = [0] * 5  # 5 parking spots for SUV

# Function to get the first available parking spot based on the selected vehicle type
def get_available_spot(vehicle_type):
    if vehicle_type == "Bike":
        for i, spot in enumerate(parking_spots_bike):
            if spot == 0:
                return i, "Bike"
    elif vehicle_type == "Semi-Sedan":
        for i, spot in enumerate(parking_spots_semi_sedan):
            if spot == 0:
                return i, "Semi-Sedan"
    elif vehicle_type == "Sedan":
        for i, spot in enumerate(parking_spots_sedan):
            if spot == 0:
                return i, "Sedan"
    elif vehicle_type == "SUV":
        for i, spot in enumerate(parking_spots_suv):
            if spot == 0:
                return i, "SUV"
    return None, None

# Function to update parking GUI for the selected vehicle type
def update_parking_gui(vehicle_type):
    # Clear the previous display of parking spots
    for widget in frame_parking_spots.winfo_children():
        widget.destroy()

    # Select the correct parking spots list based on vehicle type
    if vehicle_type == "Bike":
        parking_spots = parking_spots_bike
    elif vehicle_type == "Semi-Sedan":
        parking_spots = parking_spots_semi_sedan
    elif vehicle_type == "Sedan":
        parking_spots = parking_spots_sedan
    elif vehicle_type == "SUV":
        parking_spots = parking_spots_suv
    else:
        return
    
    # Create new display for parking spots
    for i, spot in enumerate(parking_spots):
        color = "#B6E3A1" if spot == 0 else "#F5B7B1"  # Light green for empty, Light red for occupied
        label = tk.Label(frame_parking_spots, text=f"Spot {i+1}", width=15, height=5, bg=color, font=('Arial', 12, 'bold'), relief="solid", bd=2)
        label.grid(row=i//5, column=i%5, padx=15, pady=15)

# Function to handle vehicle entry
def vehicle_enter():
    vehicle_type = vehicle_type_var.get()
    spot, _ = get_available_spot(vehicle_type)
    
    if spot is not None:
        if vehicle_type == "Bike":
            parking_spots_bike[spot] = 1
        elif vehicle_type == "Semi-Sedan":
            parking_spots_semi_sedan[spot] = 1
        elif vehicle_type == "Sedan":
            parking_spots_sedan[spot] = 1
        elif vehicle_type == "SUV":
            parking_spots_suv[spot] = 1
        update_parking_gui(vehicle_type)
        messagebox.showinfo("Parking Assignment", f"{vehicle_type} assigned to spot {spot + 1}")
    else:
        messagebox.showwarning("No available spots", "Sorry, the parking lot is full for this vehicle type.")

# Function to handle vehicle exit
def vehicle_exit():
    try:
        spot_id = int(spot_entry.get()) - 1  # Subtract 1 to match the index (0-based)
        vehicle_type = vehicle_type_var.get()

        if vehicle_type == "Bike":
            if parking_spots_bike[spot_id] == 1:
                parking_spots_bike[spot_id] = 0
                update_parking_gui(vehicle_type)
                messagebox.showinfo("Vehicle Exit", f"{vehicle_type} left from spot {spot_id + 1}")
            else:
                messagebox.showwarning("Invalid Spot", "This spot is already empty.")
        elif vehicle_type == "Semi-Sedan":
            if parking_spots_semi_sedan[spot_id] == 1:
                parking_spots_semi_sedan[spot_id] = 0
                update_parking_gui(vehicle_type)
                messagebox.showinfo("Vehicle Exit", f"{vehicle_type} left from spot {spot_id + 1}")
            else:
                messagebox.showwarning("Invalid Spot", "This spot is already empty.")
        elif vehicle_type == "Sedan":
            if parking_spots_sedan[spot_id] == 1:
                parking_spots_sedan[spot_id] = 0
                update_parking_gui(vehicle_type)
                messagebox.showinfo("Vehicle Exit", f"{vehicle_type} left from spot {spot_id + 1}")
            else:
                messagebox.showwarning("Invalid Spot", "This spot is already empty.")
        elif vehicle_type == "SUV":
            if parking_spots_suv[spot_id] == 1:
                parking_spots_suv[spot_id] = 0
                update_parking_gui(vehicle_type)
                messagebox.showinfo("Vehicle Exit", f"{vehicle_type} left from spot {spot_id + 1}")
            else:
                messagebox.showwarning("Invalid Spot", "This spot is already empty.")
    except (ValueError, IndexError):
        messagebox.showwarning("Invalid Input", "Please enter a valid parking spot ID.")

# Function to display the parking slot size based on vehicle type
def display_parking_slot_size():
    vehicle_type = vehicle_type_var.get()

    if vehicle_type == "Bike":
        slot_size_label.config(text="Standard Bike Parking Slot: 1.5m x 2.5m")
        slot_size_label.config(bg="lightblue")
    elif vehicle_type == "Semi-Sedan":
        slot_size_label.config(text="Standard Semi-Sedan Parking Slot: 2.4m x 5m")
        slot_size_label.config(bg="lightyellow")
    elif vehicle_type == "Sedan":
        slot_size_label.config(text="Standard Sedan Parking Slot: 2.5m x 5m")
        slot_size_label.config(bg="lightgreen")
    elif vehicle_type == "SUV":
        slot_size_label.config(text="Standard SUV Parking Slot: 2.7m x 5.5m")
        slot_size_label.config(bg="lightcoral")
    else:
        messagebox.showwarning("Invalid Selection", "Please select a vehicle type.")
    
    # Update parking spots based on selected vehicle type
    update_parking_gui(vehicle_type)

# GUI Setup
root = tk.Tk()
root.title("Smart Parking System")
root.geometry("1000x1000")  # Window size

# Set the background color for the window
root.configure(bg="#F0F0F0")

# Parking Spots Display (Grid)
frame_parking_spots = tk.Frame(root, bg="#F0F0F0")
frame_parking_spots.grid(row=0, column=0, padx=20, pady=20)

# Control Panel for Vehicle Entry and Exit
frame_controls = tk.Frame(root, bg="#F0F0F0")
frame_controls.grid(row=1, column=0, padx=20, pady=20)

# Label for Vehicle Type Selection
tk.Label(frame_controls, text="Select Vehicle Type:", font=('Arial', 14), bg="#F0F0F0").grid(row=0, column=0, pady=10)

# Radio buttons for selecting vehicle type
vehicle_type_var = tk.StringVar()
vehicle_type_var.set("Bike")  # Default selection

tk.Radiobutton(frame_controls, text="Bike", variable=vehicle_type_var, value="Bike", font=('Arial', 12), bg="#F0F0F0").grid(row=1, column=0)
tk.Radiobutton(frame_controls, text="Semi-Sedan", variable=vehicle_type_var, value="Semi-Sedan", font=('Arial', 12), bg="#F0F0F0").grid(row=2, column=0)
tk.Radiobutton(frame_controls, text="Sedan", variable=vehicle_type_var, value="Sedan", font=('Arial', 12), bg="#F0F0F0").grid(row=3, column=0)
tk.Radiobutton(frame_controls, text="SUV", variable=vehicle_type_var, value="SUV", font=('Arial', 12), bg="#F0F0F0").grid(row=4, column=0)

# Button to display parking slot size
tk.Button(frame_controls, text="Show Parking Slot Size", command=display_parking_slot_size, width=20, height=2, font=('Arial', 12, 'bold'), bg="#4CAF50", fg="white", relief="raised").grid(row=5, column=0, columnspan=2, pady=15)

# Label to show parking slot size
slot_size_label = tk.Label(frame_controls, text="Please select a vehicle type", font=('Arial', 12), bg="#F0F0F0", width=40, height=3)
slot_size_label.grid(row=6, column=0, columnspan=2, pady=10)

# Label for Vehicle Exit Spot Entry
tk.Label(frame_controls, text="Enter Vehicle Spot ID (Exit):", font=('Arial', 12), bg="#F0F0F0").grid(row=7, column=0, pady=10)

# Entry field for spot number
spot_entry = tk.Entry(frame_controls, font=('Arial', 12))
spot_entry.grid(row=7, column=1, pady=10)

# Buttons for Vehicle Entry and Exit
tk.Button(frame_controls, text="Vehicle Enter", command=vehicle_enter, width=20, height=2, font=('Arial', 12, 'bold'), bg="#4CAF50", fg="white", relief="raised").grid(row=8, column=0, columnspan=2, pady=15)
tk.Button(frame_controls, text="Vehicle Exit", command=vehicle_exit, width=20, height=2, font=('Arial', 12, 'bold'), bg="#FF5733", fg="white", relief="raised").grid(row=9, column=0, columnspan=2, pady=15)

# Initial Parking Spot Setup (default vehicle type is Bike)
update_parking_gui("Bike")

# Start the GUI main loop
root.mainloop()
