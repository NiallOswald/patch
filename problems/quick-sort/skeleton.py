
class QuickSort(object):

    def sort(self, data):
        # Handle invalid input by returning an empty list if data is None or not a list
        if not isinstance(data, list):
            return []
        if len(data) < 2:
            return data

        # Choose the pivot as the middle element
        pivot_index = len(data) // 2
        pivot = data[pivot_index]

        # Partition the list into two sublists: those smaller than the pivot and those greater or equal
        left = [x for x in data if x < pivot]
        right = [x for x in data if x >= pivot]

        # Recursively sort and combine 
        return self.sort(left) + self.sort(right)
