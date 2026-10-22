num = int(input("Enter a whole number grater than 0: "))
if num == 0:
    print("Please enter a whole number grater than 0!")
    exit()

sum = 0;
while num > 0:
    lastTerm = num % 10
    sum += lastTerm
    num = num // 10

print(f"The sum of digits are: {sum}")


