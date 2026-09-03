from datetime import datetime

TOTAL_SLOTS = 100
HOURLY_RATE = 30

parking_slots = {}

for slot in range(1, TOTAL_SLOTS + 1):
    parking_slots[slot] = None


def show_availability():
    available = 0

    print("\nAvailable Parking Slots:")

    for slot in parking_slots:
        if parking_slots[slot] is None:
            print(slot, end=" ")
            available += 1

    print("\n\nTotal Available Slots:", available)
    print("Occupied Slots:", TOTAL_SLOTS - available)

    if available == 0:
        print("Parking Area is FULL")


def validate_vehicle_number(vehicle_number):
    if len(vehicle_number) < 4:
        return False

    for character in vehicle_number:
        if not (character.isalnum() or character in "- "):
            return False

    return True


def find_vehicle(vehicle_number):
    for slot, vehicle in parking_slots.items():
        if vehicle is not None:
            if vehicle["number"].upper() == vehicle_number.upper():
                return slot

    return None


def allocate_slot():
    vehicle_number = input("\nEnter vehicle number: ").strip().upper()

    if not validate_vehicle_number(vehicle_number):
        print("Invalid vehicle number.")
        return

    existing_slot = find_vehicle(vehicle_number)

    if existing_slot is not None:
        print("Vehicle is already parked at slot", existing_slot)
        return

    available_slot = None

    for slot in parking_slots:
        if parking_slots[slot] is None:
            available_slot = slot
            break

    if available_slot is None:
        print("Parking Area is FULL.")
        return

    vehicle_type = input("Enter vehicle type (Car/Bike/Other): ").strip()

    entry_time = datetime.now()

    parking_slots[available_slot] = {
        "number": vehicle_number,
        "type": vehicle_type,
        "entry_time": entry_time
    }

    print("\nVehicle allocated successfully.")
    print("Vehicle Number:", vehicle_number)
    print("Vehicle Type:", vehicle_type)
    print("Allocated Slot:", available_slot)
    print("Entry Time:", entry_time.strftime("%d-%m-%Y %H:%M:%S"))


def release_slot():
    vehicle_number = input("\nEnter vehicle number: ").strip().upper()

    slot = find_vehicle(vehicle_number)

    if slot is None:
        print("Vehicle not found.")
        return

    vehicle = parking_slots[slot]

    exit_time = datetime.now()
    entry_time = vehicle["entry_time"]

    duration_seconds = (exit_time - entry_time).total_seconds()
    duration_hours = duration_seconds / 3600

    charged_hours = int(duration_hours)

    if duration_hours > charged_hours:
        charged_hours += 1

    if charged_hours < 1:
        charged_hours = 1

    charges = charged_hours * HOURLY_RATE

    print("\n========== PARKING BILL ==========")
    print("Vehicle Number :", vehicle["number"])
    print("Vehicle Type   :", vehicle["type"])
    print("Parking Slot   :", slot)
    print("Entry Time     :", entry_time.strftime("%d-%m-%Y %H:%M:%S"))
    print("Exit Time      :", exit_time.strftime("%d-%m-%Y %H:%M:%S"))
    print("Duration       :", round(duration_hours, 2), "hours")
    print("Charged Hours  :", charged_hours)
    print("Hourly Rate    : ₹", HOURLY_RATE)
    print("Total Charges  : ₹", charges)
    print("==================================")

    parking_slots[slot] = None

    print("Slot", slot, "has been released successfully.")


def view_occupied_slots():
    occupied = False

    print("\n========== OCCUPIED SLOTS ==========")

    for slot, vehicle in parking_slots.items():
        if vehicle is not None:
            occupied = True

            print(
                "Slot:", slot,
                "| Vehicle:", vehicle["number"],
                "| Type:", vehicle["type"],
                "| Entry:",
                vehicle["entry_time"].strftime("%d-%m-%Y %H:%M:%S")
            )

    if not occupied:
        print("No vehicles are currently parked.")

    print("=====================================")


def parking_status():
    occupied = 0

    for vehicle in parking_slots.values():
        if vehicle is not None:
            occupied += 1

    available = TOTAL_SLOTS - occupied

    print("\n========== PARKING STATUS ==========")
    print("Total Slots     :", TOTAL_SLOTS)
    print("Occupied Slots  :", occupied)
    print("Available Slots :", available)

    if occupied == TOTAL_SLOTS:
        print("Status          : PARKING AREA FULL")
    elif occupied == 0:
        print("Status          : PARKING AREA EMPTY")
    else:
        print("Status          : SPACE AVAILABLE")

    print("====================================")


def search_vehicle():
    vehicle_number = input("\nEnter vehicle number: ").strip().upper()

    slot = find_vehicle(vehicle_number)

    if slot is None:
        print("Vehicle not found.")
        return

    vehicle = parking_slots[slot]

    current_time = datetime.now()
    duration_seconds = (current_time - vehicle["entry_time"]).total_seconds()
    duration_hours = duration_seconds / 3600

    print("\n========== VEHICLE DETAILS ==========")
    print("Vehicle Number:", vehicle["number"])
    print("Vehicle Type  :", vehicle["type"])
    print("Parking Slot  :", slot)
    print(
        "Entry Time    :",
        vehicle["entry_time"].strftime("%d-%m-%Y %H:%M:%S")
    )
    print("Current Time  :", current_time.strftime("%d-%m-%Y %H:%M:%S"))
    print("Parked For    :", round(duration_hours, 2), "hours")
    print("=====================================")


while True:

    print("\n")
    print("==========================================")
    print("       PARKING MANAGEMENT SYSTEM")
    print("==========================================")
    print("1. Show Available Slots")
    print("2. Allocate Parking Slot")
    print("3. Release Parking Slot")
    print("4. View Occupied Slots")
    print("5. Parking Status")
    print("6. Search Vehicle")
    print("7. Exit")
    print("==========================================")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        show_availability()

    elif choice == "2":
        allocate_slot()

    elif choice == "3":
        release_slot()

    elif choice == "4":
        view_occupied_slots()

    elif choice == "5":
        parking_status()

    elif choice == "6":
        search_vehicle()

    elif choice == "7":
        print("\nThank you for using the Parking Management System.")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 7.")