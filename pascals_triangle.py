'''
Generate Pascal's Triangle up to a given number of rows
Pascal's Triangle is a triangular array of numbers that has interesting properties and
appears in various areas of mathematics, including combinatorics, algebra, and probability

Each row of Pascal's Triangle represents the coefficients in the binomial expansion.
The triangle is constructed starting with the number 1 at the top. 
Each number below it is the sum of the two numbers directly above it. 
The sides of the triangle are always 1.
'''

def pascal_triangle(num_rows):
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
