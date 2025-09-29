import math


def ler_numero(mensagem: str) -> float:
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def soma(a: float, b: float) -> float:
    return a + b


def subtracao(a: float, b: float) -> float:
    return a - b


def multiplicacao(a: float, b: float) -> float:
    return a * b


def divisao(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida")
    return a / b


def divisao_inteira(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida")
    return a // b


def resto(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida")
    return a % b


def potencia(a: float, b: float) -> float:
    return a ** b


def raiz(a: float, n: float = 2.0) -> float:
    if n == 0:
        raise ZeroDivisionError("Índice da raiz não pode ser zero")
    if a < 0 and n % 2 == 0:
        raise ValueError("Raiz de índice par de número negativo não é real")
    return math.copysign(abs(a) ** (1.0 / n), 1 if a >= 0 else -1) if n % 2 != 0 else abs(a) ** (1.0 / n)


def inverso(a: float) -> float:
    if a == 0:
        raise ZeroDivisionError("Inverso de zero não existe")
    return 1.0 / a


def absoluto(a: float) -> float:
    return abs(a)


def negacao(a: float) -> float:
    return -a


def porcentagem(parte: float, total: float) -> float:
    return (parte / 100.0) * total


def imprimir_menu(valor_atual: float | None) -> None:
    print("\n=== Calculadora ===")
    if valor_atual is None:
        print("Acumulador: vazio")
    else:
        print(f"Acumulador: {valor_atual}")
    print("1) Soma (a + b)")
    print("2) Subtração (a - b)")
    print("3) Multiplicação (a * b)")
    print("4) Divisão (a / b)")
    print("5) Potência (a ^ b)")
    print("6) Resto (a % b)")
    print("7) Divisão inteira (a // b)")
    print("8) Raiz n-ésima (raiz(a, n))")
    print("9) Inverso (1 / a)")
    print("10) Absoluto (|a|)")
    print("11) Negação (-a)")
    print("12) Porcentagem (x % de y)")
    print("13) Limpar acumulador")
    print("0) Sair")


def executar():
    valor_atual: float | None = None
    while True:
        imprimir_menu(valor_atual)
        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == "0":
                print("Até mais!")
                break
            elif opcao == "1":
                if valor_atual is None:
                    a = ler_numero("a: ")
                else:
                    a = valor_atual
                    print(f"a (do acumulador): {a}")
                b = ler_numero("b: ")
                valor_atual = soma(a, b)
                print("Resultado:", valor_atual)
            elif opcao == "2":
                if valor_atual is None:
                    a = ler_numero("a: ")
                else:
                    a = valor_atual
                    print(f"a (do acumulador): {a}")
                b = ler_numero("b: ")
                valor_atual = subtracao(a, b)
                print("Resultado:", valor_atual)
            elif opcao == "3":
                if valor_atual is None:
                    a = ler_numero("a: ")
                else:
                    a = valor_atual
                    print(f"a (do acumulador): {a}")
                b = ler_numero("b: ")
                valor_atual = multiplicacao(a, b)
                print("Resultado:", valor_atual)
            elif opcao == "4":
                if valor_atual is None:
                    a = ler_numero("a: ")
                else:
                    a = valor_atual
                    print(f"a (do acumulador): {a}")
                b = ler_numero("b: ")
                valor_atual = divisao(a, b)
                print("Resultado:", valor_atual)
            elif opcao == "5":
                if valor_atual is None:
                    a = ler_numero("base a: ")
                else:
                    a = valor_atual
                    print(f"base a (do acumulador): {a}")
                b = ler_numero("expoente b: ")
                valor_atual = potencia(a, b)
                print("Resultado:", valor_atual)
            elif opcao == "6":
                if valor_atual is None:
                    a = ler_numero("a: ")
                else:
                    a = valor_atual
                    print(f"a (do acumulador): {a}")
                b = ler_numero("b: ")
                valor_atual = resto(a, b)
                print("Resultado:", valor_atual)
            elif opcao == "7":
                if valor_atual is None:
                    a = ler_numero("a: ")
                else:
                    a = valor_atual
                    print(f"a (do acumulador): {a}")
                b = ler_numero("b: ")
                valor_atual = divisao_inteira(a, b)
                print("Resultado:", valor_atual)
            elif opcao == "8":
                if valor_atual is None:
                    a = ler_numero("a: ")
                else:
                    a = valor_atual
                    print(f"a (do acumulador): {a}")
                n = ler_numero("índice n (ex: 2 para raiz quadrada): ")
                valor_atual = raiz(a, n)
                print("Resultado:", valor_atual)
            elif opcao == "9":
                if valor_atual is None:
                    a = ler_numero("a: ")
                else:
                    a = valor_atual
                    print(f"a (do acumulador): {a}")
                valor_atual = inverso(a)
                print("Resultado:", valor_atual)
            elif opcao == "10":
                if valor_atual is None:
                    a = ler_numero("a: ")
                else:
                    a = valor_atual
                    print(f"a (do acumulador): {a}")
                valor_atual = absoluto(a)
                print("Resultado:", valor_atual)
            elif opcao == "11":
                if valor_atual is None:
                    a = ler_numero("a: ")
                else:
                    a = valor_atual
                    print(f"a (do acumulador): {a}")
                valor_atual = negacao(a)
                print("Resultado:", valor_atual)
            elif opcao == "12":
                if valor_atual is None:
                    x = ler_numero("x (%): ")
                else:
                    x = valor_atual
                    print(f"x (% do acumulador): {x}")
                y = ler_numero("de y: ")
                valor_atual = porcentagem(x, y)
                print("Resultado:", valor_atual)
            elif opcao == "13":
                valor_atual = None
                print("Acumulador limpo.")
            else:
                print("Opção inválida. Tente novamente.")
        except ZeroDivisionError as e:
            print("Erro:", e)
        except ValueError as e:
            print("Erro:", e)


if __name__ == "__main__":
    executar()


