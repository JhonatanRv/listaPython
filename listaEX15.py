banda = []

print("Etapa 1:", banda)

banda.append("John Lennon")
banda.append("Paul McCartney")
banda.append("George Marrison")
print("Etapa 2:", banda)

for members in range(2):
    banda.append(input("Novo membro: "))
print("Etapa 3:", banda)

del banda[-1]
del banda[-1]
print("Etapa 4:", banda)

banda.insert(0, "RingoStarr")
print("Etapa5:", banda)
print("The fab", len(banda))

