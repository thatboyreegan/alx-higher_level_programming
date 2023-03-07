#!/usr/bin/python3
for i in range(0, 9):
    lower_bound = (i * 10) + i + 1
    upper_bound = (i + 1) * 10
    for j in range(lower_bound, upper_bound):
        if i == 8:
            print(f"{j:02d}")
        else:
            print(f"{j:02d}, ", end=" ")
