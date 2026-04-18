matrix=[[0 for _ in range(4)] for _ in range(4) ]
print(matrix)

for r in matrix:
    print(r)


for i in range(4):
    matrix[i][i]=1

print("After putting 1 (identity Matrix):")

for r in matrix:
    print(r)




# 1.For creating a matrix of one row ,here we declared 0 then we use list comprehension. _ is a dummy variable. range(4) ==> 4 times.0==> what we want to print

# matrix=[[0 for _ in range(4)] ]
# print(matrix) ==> [[0, 0, 0, 0]]


# 2.👉 Outer part:
# [[0 for _ in range(4)] for _ in range(4)]
# Outer range(4) → creates 4 rows
# Each time, it runs the inner list → [0, 0, 0, 0]
# ✅ Final Output
# [
#  [0, 0, 0, 0],
#  [0, 0, 0, 0],
#  [0, 0, 0, 0],
#  [0, 0, 0, 0]
# ]

# got a 4 rows × 4 columns matrix

# 3.To print each row in a new line, you have a few clean options 👇

# ✅ Using a loop (best & most common)
# matrix = [[0 for _ in range(4)] for _ in range(4)]

# for row in matrix:
#     print(row)

# 4.For making identity matrix we need to put value 1 where row==column
# thats why we use matrix[i][i]=1






#print matrix row wise/column wise :

m=[[1,2,3,4],
   [5,6,7,8,9]]
s=0
for i in range(len(m[0])):
    row_sum=0
    for j in range(len(m)):
        row_sum+=m[j][i]
    print("sum:",row_sum)

#printing total 

total=0
for row in m:
    total+=sum(row)
print(total)

print(m)