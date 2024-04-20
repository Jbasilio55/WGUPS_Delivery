# Author: Jorge Basilio
# Student ID: 011149553
# Title: Task 2 - WGUPS Routing Program Implementation

import datetime

from package import package_hash
from truck import Truck


# Function to input time in HH:MM format within a specific range
def input_time():
    while True:
        try:
            # Prompt the user to input time
            time_str = input("Enter time in HH:MM format (between 8:00 AM and 5:00 PM): ")
            # Split the input into hours and minutes
            hours, minutes = map(int, time_str.split(":"))
            if 8 <= hours <= 16 and 0 <= minutes <= 59:  # Hours from 8:00 to 16:59 (5:00 PM)
                return datetime.timedelta(hours=hours, minutes=minutes)
            else:
                print("Invalid time! Time should be between 8:00 AM and 5:00 PM.")
        except ValueError:
            print("Invalid input! Please enter time in HH:MM format.")


# Function to reset truck objects
def reset_trucks_and_packages():
    for i in range(1, len(package_hash.table) + 1):
        # Retrieve package information from the hash table
        package = package_hash.search(i).status = "At the HUB"

    global truck1, truck2, truck3
    truck1 = Truck(1, datetime.timedelta(hours=8, ), "HUB")
    truck2 = Truck(2, datetime.timedelta(hours=9, minutes=5), "HUB")
    truck3 = Truck(3, datetime.timedelta(hours=8), "HUB")


if __name__ == "__main__":
    # Initialize trucks with their respective departure times and starting addresses
    truck1 = Truck(1, datetime.timedelta(hours=8, ), "HUB")
    truck2 = Truck(2, datetime.timedelta(hours=9, minutes=5), "HUB")
    truck3 = Truck(3, datetime.timedelta(hours=8), "HUB")

    # Truck 1 --> Departs at 8:00
    # Package 15 due by 9:00, all others due by 10:30
    truck_one_packages = [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40]

    # Truck 2 --> Departs at 9:05
    # Packages 6 and 25 have 10:30 deadline
    truck_two_packages = [3, 6, 18, 25, 27, 28, 32, 33, 35, 36, 38, 39]

    # Truck 3 --> All EOD packages
    # truck3_departure_time = "8:00"
    # truck_three_packages = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 19, 21, 22, 23, 24, 26]
    truck_three_packages = [2, 4, 5, 7, 8, 10, 11, 12, 17, 19, 21, 22, 23, 24, 26]

    # Print the title of the program
    print("===========================================")
    print("Western Governors University Parcel Service")
    print("===========================================")

    try:
        while True:
            def get_package_info():
                for i in range(1, len(package_hash.table) + 1):
                    # Retrieve package information from the hash table
                    package = package_hash.search(i)
                    # Print package details
                    print(f"Package ID: {package.package_id} | Address: {package.address} | City: {package.city} | "
                          f"Zipcode: {package.zipcode} | Weight: {package.weight} | Deadline: {package.delivery_deadline} | "
                          f"Delivery Status: {package.status}")

            # function that takes calculates route distance and displays packages
            def start_route(chosen_time):
                # add packages to trucks
                truck1.add_packages(truck_one_packages)
                truck2.add_packages(truck_two_packages)
                truck3.add_packages(truck_three_packages)

                # calculate route
                truck1.route(chosen_time)
                truck2.route(chosen_time)
                truck3.route(chosen_time)

                # Display package information and truck mileage
                get_package_info()

                # Display truck info
                print()
                print(f"truck #1: {truck1.get_miles()}")
                print(f"truck #2: {truck2.get_miles()}")
                print(f"truck #3: {truck3.get_miles()}")
                print()

                # Calculate and display total truck mileage
                total_distance = truck1.get_miles() + truck2.get_miles() + truck3.get_miles()
                print(f"total truck mileage: {total_distance}")

                # Reset truck objects
                reset_trucks_and_packages()

            try:
                # User selection prompt
                print()
                print("Select all option using the number keys:")
                print("[1] View all packages delivered and Mileage...")
                print("[2] Look up a time...")
                print("[3] Exit...")

                key_pressed = int(input("Enter Number: "))

                # Function to get information about all packages
                # Display all package information when delivered if selected option is '1'
                if key_pressed == 1:
                    truck_three_packages.append(9)
                    # chosen time after all packages are delivered
                    time = "12:00"
                    latest_time = datetime.datetime.strptime(time, "%H:%M")

                    # calculate and display all packages
                    start_route(latest_time)

                    truck_three_packages.remove(9)
                # Handle the case where user wants to look up a time
                if key_pressed == 2:
                    print("Please type in a time")
                    time_input = input_time()
                    print("Time input:", time_input)

                    # Convert timedelta object to string in HH:MM format
                    time_str = "{:02}:{:02}".format(time_input.seconds // 3600, (time_input.seconds // 60) % 60)

                    # Parse the time string to a datetime object
                    time_obj = datetime.datetime.strptime(time_str, "%H:%M")

                    print("[1] Look up a package")
                    print("[2] Look up all packages")

                    key_pressed_2 = int(input())

                    # Check if the time input is before or after 9:05 AM
                    if time_obj.time() < datetime.time(9, 5):
                        if key_pressed_2 == 2:
                            # Assign packages to trucks and calculate routes
                            truck1.add_packages(truck_one_packages)
                            truck3.add_packages(truck_three_packages)

                            # Assign packages to trucks and calculate routes
                            truck1.route(time_obj)
                            truck3.route(time_obj)

                            # Display package information and truck mileage
                            get_package_info()
                            print(f"truck #1: {truck1.get_miles()}")
                            print(f"truck #2: 0")
                            print(f"truck #3: {truck3.get_miles()}")

                            # Calculate and display total truck mileage
                            total = truck1.get_miles() + truck3.get_miles()
                            print(f"total truck mileage: {total}")

                            # Reset truck objects
                            reset_trucks_and_packages()
                        else:
                            # Assign packages to trucks and calculate routes
                            truck1.add_packages(truck_one_packages)
                            truck3.add_packages(truck_three_packages)

                            # Assign packages to trucks and calculate routes
                            truck1.route(time_obj)
                            truck3.route(time_obj)

                            print("Enter Package ID: ")
                            package_id = int(input())

                            package = package_hash.search(package_id)

                            if package:
                                # Print package details
                                print(
                                    f"Package ID: {package.package_id} | Address: {package.address} | City: {package.city} | "
                                    f"Zipcode: {package.zipcode} | Weight: {package.weight} | Deadline: {package.delivery_deadline} | "
                                    f"Delivery Status: {package.status}")
                            else:
                                print("Sorry the package ID, you have entered does not exist.")

                            reset_trucks_and_packages()
                    else:
                        if key_pressed_2 == 2:
                            if time_obj.time() >= datetime.time(10, 20):
                                truck_three_packages.append(9)
                            # get all packages info
                            start_route(time_obj)
                        else:
                            if time_obj.time() >= datetime.time(10, 20):
                                truck_three_packages.append(9)

                            print("Enter Package ID: ")
                            package_id = int(input())

                            truck1.add_packages(truck_one_packages)
                            truck2.add_packages(truck_two_packages)
                            truck3.add_packages(truck_three_packages)

                            truck1.route(time_obj)
                            truck2.route(time_obj)
                            truck3.route(time_obj)

                            package = package_hash.search(package_id)

                            if package:
                                # Print package details
                                print(
                                    f"Package ID: {package.package_id} | Address: {package.address} | City: {package.city} | "
                                    f"Zipcode: {package.zipcode} | Weight: {package.weight} | Deadline: {package.delivery_deadline} | "
                                    f"Delivery Status: {package.status}")
                            else:
                                print("Sorry the package ID, you have entered does not exist.")

                            # Reset truck objects
                            reset_trucks_and_packages()
                # Exit the program if selected option is '3'
                if key_pressed == 3:
                    break
            except ValueError:
                print("Please type in a valid number")
    except KeyboardInterrupt:
        print()
