def display_sums(i):
    x = 0
    print("i", "\t", "Sum(i)")
    for j in range(1, (i + 1)):
        x += (j / (j + 1))
        print(j, "\t", x)



display_sums(int(input("input integer: ")))
