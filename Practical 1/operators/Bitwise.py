a=5
b=6
print(f"Bitwise AND: {a & b}")
#a = 0110 if both has 1 in same position,we take 1,else 0
#b = 0011
#& = 0010

print(f"Bitwise OR: {a | b}") #if either has 1 ,we take as 1
print(f"Bitwise XOR: {a ^ b}")#if they are diff. we take 1
print(f"Left Shift: {a << 1}, Right Shift: {a>>1}")#posion shift by one. 0110 becomes 1100
print(f"Negation: {-a}") #flips the sign(negaiton plus - makes it same)
print(f"Bitwise NOT: {~a}") #flips all the bits plus 1
