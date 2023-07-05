print("Bem Vindo")
opç = "s"

while opç == "s":
    
    num1 = int(input("Digite um número: "))

    if num1 % 2 == 0:
        print("\nO numero que digitou é par.")

    else:
        print("\nO numero que voce digitou é impar.")

    opç = str(input("\nAperte [s] para continuar, ou qualquer outra tecla para sair. \n"))

print("Programa encerrado.")
