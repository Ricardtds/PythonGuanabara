# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaInt(msg):
    while True:
        try:
            a = int(input(msg))
        except ValueError:
            print("Digite um valor inteiro válido.")
        except KeyboardInterrupt:
            print("Entrada de dados interrompida pelo usuário.")
            return 0
        except Exception as erro:
            print(f"O erro foi: {erro.__class__}")
        else:
            return a

a = leiaInt("Digite um número inteiro: ")

print(f"Você digitou {a}.\nVolte sempre.")