import numpy as np

scoreTable = [  [1, -5, -5, -1]
                [-5, 1, -1, -5]
                [-5, -1, 1 -5]
                [-1, -5, -5, 1]]

isGapOpen = False #boolean for gap

def med(n, m):
    sol = np.zeros(n, m)
    score = 0
# set up the bases of the solution array
    for k in range (n+1):
        [k, 0] = - 4 - k
    for l in range (m+1):
        [0, l] = -4 - l

# begin looping through sol filling in the blanks
    for i in range (n+1):
        for j in range(m+1):
            sol[i, j] max(
                    sol[i-1, j] +1,
                    sol[i, j-1] +1,
                    sol[i-1, j-1] +1
                )



            # if n == 0:
            #     return m
            # elif m == 0:
            #     return n
            # else:
            #     return max(med(i-1, j) +1
            #         )

