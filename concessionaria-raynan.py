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

    for i, (marca, modelo) in enumerate(carros_cliente_vender, start = 1):
        print(f"{i} - {marca} {modelo}")

    escolha = int(input("\nDigite o número do carro que deseja vender: "))

    if escolha < 1 or escolha > len(carros_cliente_vender):
        print("\nNúmero inválido!")
        return
    
    marca, modelo = carros_cliente_vender[escolha - 1]

    print(f"\nVocê escolheu vender: {marca} {modelo}")
    
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

    marcas1 = ["Audi", "BYD", "Chevrolet"]

    for i, marca in enumerate(marcas1, start=1):
        print(f"{i} - {marca}")

    escolha_marca1 = input("\nDigite o número da marca desejada: ").strip()
    numeros_marca1 = [str(i) for i in range(1, len(marcas1) + 1)]

    if escolha_marca1 not in numeros_marca1:
        print("\nNúmero de marca inválido!")
        return

    escolha_marca1 = int(escolha_marca1)
    marca_escolhida1 = marcas1[escolha_marca1 - 1]


    modelos1 = [modelo for (marca, modelo) in carros_aluguel if marca == marca_escolhida1]

    if not modelos1:
        print(f"\nNenhum modelo disponível da marca {marca_escolhida1} no momento!")
        return
    
    print(f"\n=== MODELOS DISPONÍVEIS DE {marca_escolhida1} ===\n")

    for i, modelo in enumerate(modelos1, start=1):
        print(f"{i} - {modelo}")

    escolha_modelo1 = input("\nDigite o número do modelo desejado: ").strip()
    numeros_modelo1 = [str(i) for i in range(1, len(modelos1)+1)]

    if escolha_modelo1 not in numeros_modelo1:
        print("\nNúmero de modelo inválido!")
        return
    
    escolha_modelo1 = int(escolha_modelo1)
    modelo_escolhido1 = modelos1[escolha_modelo1 - 1]

    print(f"\nVocê escolheu: {marca_escolhida1} {modelo_escolhido1}")    

    dias = int(input("\nPor quantos dias você deseja alugar este carro? "))

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

    print("\n=== ESCOLHA A MARCA DO CARRO ===")


    marcas = ["Audi", "BYD", "Chevrolet"]

    for i, marca in enumerate(marcas, start=1):
        print(f"{i} - {marca}")

    escolha_marca = input("\nDigite o número da marca desejada: ").strip()
    numeros_marca = [str(i) for i in range(1, len(marcas)+1)]

    if escolha_marca not in numeros_marca:
        print("\nNúmero de marca inválido!")
        return

    escolha_marca = int(escolha_marca)
    marca_escolhida = marcas[escolha_marca - 1]

    modelos = [modelo for (marca, modelo) in carros_para_venda if marca == marca_escolhida]

    if not modelos:
        print(f"\nNenhum modelo disponível da marca {marca_escolhida} no momento!")
        return

    print(f"\n=== MODELOS DISPONÍVEIS DE {marca_escolhida} ===\n")
    for i, modelo in enumerate(modelos, start=1):
        print(f"{i} - {modelo}")

    escolha_modelo = input("\nDigite o número do modelo desejado: ").strip()
    numeros_modelo = [str(i) for i in range(1, len(modelos)+1)]

    if escolha_modelo not in numeros_modelo:
        print("\nNúmero de modelo inválido!")
        return

    escolha_modelo = int(escolha_modelo)
    modelo_escolhido = modelos[escolha_modelo - 1]

    print(f"\nVocê escolheu: {marca_escolhida} {modelo_escolhido}")

    valor_base = carros_precos[marca_escolhida][modelo_escolhido]
    valor_final = valor_base * 1.25

    print(f"\nValor final da compra: R$ {valor_final:.2f}")

    if cliente["saldo"] < valor_final:
        print("\nSaldo insuficiente!")
        return

    if input("Confirmar compra (s/n)? ").lower() == "s":
        cliente["saldo"] -= valor_final
        carros_para_venda.remove((marca_escolhida, modelo_escolhido))
        print("\nCompra realizada com sucesso!")

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
            print(f"\nSeu saldo atual é: R$ {cliente["saldo"]:.2f}")
        case "0":
            print("Obrigado por visitar a acerela. Até logo!")
            break