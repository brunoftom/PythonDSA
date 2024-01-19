import math

def soma(nro1, nro2):
    resultado = nro1 + nro2
    print("%r + %r = " %(nro1,nro2), resultado)

def subtração(nro1, nro2):
    resultado = nro1 - nro2
    print("%r - %r = " %(nro1,nro2), resultado)

def multiplicação(nro1, nro2):
    resultado = nro1 * nro2
    print("%r * %r = " %(nro1,nro2), resultado)

def divisão(nro1, nro2):
    resultado = nro1 / nro2
    print("%r / %r = " %(nro1,nro2), resultado)

def main():
    print("\n******************* Calculadora em Python *******************")
    op = 0
    while op != 5:
        print("\nSelecione a operação:\n")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicaçao")
        print("4. Divisão")
        print("5. Sair")
        op = input("Digite a operação desejada (1/2/3/4/5): ")

        if op == "1":
            print("\n******************* Soma *******************")
            nmo1 = float(input("\nDigite o primeiro numero: "))
            nmo2 = float(input("Digite o segundo numero: "))
            soma(nmo1,nmo2)
        elif op == "2":
            print("\n******************* Subtração *******************")
            nmo1 = float(input("\nDigite o primeiro numero: "))
            nmo2 = float(input("Digite o segundo numero: "))
            subtração(nmo1,nmo2)
        elif op == "3":
            print("\n******************* Multiplicação *******************")
            nmo1 = float(input("\nDigite o primeiro numero: "))
            nmo2 = float(input("Digite o segundo numero: "))
            multiplicação(nmo1,nmo2)
        elif op == "4":
            print("\n******************* Divisão *******************")
            nmo1 = float(input("\nDigite o primeiro numero: "))
            nmo2 = float(input("Digite o segundo numero: "))
            divisão(nmo1,nmo2)
        elif op == "5":
            print("\n******************* Encerrando Calculadora *******************")
            break
        else:
            print("Opção invalida!!!")

if __name__ == "__main__":
    main()