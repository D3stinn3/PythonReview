class SearchingArray:

    def __init__(self, reference_array):
        self.reference_array = reference_array

    def the_search(self):
        arr = self.reference_array
        size_of_arr = len(arr)

        for i in range(0, size_of_arr):
            if arr[i] == 10:
                return 'Element found at index ', i

            return 'Element not found'


if "__name__" == "__main__":
    SearchingArray(reference_array=[0, 2, 4, 6, 8, 10])

