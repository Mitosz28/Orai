magassag = int(input("Add meg a karácsonyfa magasságát: "))

for i in range(1, magassag + 1):
    # szóközök száma
    print(" " * (magassag - i) + "*" * (2 * i - 1))
