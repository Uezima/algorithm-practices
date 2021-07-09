num_array = [23, 21, 45, 123, 3, 0, 11, 56, 99, 33, 2, 4, 1, 55, 78, 29, 20, 30]

def find_smallest_number(array):
    smallest = array[0]
    for i in range(len(array)):
        if(array[i] < smallest):
            smallest = array[i]
    return smallest

def sort_to_largest(array):
    sorted_array = []
    for i in range(len(array)):
        smallest = find_smallest_number(array)
        sorted_array.append(smallest)
        array.remove(smallest)
    return sorted_array

print(sort_to_largest(num_array))