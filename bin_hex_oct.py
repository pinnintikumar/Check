number = int(input())
width = len(bin(number)[2:])
for i in range(1, number + 1):
    decimal = f"{i:{width}d} {oct(i)[2:]:>{width}} {hex(i)[2:]:>{width}} {bin(i)[2:]:>{width}}"
    print(decimal)


print("this is karthik")
print("this is new one")