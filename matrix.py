import numpy as np
import sympy as mp

# arr: [[1,2,3,],[4,5,6],[7,8,9]] =>  [[1,2,3,],
#                                       [4,5,6],
#                                       [7,8,9]]
class Matrix(object):
    def __init__(self, A):

        self.A = A
        if not self.isMatrix():
            raise Exception("Not a valid matrix")
        self.rows = len(A)
        self.columns = len(A[0])

    def isMatrix(self):
        x = len(self.A[0])
        for i in self.A:
            if len(i) != x:
                return False
        else:
            return True

    def __str__(self):
        string = ""
        for i in range(len(self.A)):
            for j in self.A[i]:
                string += str(j) + " "
            string += '\n'
        return string

    def __eq__(self, other):
        if self.A == other.A:
            return True
        else:
            return False

    def transpose(self):
        new_matrix = [[0 for _ in range(self.rows)] for _ in range(self.columns)]
        for i in range(len(self.A)):
            for j in range(len(self.A[0])):
                new_matrix[j][i] = self.A[i][j]
        return Matrix(new_matrix)

    def isSymmetric(self):
        if self.transpose().A == self.A:
            return True
        else:
            return False

    def isIdentity(self):
        if not self.isSquare():
            return False
        for i in range(len(self.A)):
            for j in range(len(self.A[0])):
                if self.A[i][j] != 0 and i != j:
                    return False
                if i != j:
                    continue
                elif i == j and self.A[i][j] != 1:
                    return False
        return True

    def isDiagonal(self):
        for i in range(len(self.A)):
            for j in range(len(self.A[0])):
                if self.A[i][j] != 0 and i != j:
                    return False
                elif self.A[i][j] == 0 and i == j:
                    return False
        return True

    def isSquare(self):
        return True if self.rows == self.columns else False

    def __add__(self, other):
        arr1 = []
        arr2 = []
        if not self.isSquare():
            raise Exception("Both matrices must be nxn size to add")
        for i in range(len(self.A)):
            for j in range(len(self.A[0])):
                arr2.append(self.A[i][j] + other.A[i][j])
            arr1.append(arr2)
            arr2 = []
        return Matrix(arr1)

    def __sub__(self, other):
        arr1 = []
        arr2 = []
        if not self.isSquare():
            raise Exception("Both matrices must be nxn size to add")
        for i in range(len(self.A)):
            for j in range(len(self.A[0])):
                arr2.append(self.A[i][j] - other.A[i][j])
            arr1.append(arr2)
            arr2 = []
        return Matrix(arr1)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Matrix([[j * other for j in i] for i in self.A])
        elif type(other) == Matrix:
            if self.columns != other.rows:
                raise Exception("Number of columns in matrix1 must be equal to number of rows in matrix2")
            elif self.isSquare():
                arr = [[0 for i in range(self.columns)] for j in range(self.rows)]
                for i in range(self.rows):
                    for j in range(self.columns):
                        for k in range(self.columns):
                            arr[i][j] += self.A[i][k] * other.A[k][j]
                return Matrix(arr)
            else:
                arr = [[0 for i in range(other.columns)] for j in range(self.rows)]
                for i in range(self.rows):
                    for j in range(other.columns):
                        arr[i][j] = 0
                        for x in range(self.columns):
                            arr[i][j] += (self.A[i][x] * other.A[x][j])
                return Matrix(arr)

    def __rmul__(self, other):
        if type(other) == int or type(other) == float:
            return Matrix([[j * other for j in i] for i in self.A])
        elif type(other) == Matrix:
            if self.columns != other.rows:
                raise Exception("Number of columns in matrix1 must be equal to number of rows in matrix2")
            elif self.isSquare():
                arr = [[0 for i in range(self.columns)] for j in range(self.rows)]
                for i in range(self.rows):
                    for j in range(self.columns):
                        for k in range(self.columns):
                            arr[i][j] += self.A[i][k] * other.A[k][j]
                return Matrix(arr)
            else:
                arr = [[0 for i in range(other.columns)] for j in range(self.rows)]
                for i in range(self.rows):
                    for j in range(other.columns):
                        arr[i][j] = 0
                        for x in range(self.columns):
                            arr[i][j] += (self.A[i][x] * other.A[x][j])
                return Matrix(arr)

    def isOrthogonal(self):
        if self.__mul__(self.transpose()).isIdentity():
            return True
        else:
            return False

    def isInvertible(self):
        if not self.isSquare():
            return False

    def determinant(self):
        a = np.array(self.A)
        return np.linalg.det(a)

    def inverse(self):
        a = np.array(self.A)
        return Matrix(np.linalg.inv(a))

    def eigenvalue(self):
        a = np.array(self.A)
        w, _ = np.linalg.eig(a)

        return Matrix([w])

    def eigenvector(self):
        a = np.array(self.A)
        _, v = np.linalg.eig(a)
        return Matrix(v)

    def rank(self):
        a = np.array(self.A)
        return np.linalg.matrix_rank(a)

    # def similar(self, other):
    #
    #     a = [i for i in self.eigenvalue().A[0]]
    #     b = [i for i in other.eigenvalue().A[0]]
    #
    #     # print(a)
    #     if sorted(a)==sorted(b):
    #         return True
    #     else:
    #         return False


if __name__ == '__main__':
    a = Matrix([[13,-8,-4], [12,7,4],[24,16,7]])
    new = Matrix([[0,0,1], [0,1,0],[1,0,0]])
    b = Matrix([[-1,0,0], [0,3,0], [0,0,-1]])
    # print(new * old)

