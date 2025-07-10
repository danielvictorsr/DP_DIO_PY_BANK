#import textwrap

def autenticacao():
    menu = """
╔═════════════════════════════════════════════╗
║█ SYSBANKPY █                                ║
╠═════════════════════════════════════════════╣
║                                             ║
║       [l]  Login                            ║
║       [nu] Novo usuário                     ║
║       [nc] Nova conta                       ║
║       [q]  Sair                             ║
║                                             ║
╚═════════════════════════════════════════════╝

                 
=> """
    return input(menu)

def menu():
    menu = """
╔═════════════════════════════════════════════╗
║█ SYSBANKPY █                                ║
╠═════════════════════════════════════════════╣
║                                             ║
║       [d]  Depositar                        ║
║       [s]  Sacar                            ║    
║       [e]  Extrato                          ║
║       [nc] Nova conta                       ║
║       [lc] Listar contas                    ║
║       [nu] Novo usuário                     ║
║       [q]  Sair                             ║
║                                             ║
╚═════════════════════════════════════════════╝

                 
=> """
    return input(menu)
    #[d]\tDepositar
    #return input(textwrap.dedent(menu))

# TODO - logar na conta; trocar de conta;
def depositar(saldo, valor, extrato, line, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print(f"💰💰💰  Deposito Realizado com Sucesso 💰💰💰") #{valor:.2f}
        print(f"                             Saldo: {saldo:.2f}")
        print(line)
    else:
        print("\n😑😑😑  Operação falhou! O valor informado é inválido. 😑😑😑")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques, line):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n😑😑😑  Operação falhou! O valor informado é inválido. 😑😑😑")

    elif excedeu_limite:
        print("\n😑😑😑  Operação falhou! O valor informado é inválido. 😑😑😑")

    elif excedeu_saques:
        print("\n😑😑😑  Operação falhou! O valor informado é inválido. 😑😑😑")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n💸💸💸 Saque realizado com sucesso! 💸💸💸")
        print(line)

    else:
        print("\n😑😑😑  Operação falhou! O valor informado é inválido. 😑😑😑")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    multiplicador = 19
    print("=" *multiplicador +" EXTRATO " + "=" *multiplicador)
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("=" *((multiplicador *2)+9))


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n😑😑😑  Já existe usuário com esse CPF! 😑😑😑")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("👤👤👤  Usuário criado com sucesso! 👤👤👤")


def buscar_conta(conta, contas):
    conta_resultado = [search_conta for search_conta in contas if search_conta["numero_conta"] == conta]
    return conta_resultado[0] if conta_resultado else None
    

def buscar_senha(senha, contas):
    senha_resultado = [search_senha for search_senha in contas if search_senha["senha"] == senha]
    return senha_resultado[0] if senha_resultado else None


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n🧾🧾🧾  Conta criada com sucesso! 🧾🧾🧾")
        return {"agencia": agencia, "numero_conta": numero_conta, "senha": 123, "usuario": usuario}

    print("\n😑😑😑 Usuário não encontrado, fluxo de criação de conta encerrado! 😑😑😑")


def listar_contas(contas, line):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print(linha)
        print(line)
        #print("=" * 100)
        #print(textwrap.dedent(linha))


def loop(LIMITE_SAQUES, AGENCIA, line, saldo, limite, extrato, numero_saques, usuarios, contas, logado):
        #se logado na conta segue o fluxo;
        #se não logado na conta: login [l] /n [nc] (l->login | nc->nova conta)
        while True:

            if logado == False:
                login = autenticacao()

                if login == "l":
                    print(line)
                    print("===Sistema de Login===")
                    conta = int(input("       Informe o número da conta (somente números): "))
                    
                    #verifica se conta existe
                    conta_resultado = buscar_conta(conta, contas)
                    if conta_resultado == None:
                        print("Conta Inexistente")
                    else:
                        senha = input("       Informe sua senha: ")
                        autenticar = buscar_senha(senha, contas)
            
                        if autenticar['senha'] == senha:
                            logado = True
                            print('Logado: ',logado)
                            loop(LIMITE_SAQUES, AGENCIA, line, saldo, limite, extrato, numero_saques, usuarios, contas, logado)

                elif login == "nu":
                    criar_usuario(usuarios)

                elif login == "nc":
                    numero_conta = len(contas) + 1
                    conta = criar_conta(AGENCIA, numero_conta, usuarios)
                    print("Sua conta é: ", conta['numero_conta'])

                    if conta:
                        senha = input("       Informe a senha: ")
                        conta['senha'] = senha

                        contas.append(conta)
                        #print(contas)
                        #print(usuarios)

                elif login == "q":
                    break

                elif login == "lc":
                    listar_contas(contas, line)

            else:   

                #opcao = menu()
                # TODO criar função para esta parte abaixo de opcao = "any"

                opcao = menu()

                if opcao == "d":
                    print(line)
                    valor = float(input("       Informe o valor do depósito: "))

                    saldo, extrato = depositar(saldo, valor, extrato, line)

                elif opcao == "s":
                    print(line)
                    valor = float(input("       Informe o valor do saque: "))

                    saldo, extrato = sacar(
                        saldo=saldo,
                        valor=valor,
                        extrato=extrato,
                        limite=limite,
                        numero_saques=numero_saques,
                        limite_saques=LIMITE_SAQUES,
                        line=line
                    )

                elif opcao == "e":
                    exibir_extrato(saldo, extrato=extrato)

                elif opcao == "nu":
                    criar_usuario(usuarios)

                elif opcao == "nc":
                    numero_conta = len(contas) + 1
                    conta = criar_conta(AGENCIA, numero_conta, usuarios)
                    #print("Sua conta é: ", conta['numero_conta'])
                    print("Sua conta é: ", conta['numero_conta'])

                    if conta:
                        senha = input("       Informe a senha: ")
                        conta['senha'] = senha

                        contas.append(conta)

                elif opcao == "lc":
                    listar_contas(contas, line)

                elif opcao == "q":
                    break

                else:
                    print("😑😑😑  Operação inválida, por favor selecione novamente a operação desejada. 😑😑😑")
    #end def loop


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    line = """═══════════════════════════════════════════════"""
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
        
    usuarios = []
    contas = []
    logado = False
    #senhas = []

    loop(LIMITE_SAQUES, AGENCIA, line, saldo, limite, extrato, numero_saques, usuarios, contas, logado)

main()