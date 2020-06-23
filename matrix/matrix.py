class Matrix:
    def __init__(self, matrix_string):
        self.rows = len(matrix_string.split('\n'))
        self.cols = len(matrix_string.split('\n')[0].split())
        self.string = matrix_string
        print('This matrix has %d rows and %d columns' % (self.rows, self.cols))

    def row(self, index):
        row_output = []
        for loop_i in range(self.cols):
            row_output.append(int(self.string.split('\n')[index-1].split()[loop_i]))
        return(row_output)

    def column(self, index):
        col_output = []
        for loop_j in range(self.rows):
            col_output.append(int(self.string.split('\n')[loop_j].split()[index-1]))
        return(col_output)
