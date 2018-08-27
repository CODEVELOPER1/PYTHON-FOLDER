number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

#print(number_grid[2][1]) #[] [] left is coloum right is row

#for row in number_grid: #will print it out in a 2 demention
 #       print(row)
 
for row in number_grid:
    for col in row:
        print(col)
        
        