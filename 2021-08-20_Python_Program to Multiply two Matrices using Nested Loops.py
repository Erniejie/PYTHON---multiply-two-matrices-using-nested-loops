#Program to multiply two matrices using nested loops
"Computer Programmming Tutor, 17th August 2021"

#3x3 Matrix

A = [[5,3,2],
     [2,3,4],
     [3,4,3]
    ]

#3x4 Matrix
B = [[2,4,1,2],
     [3,2,3,0],
     [3,2,5,1]
    ]
# Result is a 3x4 Matrix
result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]
    ]

#Iterate Through Rows of A

for p in range(len(A)):
    # Iterate Through Columns of B
    for t in range(len(B[0])):
        #Iterate Through Rows of B
        for h in range(len(B)):
            result[p][t] +=A[p][h]*B[h][t]

for r in result:
    print(r)
    
