import csv

from hash_table import HashTable


class Package:

    def __init__(self, package_id, address, city, state, zipcode, delivery_deadline, weight, note, status):
        self.package_id = package_id
        self.address = address
        self.delivery_deadline = delivery_deadline
        self.city = city
        self.zipcode = zipcode
        self.state = state
        self.weight = weight
        self.note = note
        self.status = status

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.package_id, self.address, self.city, self.state, self.zipcode,
            self.delivery_deadline, self.weight, self.note, self.status)


# https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=eee77a88-4de8-4d42-a3c3-ac8000ece256
def get_package_data(filename):
    with open(filename) as data:
        package_data = csv.reader(data, delimiter=",")
        next(package_data)  # skip header
        for package in package_data:  # Iterate over the CSV reader
            package_id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zipcode = package[4]
            delivery_deadline = package[5]
            weight = package[6]
            note = package[7]
            status = "At the HUB"

            # package Object
            pkg = Package(package_id, address, city, state, zipcode, delivery_deadline, weight, note, status)

            # insert into hash table
            package_hash.insert(package_id, pkg)


# hash instance
package_hash = HashTable()

get_package_data("csv_files/package.csv")
