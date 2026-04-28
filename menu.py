

''
item_agenda1 = {'nome' : 'José Antônio', 'telefone' : '73-8518111', 'email' : 'za@rocketseat.com', 'favorito' : False}
item_agenda2 = {'nome' : 'Maria Silva', 'telefone' : '73-8518112', 'email' : 'ms@rocketseat.com', 'favorito' : True}
item_agenda3 = {'nome' : 'Carlos Oliveira', 'telefone' : '73-8518113', 'email' : 'co@rocketseat.com', 'favorito' : False}
item_agenda4 = {'nome' : 'Ana Costa', 'telefone' : '73-8518114', 'email' : 'ac@rocketseat.com', 'favorito' : True}
item_agenda5 = {'nome' : 'Maria Costa', 'telefone' : '73-8518115', 'email' : 'mc@rocketseat.com', 'favorito' : True}
item_agenda6 = {'nome' : 'Joana Costa', 'telefone' : '73-8518116', 'email' : 'jc@rocketseat.com', 'favorito' : True}
item_agenda7 = {'nome' : 'Lidia Costa', 'telefone' : '73-8518117', 'email' : 'lc@rocketseat.com', 'favorito' : True}



lista_agenda = [item_agenda1, item_agenda2, item_agenda3, item_agenda4, item_agenda5, item_agenda6, item_agenda7   ] 

def print_menu():
    clear_screen()
    print('==============================')
    print('Bem-vindo à sua agenda de contatos!')
    print('1 - Listar contatos')
    print('2 - Adicionar contato')
    print('3 - Editar contato')
    print('4 - Excluir contato')
    print('5 - Listar favoritos')
    print('6 - Sair')

def clear_screen():
    print("\n" * 100)

def lista_contatos():
    clear_screen()
    print('Lista de contatos:')
    for contato in lista_agenda:
        print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}, Favorito: {'Sim' if contato['favorito'] else 'Não'}")
    print("Total de contatos:", len(lista_agenda)) 
    input('Pressione Enter para continuar...')

def edita_contato():
    try:
        if not lista_agenda:
            print('A agenda está vazia. Não há contatos para editar.')
            input('Pressione Enter para continuar...')
            return

        clear_screen()
        print('escolha o contato a ser editado:')
        for i, contato in enumerate(lista_agenda, start=1):
            print(f"{i} - {contato['nome']}")
        escolha = int(input('Digite o número do contato: ')) - 1
        if escolha < 1 or escolha > len(lista_agenda):
            raise ValueError('Número do contato inválido.')
        contato_selecionado = lista_agenda[escolha-1]
        print(f"Editando contato: {contato_selecionado['nome']}")
        nome = input('Digite o novo nome do contato (deixe em branco para manter o nome atual): ').strip('\n')
        telefone = input('Digite o novo telefone do contato (deixe em branco para manter o telefone atual): ')
        email = input('Digite o novo email do contato (deixe em branco para manter o email atual): ')
        favorito = input('O contato é favorito? (s/n, deixe em branco para manter o status atual): ').lower()
        if favorito in 'syt':
            favorito = True
        elif favorito in 'nf':
            favorito = False
        else:
            favorito = contato_selecionado['favorito']
    except Exception as e:
        print(f"Ocorreu um erro ao editar o contato: {e}")
        input('Pressione Enter para continuar...')
    else:
        contato_selecionado['nome'] = nome if nome else contato_selecionado['nome']
        contato_selecionado['telefone'] = telefone if telefone else contato_selecionado['telefone']
        contato_selecionado['email'] = email if email else contato_selecionado['email']
        contato_selecionado['favorito'] = favorito
        print('Contato editado com sucesso!')
        input('Pressione Enter para continuar...')

def excluir_contato():
    try:
        if not lista_agenda:
            print('A agenda está vazia. Não há contatos para excluir.')
            input('Pressione Enter para continuar...')
            return
        clear_screen()
        print('escolha o contato a ser excluído:')
        for i, contato in enumerate(lista_agenda, start=1):
            print(f"{i} - {contato['nome']}")
        escolha = int(input('Digite o número do contato: ')) - 1
        if escolha < 1 or escolha > len(lista_agenda):
            raise ValueError('Número do contato inválido.')
        contato_selecionado = lista_agenda[escolha-1]
        lista_agenda.remove(contato_selecionado)
        
    except Exception as e:
        print(f"Ocorreu um erro ao excluir o contato: {e}")
        input('Pressione Enter para continuar...')
    else:
        print('Contato excluído com sucesso!')
        input('Pressione Enter para continuar...')


def adiciona_contato():

    try:
        clear_screen()
        print('Inclusão de Novo contato:')
        nome = input('Digite o nome do contato: ').strip('\n')
        telefone = input('Digite o telefone do contato: ')
        email = input('Digite o email do contato: ')
        favorito = input('O contato é favorito? (s/n): ').lower() in 'sy'
        novo_contato = {'nome': nome, 'telefone': telefone, 'email': email, 'favorito': favorito}
        if not nome or not telefone or not email:
            raise ValueError('Todos os campos são obrigatórios.')
        if not nome.isprintable() or not telefone.isprintable() or not email.isprintable():
            raise ValueError('Todos os campos são obrigatórios.')
        lista_agenda.append(novo_contato)

    except Exception as e:
        print(f"Ocorreu um erro ao adicionar o contato: {e}")
        input('Pressione Enter para continuar...')
    else:
        print('Contato adicionado com sucesso!')
        input('Pressione Enter para continuar...')

while True:
    print_menu()
    opcao = input('Digite a opção desejada: ')
    if opcao == '6':    
        print('Saindo da agenda. Até mais!')
        break
    elif opcao == '1':
        lista_contatos()
    elif opcao == '2':
        adiciona_contato()
    elif opcao == '3':
        edita_contato()
    elif opcao == '4':
        excluir_contato()
    elif opcao == '5':
        print('Listar favoritos - Em desenvolvimento')
        input('Pressione Enter para continuar...')
    else:
        print('Opção inválida. Tente novamente.')
        input('Pressione Enter para continuar...')
