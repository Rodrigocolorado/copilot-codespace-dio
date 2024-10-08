numb1 = int(input("Insira o primeiro número: "))
numb2 = int(input("Insira o segundo número: "))

operacao = input("Digite qual operação é de sua preferência (+. -, *, /): ")

if operacao == '+':
    print(numb1 + numb2)
elif operacao == '-':
    print(abs(numb1 - numb2))
elif operacao == '*':
    print(numb1 * numb2)
elif operacao == '/':
    print(numb1 / numb2)
else:
    print("Operaçào Inválida!")
    
