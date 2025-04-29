numero1 = float(input("Digite o primeiro valor: "))
operacao = input("Escolha a operação: +, -, x, / ")
numero2 = float(input("Digite o segundo valor: "))

if operacao == "+":
    print(numero1 + numero2)
elif operacao == "-":
    print(numero1 - numero2)
elif operacao == "x":
    print(numero1 * numero2)
elif operacao == "/":
    if numero2 != 0:
        print(numero1 / numero2)
    else:
        print("Erro: divisão por zero.")
else:
    print("Operação inválida.")