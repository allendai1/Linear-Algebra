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
                string += str(j)
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
        ...


if __name__ == '__main__':
    old = Matrix([[1, 0, 0], [0, 2, 0], [0, 0, 1]])
    new = Matrix([[1, 0, 0], [0, 4, 0], [0, 0, 1]])
    print()
    print(old.transpose())
