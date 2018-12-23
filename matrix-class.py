class Matrix(object):
    def __init__(self, matrix_):
        self.matrix = matrix_

    def __repr__(self):
        return str(self.matrix)

    def __str__(self):
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
        return Matrix(
                    self.add_matrix(self(), other()))

    def __sub__(self, other):
        return Matrix(
                    self.sub_matrix(self(), other()))

    def __mul__(self, other):
        if isinstance(other, Matrix):
            return Matrix(
                        self.mul_matrix(self(), other()))
        else:
            return Matrix(
                        self.mul_matrix(self(), other))

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

        # sum_ = [[l1 + l2 for l1, l2 in zip(self.matrix[i], other[i])]
        #         for i in range(len(other))]
        # return Matrix(sum_)

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
