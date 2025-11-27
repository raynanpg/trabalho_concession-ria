print("=== \nBEM-VINDO A CONCESSIONÁRIA ACERELA ===")

print("\nFaça seu cadastro para iniciarmos o atendimento.")

cliente = {
    "nome": input("\nDigite seu nome: "),
    "telefone": input("Digite seu número de telefone: "),
    "saldo": float(input("Digite seu saldo inicial (R$): "))
}

print("\nCadastro realizado com sucesso!")

carros_precos = {
    "Audi":{

        "Q3": 210000.0,
        "A3": 150000.0,
        "Q5": 320000.0,
        "A4": 250000.0,
        "Q7": 400000.0},

    "BYD":{

        "T3": 150000.0,
        "Dolphin": 130000.0,
        "Yuan Pro": 150000.0,
        "Tang": 380000.0,
        "Atto 3": 190000.0},

    "Chevrolet":{

        "Onix": 90000.0,
        "Tracker": 120000.0,
        "S10": 200000.0,
        "Spin": 110000.0,
        "Cruze": 130000.0}
}

carros_cliente_vender = [
    ("Audi", "Q3"),
    ("Audi", "A3"),
    ("Audi", "Q5"),
    ("Audi", "A4"),
    ("Audi", "Q7"),
    ("BYD", "T3"),
    ("BYD", "Dolphin"),
    ("BYD", "Yuan Pro"),
    ("BYD", "Tang"),
    ("BYD", "Atto 3"),
    ("Chevrolet", "Onix"),
    ("Chevrolet", "Tracker"),
    ("Chevrolet", "S10"),
    ("Chevrolet", "Spin"),
    ("Chevrolet", "Cruze")

]

carros_aluguel = [
    ("Audi", "Q3"),
    ("BYD", "T3"),
    ("Chevrolet", "Onix")

]

carros_para_venda = [
    ("Audi", "Q3"),
    ("Audi", "A3"),
    ("Audi", "Q5"),
    ("BYD", "T3"),
    ("BYD", "Dolphin"),
    ("BYD", "Yuan Pro"),
    ("Chevrolet", "Onix"),
    ("Chevrolet", "Tracker"),
    ("Chevrolet", "S10")

]


def menu():

    print("\n===== CONCESSIONÁRIA ACERELA =====")
    print("\n1 - Venda seu carro")
    print("2 - Alugar")
    print("3 - Comprar")
    print("4 - Ver saldo")
    print("0 - Sair")

def vender_carro():

    print("\nCarros que temos interesse em comprar: ")

    for marca, modelo in carros_cliente_vender:
        print(f"\n- {marca} {modelo}")
    
    marca = input(f"\nDigite a marca do carro que deseja vender: ")
    modelo = input("Digite o modelo do carro: ")

    if (marca,modelo) not in carros_cliente_vender:
        print("\nDesculpe, não compramos este carro. Venda não realiazada.")
        return
    

    valor_total = carros_precos[marca][modelo]
    proposta = valor_total * 0.88

    print(f"\nValor médio do carro: R$ {valor_total:.2f}")
    print(f"Proposta da concessionária: R$ {proposta:.2f}")

    confirmacao = input("\nDeseja vender este carro (s/n)? ").strip().lower()

    if confirmacao == "s":
        cliente["saldo"] += proposta

        print("\nCarro vendido com sucesso!")

        if (marca, modelo) not in carros_para_venda:

            carros_para_venda.append((marca, modelo))

    else:
        print("\nVenda cancelada.")


def alugar_carro():

    print("\n=== CARROS PARA ALUGAR ===")

    for marca, modelo in carros_aluguel:
        print(f"{marca} {modelo}")

    marca = input("\nQual a marca do carro que deseja alugar? ")
    modelo = input("Qual o modelo do carro? ")

    print(f"\nVocê escolheu: {marca} {modelo}")

    dias = int(input("Por quantos dias você deseja alugar este carro? "))

    dias_totais = dias * 77

    print(f"\nO valor total do aluguel: R$ {dias_totais:.2f}")

    if cliente["saldo"] < dias_totais:
        print("Saldo insuficiente!")
        return
    
    confirmacao = input("\nConfirmar o aluguel (s/n): ").lower().strip()
    if confirmacao == "s":

        cliente["saldo"] -= dias_totais
        print("Aluguel feito!")
    
    else:

        print("Aluguel cancelado.")

def comprar_carro():

    print("\n=== CARROS DISPONÍVEIS PARA COMPRA ===\n")

    for marca, modelo in carros_para_venda:
        print(f"{marca} {modelo}")

    marca = input("\nInforme a marca do carro que deseja comprar: ")
    modelo = input("Informe o modelo do carro: ")

    print(f"\nVocê escolheu {marca} {modelo}")

    valor_total2 = carros_precos[marca][modelo]

    valor_final = valor_total2 * 1.25

    print(f"\nO valor total da compra é de: R$ {valor_final:.2f}")

    if cliente["saldo"] < valor_final:
        print("Saldo insuficiente!")
        return
    
    confirmacao = input("Confirmar compra (s/n)? ").lower()

    if confirmacao == "s":
        cliente["saldo"] -= valor_final

        carros_para_venda.remove((marca, modelo))

        print("\nCompra feita!")
    
    else:
        print("\nCompra cancelada.")

while True:
    menu()

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            vender_carro()
        case "2":
            alugar_carro()
        case "3":
            comprar_carro()
        case "4":
            print(f"\nSeu saldo atual é: R$ {cliente['saldo']:.2f}")
        case "0":
            print("Obrigado por visitar nossa concessionária. Até logo!")

