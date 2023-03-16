listaDuplicata = [1,2,3,1,4,2,5,6,3,7,8,5,9]

listaSDuplicata = []

while listaDuplicata:
    elemento = listaDuplicata.pop(0) #pop é usado para remover um elemento
    if elemento not in listaSDuplicata:
        listaSDuplicata.append(elemento)
        
print("A lista sem duplicatas é:", listaSDuplicata)        