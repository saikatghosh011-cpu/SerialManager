import pandas as pd
import os

DATA_FILE = "serial_numbers.xlsx"

def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_excel(DATA_FILE)
    else:
        return pd.DataFrame(columns=["SerialNumber"])

def save_data(df):
    df.to_excel(DATA_FILE, index=False)

def add_serial_number(serial):
    df = load_data()
    if serial in df["SerialNumber"].values:
        print(f"❌ Serial number {serial} already exists!")
        return False
    else:
        df = pd.concat([df, pd.DataFrame({"SerialNumber": [serial]})], ignore_index=True)
        save_data(df)
        print(f"✅ Serial number {serial} added successfully.")
        return True

def search_serial_number(serial):
    df = load_data()
    if serial in df["SerialNumber"].values:
        print(f"🔎 Serial number {serial} FOUND in database.")
        return True
    else:
        print(f"🔎 Serial number {serial} NOT found.")
        return False

def main():
    print("=== Serial Number Manager ===")
    while True:
        print("\nOptions:")
        print("1. Add new serial number")
        print("2. Search serial number")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            serial = input("Enter serial number: ")
            add_serial_number(serial.strip())
        elif choice == "2":
            serial = input("Enter serial number to search: ")
            search_serial_number(serial.strip())
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
