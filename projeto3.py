while True:
    print("CALCULADORA SIMPLES")
    print('-=-=-=-=-=-=-=-=-=-=-=-=-')
    print("[1] Somar")
    print("[2] Subtrair")
    print("[3] Multiplicar")
    print("[4] Dividir")
    print('-=-=-=-=-=-=-=-=-=-=-=-=-')
    op = int(input("Escolha -> "))
    print('=-=-=-=-')
    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))
    print('-=-=-=-=-=-=')
    if op == 1:
        print("Resultado:", n1 + n2)
    elif op == 2:
        print("Resultado:", n1 - n2)
    elif op == 3:
        print("Resultado:", n1 * n2)
    elif op == 4:
        if n2 == 0:
            print("Não dá pra dividir por zero!")
        else:
            print("Resultado:", n1 / n2)
    else:
        print("Opção inválida!")

    continuar = input("Quer continuar? [S/N] -> ").upper()

    if continuar != "S":  # se NÃO for S, sai
        print("Encerrando...")
        break

    print()  # só pra dar uma espaçada
