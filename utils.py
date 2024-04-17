import csv


# load data from CSV file into list
# Time complexity: O(n), Space complexity: O(n)
def load_data(filename):
    # make new list
    mylist = []

    # iterate through file and get value for list that are seperated by comma
    with open(filename) as data:
        item_data = csv.reader(data, delimiter=",")
        next(item_data)  # skip header
        for row in item_data:
            # add info to list
            mylist.append(row)
    return mylist


# Time complexity: O(1), Space complexity: O(1)
def calculate_distance(package_address, current_address, address_hash):
    # Load the distance matrix data
    distance_matrix = load_data("csv_files/DistanceTable2.csv")

    # Retrieve the indices (row and column) from the address hash table
    index1 = address_hash.search(package_address)
    index2 = address_hash.search(current_address)

    # Retrieve the distance value from the distance matrix
    if index1 is not None and index2 is not None:

        # during lookup in distance matrix - distance[larger number][smaller number]
        if index1 > index2:

            distance = float(distance_matrix[index1 - 1][index2 - 1])
            return distance
        else:
            distance = float(distance_matrix[index2 - 1][index1 - 1])
            return distance
    else:
        # Handle the case where either address1 or address2 is not found
        print("Address not found in the data.")
        return None
