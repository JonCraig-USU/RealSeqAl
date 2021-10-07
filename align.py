
# open a gap score = openScore
# continue gap score = continueScore
# substitue score dictionary S

import numpy as np

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
             S[A[n], B[m]] + align(n-1, m-1))

def continueDeleteA(n, m):
  if n == 0:
    return align(n, m)
  return max(continueScore + continueDeleteA(n-1, m), align(n, m))

def continueDeleteB(n, m):
  if m == 0:
    return align(n, m)
  return max(continueScore + continueDeleteB(n-1, m), align(n, m))

scores = {  ("A", "A"): 1, ("A", "T"): -5, ("A", "C"): -5, ("A", "G"): -1,
            ("T", "A"): -5, ("T", "T"): 1, ("T", "C"): -1, ("T", "G"): -5,
            ("C", "A"): -5, ("C", "T"): -1, ("C", "C"): 1, ("C", "G"): -5,
            ("G", "A"): -1, ("G", "T"): -5, ("G", "C"): -5, ("G", "G"): 1
         }

def alignDP(n, m):
    sol = np.zeros(shape = (3, n+1, m+1))

    sol[0, 0, 0] = 0  # set the 0 postion on all arrays
    sol[1, 0, 0] = 0  # set the 0 postion on all arrays
    sol[2, 0, 0] = 0  # set the 0 postion on all arrays

    for i in range (1, m+1):
        sol[0, 0, i] = -4 - i # set the base for swap array
        sol[1, 0, i] = -4 - i # set the base for delA array

    for j in range (1, n+1):
            sol[0, j, 0] = -4 - j # set the base for swap array
            sol[2, j, 0] = -4 - j # set the base for delB array

    for x in range (1, n+1):
        for y in range (1, m+1):
            # set swap value
            sol[0, x, y] = max(
                sol[0, x-1, y-1] + scores((A[x], B[y])),
                sol[1, x-1, y],
                sol[2, x, y-1]
            )

            # set delA
            sol[1, x, y] = max(
                sol[1, x-1, y] + continueScore,
                sol[0, x, y] + openScore
            )

            # set delB
            sol[2, x, y] = max(
                sol[2, x, y-1] + continueScore,
                sol[0, x, y] + openScore
            )

A = "ATTCGTT"
B = "ATCCGGA"

print(alignDP(len(A), len(B)))

# if __name__ == "__main__":
#     alignDP()
            


    
