class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.matrix = []
        for row in self.matrix_string.split("\n"):
            sub_string = list(map(int, row.split(" ")))
            self.matrix.append(sub_string)

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        result = []
        for row in self.matrix:
            result.append(row[index-1])
        return result
