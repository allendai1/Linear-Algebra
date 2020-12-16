import math


class Vector:
    def __init__(self, *args):  # create list of vector elements
        self.elements = [int(i) for i in args]
        self.length = self.__findLength(self.elements)

    def __findLength(self, elements):
        length = 0.0
        for i in elements:
            length += i * i
        return math.sqrt(length)

    def __getitem__(self, item):  # get element of vector
        return self.elements[item]

    def __add__(self, other):  # adds 2 vectors together
        if len(self.elements) != len(other.elements):
            raise Exception("Number of vector elements invalid")
        new_vector = []
        for i in range(len(self.elements)):
            new_vector.append(self.elements[i] + other.elements[i])
        return Vector(*new_vector)

    def __sub__(self, other):
        if len(self.elements) != len(other.elements):
            raise Exception("Number of vector elements invalid")
        new_vector = []
        for i in range(len(self.elements)):
            new_vector.append(self.elements[i] - other.elements[i])
        return Vector(*new_vector)

    def __mul__(self, other):  # dot product of 2 vectors
        if type(self) == type(other):
            if len(self.elements) != len(other.elements):
                raise Exception("Number of vector elements invalid")
            total = 0
            for i in range(len(self.elements)):
                total += self.elements[i] * other.elements[i]
            return total
        else:
            new_vector = []
            for i in range(len(self.elements)):
                new_vector.append(other * self.elements[i])
            return Vector(*new_vector)

    def __rmul__(self, other):  # dot product of 2 vectors
        if type(self) == type(other):
            if len(self.elements) != len(other.elements):
                raise Exception("Number of vector elements invalid")
            total = 0
            for i in range(len(self.elements)):
                total += self.elements[i] * other.elements[i]
            return total
        else:
            new_vector = []
            for i in range(len(self.elements)):
                new_vector.append(other * self.elements[i])
            return Vector(*new_vector)

    def length(self):
        total = 0.0
        for i in self.elements:
            total += i * i
        return float(math.sqrt(total))

    def __str__(self):
        return str(self.elements)


if __name__ == '__main__':
    x = Vector(1, 1, 1, 4)
    y = Vector(1, 1, 1, 5)
    z = Vector(45, 45, 45, 1)
