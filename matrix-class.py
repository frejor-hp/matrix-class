class Matrix(object):
    def __init__(self, matrix_):
        self.matrix = matrix_

    def __repr__(self):
        return str(self.matrix)

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if self.matrix == other.matrix:
                return True
            return False
        return self.matrix == other

    def __ne__(self, other):
        if isinstance(other, Matrix):
            if self.matrix != other.matrix:
                return True
            return False
        return self.matrix != other

    def __pos__(self):
        return self

    def __neg__(self):
        return self * -1

    def __call__(self, *args):
        matrix_ = self.matrix
        for i in args:
            matrix_ = matrix_[i]

        return matrix_

    def __getitem__(self, item):
        return self.matrix[item]

    def __len__(self):
        return len(self.matrix)

    def __add__(self, other):

        add_ = [[p1 + p2 for p1, p2 in zip(self.matrix[i], other[i])]
                for i in range(len(other))]
        return Matrix(add_)

        # return Matrix(
        #             self.add_matrix(self(), other()))

    def __sub__(self, other):

        sub_ = [[p1 - p2 for p1, p2 in zip(self.matrix[i], other[i])]
                for i in range(len(other))]
        return Matrix(sub_)

        # return Matrix(
        #     self.sub_matrix(self(), other()))

    def __mul__(self, other):
        if isinstance(other, Matrix):
            mul_ = [[0] * len(other.matrix[i]) for i in range(len(self.matrix))]

            if len(self.matrix[0]) != len(other.matrix):
                raise Exception('length of matrix A line different than length of matrix B column')

            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[i])):
                    for k in range(len(self.matrix[i])):
                        mul_[i][j] += self.matrix[i][k] * other.matrix[k][j]

            # return Matrix(
            #     self.mul_matrix(self(), other()))

        else:
            mul_ = [[p * other for p in self.matrix[i]]
                    for i in range(len(self.matrix))]

            # return Matrix(
            #     self.mul_matrix(self(), other))

        return Matrix(mul_)

    def __div__(self, other):
        if isinstance(other, Matrix):
            div_ = [[]]
            print 'Division between matrix not implemented yet'
        else:
            div_ = [[p / other for p in self.matrix[i]]
                    for i in range(len(self.matrix))]

        return Matrix(div_)

    def __rmul__(self, other):
        return self * other

    def __int__(self):
        int_ = [[int(p) for p in self.matrix[i]]
                for i in range(len(self.matrix))]

        return Matrix(int_)

    def __float__(self):
        return self * 1.

    def __str__(self):
        str_ = ''

        for i in range(len(self.matrix)):
            str_ += str(self.matrix[i])
            str_ += '\n'

        return str_[:-1]

    @classmethod
    def add_matrix(cls, m1, m2):
        sum_ = []

        if len(m1) != len(m2):
            raise Exception('Lists with different length')

        for i in range(len(m1)):
            if type(m1[i]) is list:
                sum_.append(cls.add_matrix(m1[i], m2[i]))
            else:
                sum_.append(m1[i] + m2[i])

        return sum_

    @classmethod
    def sub_matrix(cls, m1, m2):
        sub_ = []

        if len(m1) != len(m2):
            raise Exception('Lists with different length')

        for i in range(len(m1)):
            if type(m1[i]) is list:
                sub_.append(cls.sub_matrix(m1[i], m2[i]))
            else:
                sub_.append(m1[i] - m2[i])

        return sub_

    @classmethod
    def mul_matrix(cls, m1, m2):
        mul = []
        if type(m2) is list:
            pass
        else:
            for i in range(len(m1)):
                if type(m1[i]) is list:
                    mul.append(cls.mul_matrix(m1[i], m2))
                else:
                    mul.append(m1[i] * m2)

        return mul


matrix = Matrix([[1, 2],
                 [3, 4]])

matrix2 = Matrix([[-1, 3],
                  [ 4, 2]])

print matrix
print -matrix
print matrix + matrix2
print matrix * 2
print matrix * matrix2
print matrix / 2
