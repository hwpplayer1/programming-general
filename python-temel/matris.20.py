a = [[1, 20, 3], [21, 87, 8, 10], [5, 9, 6, 44]]

result = [y for x in a for y in x if y >= 20]
print(result)
