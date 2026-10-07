import numpy as np


arr = np.arange(1, 11)
print("Original Array:", arr)


print("First 5 elements:", arr[:5])
print("Last 3 elements:", arr[-3:])
print("Elements from index 2 to 7:", arr[2:8])


print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))


arr_modified = arr * 2   
print("Array after broadcasting (×2):", arr_modified)






