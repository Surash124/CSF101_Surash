count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
    print("loop ended")

for num in rangee(1,6):
    for num in range(1,6):
        if num % 2 == 0:
            continue
        print(num)
        
