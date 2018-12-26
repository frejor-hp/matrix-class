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

    def __sub__(self, other):

        sub_ = [[p1 - p2 for p1, p2 in zip(self.matrix[i], other[i])]
                for i in range(len(other))]

        return Matrix(sub_)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            mul_ = [[0] * len(other.matrix[i]) for i in range(len(self.matrix))]

            if len(self.matrix[0]) != len(other.matrix):
                raise Exception('length of matrix A line different than length of matrix B column')

            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[i])):
                    for k in range(len(self.matrix[i])):
                        mul_[i][j] += self.matrix[i][k] * other.matrix[k][j]
        else:
            mul_ = [[p * other for p in self.matrix[i]]
                    for i in range(len(self.matrix))]

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
        max_column = [0] * len(self.matrix[0])

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                size = len(str(self.matrix[i][j]))
                if size > max_column[j]:
                    max_column[j] = size  # pego o numero com maior numero de caracteres na coluna

        for i in range(len(self.matrix)):
            line = ''
            for j in range(len(self.matrix[i])):
                size = max_column[j] - len(str(self.matrix[i][j]))
                line += ' ' * (size+1)  # coloco um espaco a mais para que nao fique junta da ','
                line += str(self.matrix[i][j])
                line += ','
            str_ += '[' + line[1:-1] + ']\n'  # tiro o primeiro espaco para que fique alinhado com o '[' e a ultima ','

        return str_[:-1]  # tiro o ultimo '\n'


print matrix
print -matrix
print matrix + matrix2
print matrix * 2
print matrix * matrix2
print matrix / 2
