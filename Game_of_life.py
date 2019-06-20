import random
from time import sleep

data = []

def create_matrix(num):
    matrix = []
    count_row = 0
    while count_row < num:
        row = []
        count_column = 0
        while count_column < num:
            row.append(random.randrange(0,2))
            count_column += 1
        matrix.append(row)
        count_row += 1
    global data
    data = matrix

def ca():

    global data
    new_matrix = []

    row = 0
    rw_nr = len(data)

    # iterates through rows
    while row < rw_nr:

        this_row = []

        #iterates through cells
        col = 0
        col_nr = len(data[row])

        while col < col_nr:
            # read cell state and initialise counter
            state = data[row][col]
            total = 0

            #cells far from sides
            if 1 <= col <= col_nr-2:
                #check cells on side
                total = data[row][col-1] + data[row][col+1]

                #if on first row
                if row == 0:
                    # row below
                    total += data[row + 1][col - 1]
                    total += data[row + 1][col]
                    total += data[row + 1][col + 1]

                #if on last row
                elif row == rw_nr-1:
                    total += data[row - 1][col - 1]
                    total += data[row - 1][col]
                    total += data[row - 1][col + 1]

                #if on any other row
                else:
                    #row above
                    total += data[row - 1][col - 1]
                    total += data[row - 1][col]
                    total += data[row - 1][col + 1]
                    #row below
                    total += data[row + 1][col - 1]
                    total += data[row + 1][col]
                    total += data[row + 1][col + 1]

            #cells in the first column
            elif col == 0:

                # cell on the right
                total += data[row][col + 1]

                # if on first row
                if row == 0:
                    # row below
                    total += data[row + 1][col]
                    total += data[row + 1][col + 1]

                # if on last row
                elif row == rw_nr - 1:
                    total += data[row - 1][col]
                    total += data[row - 1][col + 1]

                # if on any other row
                else:
                    # row above
                    total += data[row - 1][col]
                    total += data[row - 1][col + 1]
                    # row below
                    total += data[row + 1][col]
                    total += data[row + 1][col + 1]

            #cells in the last colums
            elif col == col_nr-1:

                # cell on the left
                total += data[row][col - 1]

                # if on first row
                if row == 0:
                    # row below
                    total += data[row + 1][col - 1]
                    total += data[row + 1][col]

                # if on last row
                elif row == rw_nr - 1:
                    total += data[row - 1][col - 1]
                    total += data[row - 1][col]

                # if on any other row
                else:
                    # row above
                    total += data[row - 1][col - 1]
                    total += data[row - 1][col]
                    # row below
                    total += data[row + 1][col - 1]
                    total += data[row + 1][col]

            #checks state and total and updates state
            if state == 1:
                if total < 2:
                    this_row.append(0)
                elif total == 2 or total == 3:
                    this_row.append(1)
                elif total > 3:
                    this_row.append(0)
            if state == 0:
                if total ==3:
                    this_row.append(1)
                else:
                    this_row.append(0)
            col += 1
        print_row = ''
        for cell in this_row:
            print_row += str(cell).replace('0','- ').replace('1', '# ')
        print(print_row)

        #adds row to the updated matrix
        new_matrix.append(this_row)
        row += 1
    print('\n - - - - - -  \n')
    data = new_matrix
    sleep(0.2)


def execute(num):
    print('Original matrix\n')
    for row in (data):
        print_row = ''
        for cell in row:
            print_row += str(cell).replace('0','- ').replace('1', '# ')
        print(print_row)
    print('\n - - - - - -  \n')
    sleep(0.5)
    count = 0
    while count < num:
        ca()
        count += 1

create_matrix(30)
execute(400)






















