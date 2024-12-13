import sqlite3

def setup_database():
    conn = sqlite3.connect('parking_system.db')
    cursor = conn.cursor()
    
    # Create table to store parking slot status
    cursor.execute('''CREATE TABLE IF NOT EXISTS parking_slots (
                        slot_id INTEGER PRIMARY KEY,
                        is_occupied INTEGER)''')
    
    # Initialize parking slots (e.g., 10 slots)
    cursor.executemany("INSERT OR IGNORE INTO parking_slots (slot_id, is_occupied) VALUES (?, ?)", 
                        [(i, 0) for i in range(1, 11)])
    
    conn.commit()
    conn.close()

def update_slot(slot_id, status):
    conn = sqlite3.connect('parking_system.db')
    cursor = conn.cursor()
    
    cursor.execute("UPDATE parking_slots SET is_occupied = ? WHERE slot_id = ?", (status, slot_id))
    
    conn.commit()
    conn.close()

def get_available_slot():
    conn = sqlite3.connect('parking_system.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT slot_id FROM parking_slots WHERE is_occupied = 0 LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    
    return result[0] if result else None

def get_slot_status():
    conn = sqlite3.connect('parking_system.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT slot_id, is_occupied FROM parking_slots")
    slots = cursor.fetchall()
    conn.close()
    
    return slots
