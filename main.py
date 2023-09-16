try:
    numerador = int(input("Numerador: "))
    denominador = int(input("Denomindor: "))
    r = numerador / denominador
except ZeroDivisionError:
    print(f"Você não pode realizar uma divisão por zero.")
except (ValueError, TypeError):
    print(f"Infelizmente tivemos um problema com os tipos de dados que você digitou.oitro")
except KeyboardInterrupt:
    print(f"O usuário preferiu não informar o dados!")
except Exception as erro:
    print(f"O erro encontrado foi {erro.__cause__}")
else:
    print(r)
finally:
    print("Volte sempre! Muito obrigado!")