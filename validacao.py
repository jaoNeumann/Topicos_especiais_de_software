# 8.3 - Validação
# 8.10 – Módulos
def input_float(msg):
    while True:
        valor = input(msg)
        try:
            return float(valor)
        except ValueError:
            print("⚠ Entrada inválida. Digite um número decimal separado por ponto.")


def input_int(msg, minimo=None, maximo=None):
    while True:
        valor = input(msg)
        try:
            valor_int = int(valor)
            if (minimo is not None and valor_int < minimo) or (maximo is not None and valor_int > maximo):
                print(f"⚠ Digite um número entre {minimo} e {maximo}.")
                continue
            return valor_int
        except ValueError:
            print("⚠ Entrada inválida. Digite um número inteiro.")


def input_str(msg):
    while True:
        valor = input(msg).strip()
        if valor == "":
            print("⚠ Campo não pode ser vazio.")
        else:
            return valor


def input_bool(msg):
    while True:
        valor = input(msg).strip().upper()
        
        if valor == 'S':
            return True
        if valor == 'N':
            return False

        print("⚠ Campo só pode conter 'S' ou 'N'.")
