import collections

grid = [[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]

counter = 0
rows = []
columns = []
for i in range(len(grid)):
    rows.append(grid[i][:])
    columns.append([x[i] for x in grid])
print(rows, columns)

print([item for item in collections.Counter(columns).items()])

for row in rows:
    if row in columns:
        counter+=1
