def triangle(n):

    k = 1
    for i in range(0, 4):
        for j in range(0, k):
            print("* ", end=" ")
        k = k + 2
        print("\r")
    k = 5
    for i in range(0, 5):
        for j in range(0, k):
            print("* ", end=" ")
        k = k - 2
        print("\r")

n = 5
triangle(n)