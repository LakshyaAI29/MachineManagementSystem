import datetime

DATA_FILE = "machine_data.txt"

def is_valid_date(date_str):
    """Check if date is in YYYY-MM-DD format."""
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def add_machine():
    print("\n--- Add New Machine ---")
    machine_id = input("Enter unique Machine ID (e.g., M101): ").strip()
    name = input("Enter Machine Name: ").strip()
    mtype = input("Enter Machine Type (e.g., CNC, Robot): ").strip()
    
    while True:
        last_maint = input("Enter Last Maintenance Date (YYYY-MM-DD): ").strip()
        if is_valid_date(last_maint):
            break
        print("⚠️ Invalid date format. Please enter YYYY-MM-DD.")
    
    status = input("Enter Status (Working / Needs Repair): ").strip()

    with open(DATA_FILE, "a") as file:
        file.write(f"{machine_id},{name},{mtype},{last_maint},{status}\n")

    print("✅ Machine added successfully.\n")

def view_all_machines():
    print("\n--- All Machine Records ---")
    try:
        with open(DATA_FILE, "r") as file:
            data = file.readlines()
            if not data:
                print("⚠️ No machines found.\n")
                return
            
            print(f"{'ID':<8} {'Name':<25} {'Type':<10} {'Last Maint.':<12} {'Status'}")
            print("-" * 65)
            for line in data:
                machine_id, name, mtype, last_maint, status = map(str.strip, line.split(","))
                print(f"{machine_id:<8} {name:<25} {mtype:<10} {last_maint:<12} {status}")
            print()
    except FileNotFoundError:
        print("⚠️ Machine data file not found.\n")

def search_machine():
    search_id = input("\nEnter Machine ID to search: ").strip().lower()
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                machine_id = line.split(",")[0].strip().lower()
                if search_id == machine_id:
                    machine_id, name, mtype, last_maint, status = map(str.strip, line.split(","))
                    print("\n🔍 Machine Found:")
                    print(f"ID: {machine_id}")
                    print(f"Name: {name}")
                    print(f"Type: {mtype}")
                    print(f"Last Maintenance Date: {last_maint}")
                    print(f"Status: {status}\n")
                    break
            else:
                print("❌ Machine not found.\n")
    except FileNotFoundError:
        print("⚠️ Machine data file not found.\n")

def delete_machine():
    delete_id = input("\nEnter Machine ID to delete: ").strip().lower()
    try:
        with open(DATA_FILE, "r") as file:
            lines = file.readlines()

        with open(DATA_FILE, "w") as file:
            for line in lines:
                machine_id = line.split(",")[0].strip().lower()
                if machine_id != delete_id:
                    file.write(line)
                else:
                    print(f"🗑️ Machine ID {delete_id.upper()} deleted successfully.\n")
                    # No write → effectively deletes this record
            else:
                # If the loop finishes without deleting, print not found
                if all(line.split(",")[0].strip().lower() != delete_id for line in lines):
                    print("❌ Machine not found.\n")
    except FileNotFoundError:
        print("⚠️ Machine data file not found.\n")

def update_machine():
    update_id = input("\nEnter Machine ID to update: ").strip().lower()
    try:
        with open(DATA_FILE, "r") as file:
            lines = file.readlines()

        updated = False
        with open(DATA_FILE, "w") as file:
            for line in lines:
                machine_id = line.split(",")[0].strip().lower()
                if machine_id == update_id:
                    print(f"\n✏️ Updating Machine ID: {update_id.upper()}")
                    name = input("New Machine Name: ").strip()
                    mtype = input("New Machine Type: ").strip()
                    
                    while True:
                        last_maint = input("New Last Maintenance Date (YYYY-MM-DD): ").strip()
                        if is_valid_date(last_maint):
                            break
                        print("⚠️ Invalid date format. Please enter YYYY-MM-DD.")
                    
                    status = input("New Status (Working / Needs Repair): ").strip()
                    file.write(f"{update_id},{name},{mtype},{last_maint},{status}\n")
                    updated = True
                    print("✅ Machine updated successfully.\n")
                else:
                    file.write(line)
        
        if not updated:
            print("❌ Machine not found.\n")
    except FileNotFoundError:
        print("⚠️ Machine data file not found.\n")

def main_menu():
    while True:
        print("====== MACHINE MANAGEMENT SYSTEM ======")
        print("1. Add Machine")
        print("2. View All Machines")
        print("3. Search Machine by ID")
        print("4. Delete Machine by ID")
        print("5. Update Machine by ID")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_machine()
        elif choice == "2":
            view_all_machines()
        elif choice == "3":
            search_machine()
        elif choice == "4":
            delete_machine()
        elif choice == "5":
            update_machine()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, please enter a number from 1 to 6.\n")

if __name__ == "__main__":
    main_menu()
