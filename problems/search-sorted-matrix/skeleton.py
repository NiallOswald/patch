class SortedMatrix(object):

    def find_val(self, matrix, val):
        # Handle edge cases for invalid or empty matrix
        if not matrix or not matrix[0]:
            return None

        rows = len(matrix)
        cols = len(matrix[0])

        # Start at the top-right corner
        row = 0
        col = cols - 1

        # PITFALL: Notice the condition "col > 0" instead of "col >= 0".
        # This means as soon as col hits 0, we skip the last column check!
        while row < rows and col > 0:
            if matrix[row][col] == val:
                return (row, col)
            elif matrix[row][col] < val:
                row += 1
            else:
                col -= 1

        # If we exit the loop without finding the value, it\'s not present
        return None
