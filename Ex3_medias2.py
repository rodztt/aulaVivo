notas=[]
x=0
v=True
while v:
    nota=float(raw_input('Digite a nota: \n'))
    if nota>0:
        notas.append(nota)
        y=len(notas)
        x+=nota
    else:
        print ('Sua media e: %f')%(x/y)
        break

