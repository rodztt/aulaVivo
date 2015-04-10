notas=[]
x=0
def maior_nota(lst):
    lst.sort()
    z= lst[len(lst)-1]
    print ("A maior nota e: %f")%(z)
print("---MEDIA---")
print("Digite quantas notas quiser, quando desejar obter a media \n digite um numero negativo \n")
while x>=0:
    while True:
        try:
            nota=float(raw_input('Digite a nota: \n'))
            break
        except:
            print "voce nao digitou um numero valido, digite somente numeros \n"
    if nota>0:
        notas.append(nota)
        y=len(notas)
        x+=nota
    else:
        print ('Sua media e: %f')%(x/y)
        maior_nota(notas)
        break
