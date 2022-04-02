# multiplexar tres fluxos de dados
from collections import deque

fila1=deque([10,22,37,14,25,48])
fila2= deque([98,32,42,28])
fila3= deque([17,66,22,98])


filaUnida =[]
laco= len(fila1)+len(fila2)+len(fila3)
while len(filaUnida)<laco:

    if len(fila1) != 0:
        temp1=[]
        temp1.append(1)
        temp1.append(fila1.popleft())
        filaUnida.append(temp1)
    if len(fila2) != 0:
        temp2=[]
        temp2.append(2)
        temp2.append(fila2.popleft())
        filaUnida.append(temp2)
    if len(fila3) != 0:
        temp3=[]
        temp3.append(3)
        temp3.append(fila3.popleft())
        filaUnida.append(temp3)


print(filaUnida)
#print(laco)



