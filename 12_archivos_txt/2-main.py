with open("stock.txt", "w") as pedropapel:
    pedropapel.write(input(">Razon para modificar stock: "))

with open("stock.txt", "r") as pedropapel:
    abrir = pedropapel.read()

print(abrir)