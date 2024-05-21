def perform_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

numbers = [65, 37, 75, 18, 62, 55, 70]
sorted_numbers = perform_bubble_sort(numbers)
print("Sorted list:", sorted_numbers)

def perform_selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

strings = ["milk", "cake", "juice", "burger", "choclate"]
sorted_strings = perform_selection_sort(strings)
print("Sorted list:", sorted_strings)
