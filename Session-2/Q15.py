matrix = []
m = int(input())

for i in range(m):
    matrix.append(list(map(int, input().split())))

flat = [item for row in matrix for item in row]
print(flat)