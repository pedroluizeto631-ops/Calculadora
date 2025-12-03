RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

while True:
    print(CYAN + "=== CALCULADORA COLORIDA v1.2 ===" + RESET)
    print("[1] Somar")
    print("[2] Subtrair")
    print("[3] Multiplicar")
    print("[4] Dividir")
    print("[5] Sair")
    op = input("Escolha -> ")

    if op == "5":
        print(YELLOW + "Encerrando..." + RESET)
        break

    n1 = float(input("Número 1: "))
    n2 = float(input("Número 2: "))

    print(GREEN + "Resultado: ", end="")

    if op == "1":
        print(n1 + n2)
    elif op == "2":
        print(n1 - n2)
    elif op == "3":
        print(n1 * n2)
    elif op == "4":
        if n2 == 0:
            print(RED + "Erro: divisão por zero!" + RESET)
        else:
            print(n1 / n2)
    else:
        print(RED + "Opção inválida!" + RESET)

    print(RESET)
    continuar = input("Continuar? [S/N] -> ").strip().upper()
    if continuar != "S":
        break

    print()

