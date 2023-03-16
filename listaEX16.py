minhaLista = [17,8,10,6,2,4]

trocar = True

while trocar:
    trocar = False
    for i in range(len(minhaLista) - 1):
        if minhaLista[i] > minhaLista[i + 1]:
            trocar = True 
            minhaLista[i], minhaLista[i + 1] = minhaLista[i + 1], minhaLista[i]
            
print(minhaLista)            