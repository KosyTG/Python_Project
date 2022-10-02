number = 11
for i in range(number):
    print("number:", i)

for i in range(number):
    if i == 2:
        continue
    print("number:", i)

for i in range(number):
    if i == 8:
        break
    print("number:", i)
