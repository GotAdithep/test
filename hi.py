list = []
number = int(input(f"input "))
if 1 <= number and number <= 10000:
    for i in range(1,number+1):
        list.append(i)

print(f"output {sum(list)}")