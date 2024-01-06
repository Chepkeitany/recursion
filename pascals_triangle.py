'''
Generate Pascal's Triangle up to a given number of rows
Pascal's Triangle is a triangular array of numbers that has interesting properties and
appears in various areas of mathematics, including combinatorics, algebra, and probability

Each row of Pascal's Triangle represents the coefficients in the binomial expansion.
The triangle is constructed starting with the number 1 at the top. 
Each number below it is the sum of the two numbers directly above it. 
The sides of the triangle are always 1.

Time Complexity: O(n^2) - where n if the number of rows. The function makes n
                          recursive calls until the base case is reached. In each call,
                          we also construct a new row based on the previous row which takes i time
                          depending on the number of elements in that row
                          which is n for the last row
                          The time taken for all rows from 1 to num_rows is given by
                          the following arithmetic progression formula:
                          num_rows (num_rows + 1) / 2 which can be simplified as num_rows^2
Space Complexity: O(n^2) - Since we store a list of each row of the pascal triangle,
                           the space required is equal given the arithmetic formula above.
                           Therefore, space required is num_rows ^2.
                           The recursive call stack is O(num_rows)
                           because we make n recursive calls until the base case is reached.
                           The dominant power in the space complexity is num_rows ^ 2                 
'''

def pascal_triangle(num_rows):
    """ Generate Pascal's Triangle up to a given number of rows """
    if num_rows == 0:
        return []
    if num_rows == 1:
        return [[1]]
    triangle = pascal_triangle(num_rows - 1)
    previous_row = triangle[-1]

    current_row = [1]
    for i in range(1, num_rows - 1):
        adjacent_elements_sum = previous_row[i - 1] + previous_row[i]
        current_row.append(adjacent_elements_sum)

    current_row.append(1)
    triangle.append(current_row)

    return triangle

assert pascal_triangle(1) == [
                                [1]
                             ],              "Failed on pascal_triangle(1)"
assert pascal_triangle(3) == [
                                [1],
                               [1, 1],
                              [1, 2, 1]
                             ],              "Failed on pascal_triangle(3)"
assert pascal_triangle(4) == [
                                [1],
                               [1, 1],
                              [1, 2, 1],
                             [1, 3, 3, 1]
                             ],             "Failed on pascal_triangle(5)"

print("All tests passed!")
