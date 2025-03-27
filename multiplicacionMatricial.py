import numpy as np
import math as math

def canMultiply(matrix1, matrix2): # Create a function to check if the matrices can be multiplied, checking the number of columns of the first matrix and the number of rows of the second matrix, taking into account the multiplication will be matrix1 times matrix2

    matrix1Columns = len(matrix1[0]) # Get the columns of the matrix number 1 
    matrix2Rows = len(matrix2) # Get the rows of the matrix number 2

    if matrix1Columns == matrix2Rows:
        return True
    else:
        return False
    

def getNumberRowsAndColumns(matrix):
    rows = len(matrix)  # Get the number of rows of the matrix
    columns = len(matrix[0]) # Get the number of columns of the matrix

    return rows, columns # Return the number of rows and columns of the matrix

def get2x2Matrix(matrix1):
    a = [ [matrix1[0][0] , matrix1[0][1]],
          [matrix1[1][0] , matrix1[1][1]]]
    
    b = [ [matrix1[0][2] , matrix1[0][3]],
          [matrix1[1][2] , matrix1[1][3]]]
    
    c = [ [matrix1[2][0] , matrix1[2][1]], 
          [matrix1[3][0] , matrix1[3][1]]]
    
    d = [ [matrix1[2][2] , matrix1[2][3]], 
          [matrix1[3][2] , matrix1[3][3]]]

    return a, b, c, d

def sumMatrix(matrix1 , matrix2): # sumMatrix all the elements of the matrices
    rowsMatrix1 , columnsMatrix1 = getNumberRowsAndColumns(matrix1)
    rowsMatrix2 , columnsMatrix2 = getNumberRowsAndColumns(matrix2)

    if rowsMatrix1 == rowsMatrix2 and columnsMatrix1 == columnsMatrix2:
        result = [[0 for x in range(columnsMatrix1)] for y in range(rowsMatrix1)]
        for i in range(rowsMatrix1):
            for j in range(columnsMatrix1):
                result[i][j] = matrix1[i][j] + matrix2[i][j]
        return result
    else:
        return False
    
def multiply(matrix1, matrix2):  # Multiply all the elements of 2x2 matrices
    result = [[0, 0], 
                [0, 0]]
    
    for i in range(2):
        for j in range(2):
            result[i][j] = sum(matrix1[i][k] * matrix2[k][j] for k in range(2))
    return result

def multiplyScalar(matrix1 , scalar):
    rowsMatrix1 , columnsMatrix1 = getNumberRowsAndColumns(matrix1)
    result = [[0 for x in range(columnsMatrix1)] for y in range(rowsMatrix1)]
    for i in range(rowsMatrix1):
        for j in range(columnsMatrix1):
            result[i][j] = matrix1[i][j] * scalar
    return result

def strassenAlgorithm4x4(a11 , a12 , a21 , a22 , b11 , b12 , b21 , b22):
    # Strassen's algorithm
    
    p1 = multiply(sumMatrix(a11 , a22) , (sumMatrix(b11 , b22))) # p1 = (a11 + a22) * (b11 + b22)
    p2 = multiply(sumMatrix(a21 , a22) , b11) # p2 = (a21 + a22) * b11
    p3 = multiply(a11 , sumMatrix(b12 , multiplyScalar(b22 , -1))) # p3 = a11 * (b12 - b22)
    p4 = multiply(a22 , sumMatrix(b21 , multiplyScalar(b11 , -1))) # p4 = a22 * (b21 - b11)
    p5 = multiply(sumMatrix(a11 , a12) , b22) # p5 = (a11 + a12) * b22
    p6 = multiply(sumMatrix(a21 , multiplyScalar(a11 , -1)) , sumMatrix(b11 , b12)) # p6 = (a21 - a11) * (b11 + b12)
    p7 = multiply(sumMatrix(a12 , multiplyScalar(a22 , -1)) , sumMatrix(b21 , b22)) # p7 = (a12 - a22) * (b21 + b22)

    c11 = sumMatrix(p1 , sumMatrix(p4 , sumMatrix(p7 , multiplyScalar(p5 , -1)))) # c11 = p1 + p4 - p5 + p7
    c12 = sumMatrix(p3 , p5) # c12 = p3 + p5
    c21 = sumMatrix(p2 , p4) # c21 = p2 + p4
    c22 = sumMatrix(p1 , sumMatrix(p3 , sumMatrix(p6 , multiplyScalar(p2 , -1)))) # c22 = p1 + p3 - p2 + p6        

    # Organize the results for the final matrix
    c11 = np.array(c11) 
    c12 = np.array(c12)
    c21 = np.array(c21)
    c22 = np.array(c22)

    # Constructing the final matrix 'c' from the blocks
    c = np.block([[c11, c12], [c21, c22]])

    return c
    
def addCerosUltil2n(matrix1):
    rowsMatrix1, columnsMatrix1 = getNumberRowsAndColumns(matrix1)  # Get rows and columns

    canItBe2nMatrix1 = math.log2(max(rowsMatrix1, columnsMatrix1))  # Use the larger dimension

    if canItBe2nMatrix1.is_integer():
        return matrix1

    # Find the closest power of 2 greater than or equal to the larger dimension
    nextPower = 2 ** math.ceil(math.log2(max(rowsMatrix1, columnsMatrix1)))

    # Create a new matrix with the new size
    newMatrix = [[0 for x in range(nextPower)] for y in range(nextPower)]

    # Copy elements from the original matrix to the new matrix
    for i in range(rowsMatrix1):
        for j in range(columnsMatrix1):  # Iterate over the actual number of columns
            newMatrix[i][j] = matrix1[i][j]

    return newMatrix

def removeZeroRows(matrix):
    # Keep rows that are not all zeros
    matrix = [row for row in matrix if not all(val == 0 for val in row)]
    return matrix

# Function to remove columns that are all zeros
def removeZeroColumns(matrix):
    # Get the number of rows and columns
    num_rows, num_columns = len(matrix), len(matrix[0])
    
    # Keep columns that are not all zeros
    matrix = [[matrix[i][j] for j in range(num_columns) if any(matrix[k][j] != 0 for k in range(num_rows))] for i in range(num_rows)]
    
    return matrix

def printMatrix(matrix):
    for row in matrix:
        print(row)

matrix1 = [
    [1,2,3],
    [1,2,3],
    [1,2,3]
]

matrix2 = [
    [1,2,3],
    [1,2,3],
    [1,2,3]
]

canMultiply(matrix1, matrix2) # Call the function to check if the matrices can be multiplied

if canMultiply: # If this is true, do...
    rowsMatrix1 , columnsMatrix1 = getNumberRowsAndColumns(matrix1) # Call the function to get the number of rows and columns of the matrix number 1
    rowsMatrix2 , columnsMatrix2 = getNumberRowsAndColumns(matrix2) # Call the function to get the number of rows and columns of the matrix number 2

    if (rowsMatrix1 == columnsMatrix1) and rowsMatrix2 == columnsMatrix2: # if they are square matrices, do Strassen's algorithm
        
        canItBe2nMatrix1 = math.log2(rowsMatrix1)
        canItBe2nMatrix2 = math.log2(rowsMatrix2)
        
        matrix1Prime = addCerosUltil2n(matrix1)
        matrix2Prime = addCerosUltil2n(matrix2)
        
        a11 , a12 , a21 , a22 = get2x2Matrix(matrix1Prime)

        b11 , b12 , b21 , b22 = get2x2Matrix(matrix2Prime)

        c = strassenAlgorithm4x4(a11 , a12 , a21 , a22 , b11 , b12 , b21 , b22)

        c = removeZeroColumns(c)
        c = removeZeroRows(c)

        printMatrix(c)
        
else:
    print("This pair of matrices can't be multiplied") # If the matrices can't be multiplied, print this message

