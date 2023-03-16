minhaLista = []

trocar = True
num = int(input("Quantos elementos deseja? "))

for i in range(num):
    val = float(input("Entre com um número: "))
    minhaLista.append(val)
    
while trocar:
    trocar = False
    for i in range(len(minhaLista) - 1):
        if minhaLista[i] > minhaLista[i + 1]:
            trocar = True
            minhaLista[i], minhaLista[i + 1] = minhaLista[i + 1], minhaLista[i]
        
        
print("\nOrdenado:")
print(minhaLista)