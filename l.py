produtos = {}

# Pedindo os dados ao usuário
for i in range(5):
    nome = input(f"Digite o nome do produto {i + 1}: ")
    preco = float(input(f"Digite o preço do produto '{nome}': R$ "))
    produtos[nome] = preco

# Calculando o valor total da compra
total = 0
for chave in produtos:
    total += produtos[chave]

# Exibindo o resultado
print("\nResumo da compra:")
for chave in produtos:
    print(f"{chave}: R$ {produtos[chave]:.2f}")

print(f"\nValor total da compra: R$ {total:.2f}")