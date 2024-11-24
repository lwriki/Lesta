def v1(number):
    return (number & 1) == 0

def v2(number):
    return number - (number // 2) * 2 == 0

def v3(number):
    if number == 0:
        return True
    if number == 1:
        return False
    return v2(number - 2)

variable = [v1,v2,v3]
num = int(input("Введите целое число: "))
for i in variable:
    if (i)(num):
        print(f"{num} - четное число.")
    else:
        print(f"{num} - нечетное число.")
