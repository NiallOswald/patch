class QuickSort(object):

    def sort(self, data):
        if type(data) != list:
            raise TypeError("Input must be a list")
        
        if len(data) <= 1:
            return data

        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]

        return self.sort(left) + middle + self.sort(right)