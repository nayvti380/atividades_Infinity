import random

def lancar_dados():
    lados = [1, 2, 3, 4, 5, 6]
    dado1 = random.choice(lados)
    dado2 = random.choice(lados)
    total = dado1 + dado2
    return total

resultado = lancar_dados()
print(f"Resultado do lançamento dos dados: {resultado}")
