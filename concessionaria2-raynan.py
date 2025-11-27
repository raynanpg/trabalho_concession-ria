print("=== \nBEM-VINDO A CONCESSIONÁRIA ACERELA ===")

print("\nFaça seu cadastro para iniciarmos o atendimento.")

cliente = {
    "nome": input("\nDigite seu nome: "),
    "email": input("Digite seu e-mail: "),
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
    ("Audi", "A3"),
    ("BYD", "T3"),
    ("BYD", "Dolphin"),
    ("Chevrolet", "Onix"),
    ("Chevrolet", "Tracker")
]

carros_para_venda = [
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


def menu():

    print("\n===== CONCESSIONÁRIA ACERELA =====")
    print("1 - Venda seu carro")
    print("2 - Alugar")
    print("3 - Comprar")
    print("4 - Ver saldo")
    print("0 - Sair")

def vender_carro():

    print("\n=== VENDA SEU CARRO ===")

    print("\nCarros que compramos: ")

    for marca, modelo in carros_cliente_vender:
        print(f"\n- {marca} {modelo}")
    
    marca = input(f"\nDigite a marca do carro que deseja vender: ").strip()
    modelo = input("Digite o modelo do carro: ").strip()

    if (marca,modelo) not in carros_cliente_vender:
        print("\nDesculpe, não compramos este carro. Venda não realiazada.")
        return
    

    valor_medio = carros_precos[marca][modelo]
    proposta = valor_medio * 0.88

    print(f"\nValor médio do carro: R$ {valor_medio:.2f}")
    print(f"Proposta da concessionária: R$ {proposta:.2f}")

    confirmacao = input("\nDeseja vender este carro (s/n)?").strip().lower()

    if confirmacao == "s":
        cliente["saldo"] += proposta

        carros_para_venda.append((marca, modelo))

        print("\nCarro vendido com sucesso!")
    else:
        print("\nVenda cancelada.")


def alugar_carro():

    print("\n=== ALUGUE UM CARRO ===")

    def menu2():
        print("\n=== ESCOLHA A MARCA DO CARRO ===")
        print("1 - AUDI")
        print("2 - BYD")
        print("3 - Chevrolet")
        print("0 - Voltar")
    
    while True:
        menu2()

        opcao = input("Escolha uma marca: ")

        match opcao:
            case "1":
                marca = "Audi"
            case "2":
                marca = "BYD"
            case "3":
                marca = "Chevrolet"
            case "0":
                print("Votlando ao menu principal...")
                return
            case _:
                print("\nOpção inválida")
                continue

        modelos = [(marca_carro, modelo) for marca_carro, modelo in carros_aluguel if marca_carro == marca.lower()]

        print(f"\n=== MODELOS DISPONÍVEIS PARA {marca} ===")
        
        for i, (marca_carro, modelo) in enumerate(modelos, start=1):
            print(f"{i} - {modelo}")




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
