print("=" * 30)
print("{:^30}".format("BANCO CEV"))
print("=" * 30)
n = int(input("Qual o valor que gostaria de saca? R$"))
ced = 50
total_ced = 0
while True:
    if n >= ced:
        n -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print("Total de {} cedulas de R${}".format(total_ced, ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if n == 0:
            break
print("FIM")