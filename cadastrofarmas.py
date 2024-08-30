repositorio = [
    {
        "crf": 7180,
        "nome": "Francisco Thiago Guedes Holanda",
        "endereço": "rua 824, casa 42, Terceira Etapa",
        "bairro": "Conjunto Ceará",
        "cep": "60532220", #quando o número for grande, não cabe no int e preciso transfomá-lo em texto
        "telefone": "85997267990",
        "email": "guedesholanda@gmail.com",
        "cpf": "95946306391",
        "identidade": "99012019037",
    }
]
crfAtual = 7180
# menu de navegação
while True:
    print('--- BEM VINDO AO MENU ---')
    print('1 - Cadastrar farmacêutico')
    print('2 - Listar todos')
    print('3 - Pesquisar farmacêutico')
    print('4 - Editar farmacêutico')
    print('5 - Excluir farmacêutico')
    print('6 - Sair')
    opcao = input('Selecione uma opção: ')
    if opcao == '6':
        print('Você saiu do sistema...')
        break
    elif opcao == '1':
        crfAtual += 1
        crf = int(input('Digite o crf do farmacêutico: '))
        nome = input('Digite o nome completo: ')
        endereço = input('Digite o endereço completo: ')
        bairro = input('Digite o bairro: ')
        cep = input('Digite o cep sem pontuação, apenas números: ')
        telefone = input('Digite o telefone - utilizar apenas números: ')
        email = input('Digite teu email: ')
        cpf = input('Digite o CPF utilizando apenas números: ')
        identidade = input('Digite a identidade utilizando apenas números: ')
        #criando um dicionário
        farmaceutico = {
            "crf": crf,
            "nome": nome,
            "endereço": endereço,
            "bairro": bairro,
            "cep": cep,
            "telefone": telefone,
            "email": email,
            "cpf": cpf,
            "identidade": identidade
        }
        repositorio.append(farmaceutico)
        print('Farmacêutico(a) cadastrado com sucesso!')
        print(repositorio)
    elif opcao == '2':
        print('--- ALUNOS MATRICULADOS ---')
        for aluno in repositorio: #a cada volta, vai ser pegue um dicionário do repositorio
            print(f"Matricula: {aluno['matricula']}") #para apegar o valor no dicionário a sintaxe é: nome do dicionário['chave que quero acessar']
            print(f"Nome: {aluno['nome']}") # aspas duplas e simples são utilizadas para manter o conteudo dentro do outro
            print(f"Idade: {aluno['idade']}")
            print(f"Nota: {aluno['nota']}")
            print('-'*50) # Multiplica o - 50 vezes
    elif opcao == '3':
        matricula = int(input('Digite a matricula: '))
        print('-'*50)
        for aluno in repositorio: #percorremos a lista à procura da matrícula pesquisada
            if aluno['matricula'] == matricula: 
                print(f"Matricula: {aluno['matricula']}") 
                print(f"Nome: {aluno['nome']}") 
                print(f"Idade: {aluno['idade']}")
                print(f"Nota: {aluno['nota']}")
                print('-'*50)
                break
        else:
            print('Aluno não encontrado!')
    elif opcao == '4':
        matricula = int(input('Digite a matricula: '))
        print('-'*50)
        for aluno in repositorio:
            if aluno['matricula'] == matricula:
                aluno['nome'] = input('Digite o novo nome do aluno: ')
                aluno['idade'] = int(input('Digite a nova idade do aluno: '))
                aluno['nota'] = float(input('Digite a nova nota do aluno: '))
                print('Dados alterados com sucesso!')
                break
        else: #esse else não é do if, mas do for. No que chamamos de FOR-ELSE
            print('Aluno não encontrado!')
    elif opcao == '5':
        matricula = int(input('Digite a matricula: '))
        print('-'*50)
        for aluno in repositorio:
            if aluno['matricula'] == matricula:
                repositorio.remove(aluno)
                print('Aluno removido com sucesso')
                break
        else: 
            print('Aluno não encontrado!')