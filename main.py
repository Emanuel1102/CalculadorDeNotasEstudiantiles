cantidad_notas = 3

notas=[]

for i in range(cantidad_notas):
    nota=float(input(f'Nota #{i+1} => '))
    notas.append(nota)

promedio=sum(notas)/len(notas)

print(f'Promedio: {promedio:.1f}')