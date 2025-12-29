lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

filtered_elements = [elem for elem in lst if elem < 30 and elem % 3 == 0]

print(filtered_elements)