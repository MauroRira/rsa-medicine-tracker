#first we define the medications and their details
import json
tachi = {
    "name": "Tachipirina",
    "daily_dose": 1,
    "quantity": 10,
    "expiration_date": "2026-08-15"
}
Depakin = {
    "name": "Depakin",
    "quantity": 5,
    "expiration_date": "2026-09-20"
}
Entumin = {
    "name": "Entumin",
    "quantity": 8,
    "expiration_date": "2026-10-10"
}
test_med = {
    "name": "TestMed",
    "quantity": 20,
    "expiration_date": "2023-12-31"
}
 # Try to load existing data from file
from datetime import datetime
today = datetime.today()
def restock_medicine(quantity: int) -> float:
    print("\n--- Restock Medicine ---")
    
    med_name = input("Which medicine do you want to restock? ")
    
    try:
        med_quantity = int(input(f"How many boxes of {med_name} are we loading? "))
    except ValueError:
        print("Please enter a valid number.")
        return  # 'return' stops the function immediately if there is an error

    found = False
    
    for item in medicine_list:
        if item["name"].lower() == med_name.lower(): 
            item["quantity"] += med_quantity
            print(f"Success! Updated {item['name']}. New total: {item['quantity']}")
            found = True
            break
            
    if not found:
        print(f"Warning: '{med_name}' is not in our system yet.")

def check_inventory(medicine_list: list) -> None:
    print("\n" + "="*40)
    print("📋 RSA MEDICINE INVENTORY CHECK")
    print("="*40)
    
    today = datetime.today()
    
    for item in medicine_list:
        print(f"\n🔹 Medication: {item['name']}")
        
        # 1. Controllo Scadenza
        try:
            exp_date = datetime.strptime(item["expiration_date"], "%Y-%m-%d")
            if today > exp_date:
                print("   🚨 ALERT: EXPIRED! Please discard.")
            else:
                print("   ✅ Status: Valid")
        except ValueError:
            print("   ❌ ERROR: Invalid date format.")
        
        # 2. Controllo Quantità (Giorni rimanenti)
        try:
            # .get() previene errori se il farmaco non ha ancora "daily_dose"
            dose = item.get("daily_dose", 1) 
            days_left = item["quantity"] / dose
            
            if days_left > 0:
                print(f"   📦 Quantity: {item['quantity']} (Enough for {days_left:.1f} days)")
            else:
                print("   🚨 ALERT: Out of stock!")
                
        except ZeroDivisionError:
            print("   ❌ ERROR: Daily dose cannot be zero.")
            
    print("\n" + "="*40)

def add_new_medicine(medicine_list: list) -> None:
    print("\n--- Add New Medicine ---")
    new_name = input("Enter the name of the new medicine: ")
    
    try:
        new_quantity = int(input(f"Enter the quantity for {new_name}: "))
    except ValueError:
        print("Please enter a valid number for quantity.")
        return  # FIXED: Use 'return' instead of 'continue' to exit the function
    
    new_exp_date = input(f"Enter the expiration date for {new_name} (YYYY-MM-DD): ")
    
    # Basic validation for date format
    try:
        datetime.strptime(new_exp_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return  # FIXED: Use 'return' here too
    
    # Create the new dictionary
    new_medicine = {
        "name": new_name,
        "quantity": new_quantity,
        "expiration_date": new_exp_date,
        "daily_dose": 1  # Added a default daily dose so check_inventory doesn't break!
    }
    
    # FIXED: Use the parameter name 'medicine_list', not the global 'mylist'
    medicine_list.append(new_medicine)
    
    # DEBUG PRINT: This proves the list grew!
    print(f"✅ Success! Added {new_name} to inventory.")
    print(f"🔍 DEBUG: The list now contains {len(medicine_list)} medicines.")
    
def remove_medicine(medicine_list: list) -> None:
    print("\n--- Remove Medicine ---")
    med_name = input("Enter the name of the medicine to remove: ")
    
    found = False
    
    for item in medicine_list:
        if item["name"].lower() == med_name.lower():
            # We found it! Remove this exact dictionary from the list
            medicine_list.remove(item)
            print(f"✅ Success! '{item['name']}' has been removed from the inventory.")
            found = True
            break # Stop searching, it's already gone
            
    if not found:
        print(f"⚠️ Warning: '{med_name}' was not found in the system.")
  

def save_data(medicine_list, filename="medicines.json"):
    try:
        # "w" means "write" mode. It creates the file or overwrites it.
        with open(filename, "w") as file:
            json.dump(medicine_list, file, indent=4)
        print(f"✅ Data successfully saved to {filename}.")
    except Exception as e:
        print(f"❌ Error saving data: {e}")

def load_data(filename="medicines.json"):
    try:
        # "r" means "read" mode.
        with open(filename, "r") as file:
            loaded_list = json.load(file)
            print(f"✅ Data successfully loaded from {filename}.")
            return loaded_list
    except FileNotFoundError:
        # This happens the very first time you run the program (file doesn't exist yet)
        print("ℹ️ No saved data found. Starting with default inventory.")
        return None # We will handle this in the main code
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None

print("--- Welcome to the RSA Medicine Tracker ---")
mylist = load_data() 
# This loop will run forever until we hit 'break'
while True:
    print("\nWhat would you like to do?")
    print("1. Check Inventory")
    print("2. Restock Medicine")
    print("3. Add New Medicine ")
    print("4. Remove Medicine")
    print("5. Exit Program")
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    if choice == "1":
        check_inventory(mylist)
        
    elif choice == "2":
        restock_medicine(mylist)

    elif choice == "3":
        add_new_medicine(mylist)

    elif choice == "4":
        remove_medicine(mylist)

    elif choice == "5":
        print("Saving changes and exiting... Goodbye!")
        save_data(mylist)  # Save the current state of the inventory to a file
        break  # This stops the while loop and ends the program
        
    else:
        print("Invalid choice. Please enter 1, 2,3, 4 or 5.")

print("--- Program finished ---")