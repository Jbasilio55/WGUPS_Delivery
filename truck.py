import datetime

from hash_table import HashTable
from package import package_hash
from utils import calculate_distance, load_data


class Truck:

    def __init__(self, number, depart_time, current_location):
        self.address_hash = HashTable()
        self.package_list = []
        self.current_address = current_location
        self.next_address = ""
        self.truck_number = number
        self.depart_time = depart_time
        self.elapsed_time = depart_time
        self.route_miles = 0
        self.total_miles = 0

        self.load_address()  # Load addresses from a CSV file

    # Load addresses from a CSV file into the hash table
    # Time complexity: O(N), Space complexity: O(N)
    def load_address(self):
        address_list = load_data("csv_files/Address.csv")
        index = 0  # Initialize an index counter

        for address in address_list:
            index += 1  # Increment the index counter
            self.address_hash.insert(index, address[0])

    # Add packages to the truck's package list
    # Time complexity: O(N), Space complexity: O(N)
    def add_packages(self, package_list):
        for package_id in package_list:
            # Retrieve package information from the package hash
            package = package_hash.search(package_id)  # Time complexity: O(1)
            package.status = f"Delivery Package #{package_id} is en route on truck {self.truck_number}"
            # Add the package to the truck's package list
            self.package_list.append(package)  #Time complexity: O(N)

    # Get the total miles traveled by the truck
    # Time complexity: O(1), Space complexity: O(1)
    def get_miles(self):
        return self.total_miles

    # Get the list of packages loaded on the truck
    def get_package_list(self):
        return self.package_list

    # Plan the route and deliver packages
    # Time complexity: O(N^2), Space complexity: O(N)
    def route(self, time):
        # Change (user input) datetime to timedelta
        time_of_day = time - datetime.datetime.combine(time.date(), datetime.time())

        # Continue routing until all packages are delivered
        while len(self.package_list) > 0:
            # If elapse time is greater than time given break out of while-loop
            if time_of_day < self.elapsed_time:
                break

            if self.elapsed_time >= datetime.timedelta(hours=10, minutes=20):
                package_hash.search(9).address = "410 S State St"

            # Find the nearest neighbor and return (package and distance) --> [package, distance]
            package_distance = self.find_nearest_neighbor()

            # if package is not None
            if package_distance[0]:
                # If distance is greater than 0, then divide the distance by 18mph and add it to elapsed time
                if package_distance[1] > 0:
                    self.elapsed_time += datetime.timedelta(hours=package_distance[1] / 18)

                # add distance to total mileage
                self.route_miles += package_distance[1]

                # Search for package and update delivery status (Delivered: Time)
                package = package_hash.search(package_distance[0].package_id)
                package.status = "Delivered: " + str(self.elapsed_time)

                # Change current address to address of package
                self.current_address = package_distance[0].address

                # remove delivered packages
                self.package_list.remove(package_distance[0])

        # add distance traveled to total mileage
        self.total_miles += self.route_miles

        # reset data after each loop
        self.package_list = []
        self.current_address = "HUB"
        self.elapsed_time = self.depart_time
        self.route_miles = 0

    # Find the nearest neighbor package to the truck's current location
    # Time complexity: O(N), Space complexity: O(N)
    def find_nearest_neighbor(self):
        # make new list to store package and distance
        neighbor_distance = []
        min_distance = 10000
        nearest_neighbor = None

        # Iterate through each package in the package list
        for package in self.package_list:
            # Calculate the distance to next package
            distance = calculate_distance(package.address, self.current_address, self.address_hash)

            # Check if the calculated distance is less than the minimum distance
            if distance < min_distance:
                min_distance = distance
                nearest_neighbor = package

        # add package and distance to list
        neighbor_distance.append(nearest_neighbor)
        neighbor_distance.append(min_distance)

        return neighbor_distance
