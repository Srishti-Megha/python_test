##### change variable 'l' to any string you want
l = input("Enter your string: ") or "PAYPALISHIRING"
row_len = int(input("Enter number of rows: ") or 4)
check_sum = 0
col_len = 0
while check_sum < len(l):
    if col_len % (row_len-1) == 0:
        check_sum += row_len
    else:
        check_sum += 1       
    col_len += 1     
    
matrix = [[' ' for i in range(col_len)] for j in range(row_len)]
col = 0

index = 0
while col < col_len:
    if col % (row_len-1) == 0:
        for i in range(row_len):
            if index < len(l):
                matrix[i][col]= l[index]       
                index += 1
        # print(col)
        col += 1
    else:
        for i in range(1, row_len -1):
            if index < len(l) and col<col_len:
                matrix[row_len-1-i][col] = l[index]
                index += 1
                col += 1
            else:
                col += 1

print('\n'.join(' '.join(i) for i in matrix))

"""
#complex approach

while col < col_len:
    if col % (row_len-1) == 0:
        for i in range(row_len):
            if (col// (row_len-1)*(2*row_len-2))+i < len(l):
                matrix[i][col]= l[(col// (row_len-1)*(2*row_len-2))+i]       
        # print(col)
        col += 1
        check_sum += row_len
    else:
        num_of_full_column = (col//(row_len-1))+1
        num_of_middle_col = (col//(row_len-1))*(row_len-2)
        last_index_full_column = num_of_full_column*(row_len) + num_of_middle_col -1
        # print(last_index_full_column)
        for i in range(1, row_len -1):
            if last_index_full_column +(col% (row_len-1)) < len(l) and col<col_len:
                matrix[row_len-1-i][col] = l[last_index_full_column+(col% (row_len-1))]
                col += 1
            else:
                col += 1
print('\n'.join(' '.join(i) for i in matrix))
"""
