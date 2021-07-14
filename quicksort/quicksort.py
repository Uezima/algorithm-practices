num_arrays = [1, 43, 21, 56, 32, 56, 45]

def quicksort(array):
    if (len(array) <= 2):
        return array
    pivot = array[0]
    lowest = [i for i in array[1:] if i <= pivot]
    highest = [i for i in array[1:] if i > pivot]
    return quicksort(lowest) + [pivot] + quicksort(highest)

print(quicksort(num_arrays))