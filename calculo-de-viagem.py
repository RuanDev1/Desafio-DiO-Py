valores = input().split()

temp = int(valores[0])
Vl = int(valores[1])

d = (temp*Vl)
litros = (d/12)

print(f'{litros:.3f}')
