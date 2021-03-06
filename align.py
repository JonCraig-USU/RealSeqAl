import numpy as np
from showtime import showTime

continueScore = -1
openScore = -5

def align(n, m):
  if n == 0 and m == 0:
    return 0
  if n == 0:
    return openScore + continueDeleteB(0, m-1)
  if m == 0:
    return openScore + continueDeleteA(n-1, 0)
  return max(openScore + continueDeleteB(n, m-1),
             openScore + continueDeleteA(n-1, m),
             scores[A[n], B[m]] + align(n-1, m-1))

def continueDeleteA(n, m):
  if n == 0:
    return align(n, m)
  return max(continueScore + continueDeleteA(n-1, m), align(n, m))

def continueDeleteB(n, m):
  if m == 0:
    return align(n, m)
  return max(continueScore + continueDeleteB(n, m-1), align(n, m))


# Score table/ dictionary
scores = {  ("A", "A"): 1, ("A", "T"): -5, ("A", "C"): -5, ("A", "G"): -1,
            ("T", "A"): -5, ("T", "T"): 1, ("T", "C"): -1, ("T", "G"): -5,
            ("C", "A"): -5, ("C", "T"): -1, ("C", "C"): 1, ("C", "G"): -5,
            ("G", "A"): -1, ("G", "T"): -5, ("G", "C"): -5, ("G", "G"): 1
         }

# Dynamic Program
def alignDP(n, m):
    sol = np.zeros(shape = (3, n+1, m+1), dtype=np.int32)

    sol[0, 0, 0] = 0  # set the 0 postion on align array
    sol[1, 0, 0] = 0  # set the 0 postion on contA array
    sol[2, 0, 0] = 0  # set the 0 postion on contB array

    for i in range (1, n+1):
            sol[1, i, 0] = continueScore + sol[1, i-1, 0]  # continueA
            sol[0, i, 0] = openScore + sol[1, i-1, 0]      # open then continueA

    for j in range (1, m+1):
        sol[2, 0, j] = continueScore + sol[2, 0, j-1] # continueB
        sol[0, 0, j] = openScore + sol[2, 0, j-1]     # open then continueB


    for x in range (1, n+1):
        for y in range (1, m+1):
            # set swap value
            sol[0, x, y] = max(
                sol[0, x-1, y-1] + scores[(A[x], B[y])],
                sol[1, x-1, y] + openScore,
                sol[2, x, y-1] + openScore
            )
            # set delA
            sol[1, x, y] = max(
                sol[1, x-1, y] + continueScore,
                sol[0, x, y]
            )
            # set delB
            sol[2, x, y] = max(
                sol[2, x, y-1] + continueScore,
                sol[0, x, y]
            )
    # print(sol)   # only for testing small batches
    return sol[0, n, m]


'''TEST CASES'''
# # Case 1
# A = "_"
# B = "_"
# print("Case 1: " + str(alignDP(len(A)-1, len(B)-1)))
# print(align(len(A)-1, len(B)-1))

# # Case
# A = "_ATCG"
# B = "_"
# print("Case 2: " + str(alignDP(len(A)-1, len(B)-1)))
# print(align(len(A)-1, len(B)-1))

# # Case
# A = "_ATCG"
# B = "_ATCG"
# print("Case 3: " + str(alignDP(len(A)-1, len(B)-1)))
# print(align(len(A)-1, len(B)-1))

# # Case
# A = "_A"
# B = "_T"
# print("Case 4: " + str(alignDP(len(A)-1, len(B)-1)))
# print(align(len(A)-1, len(B)-1))

# # Case
# A = "_A"
# B = "_G"
# print("Case 5: " + str(alignDP(len(A)-1, len(B)-1)))
# print(align(len(A)-1, len(B)-1))

# # Case 6
# A = "_AAA"
# B = "_TTT"
# print("Case 6: " + str(alignDP(len(A)-1, len(B)-1)))
# print(align(len(A)-1, len(B)-1))
'''END TEST CASES'''

# Read in given file
# done 2 by 2 for time sake
valid = {'A','T','C','G'}
A = ""
for line in open("dna/dna1.txt", 'r').readlines():
    for char in line.strip():
        if char in valid:
            A += char
B = ""
for line in open("dna/dna1.txt", 'r').readlines():
    for char in line.strip():
        if char in valid:
            B += char


def alignGraph(n):
  alignDP(n, n)

sizes = [2**8, 2**9, 2**10, 2**11, 2**12]

showTime(alignGraph, sizes)


