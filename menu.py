


lista_agenda = [
               {'nome' : 'José Antônio', 'telefone' : '73-8518111', 'email' : 'za@rocketseat.com', 'favorito' : False},
               {'nome' : 'Maria Silva', 'telefone' : '73-8518112', 'email' : 'ms@rocketseat.com', 'favorito' : True},
               {'nome' : 'Carlos Oliveira', 'telefone' : '73-8518113', 'email' : 'co@rocketseat.com', 'favorito' : False},
               {'nome' : 'Ana Costa', 'telefone' : '73-8518114', 'email' : 'ac@rocketseat.com', 'favorito' : False},
               {'nome' : 'Maria Costa', 'telefone' : '73-8518115', 'email' : 'mc@rocketseat.com', 'favorito' : False},
               {'nome' : 'Joana Costa', 'telefone' : '73-8518116', 'email' : 'jc@rocketseat.com', 'favorito' : False},
               {'nome' : 'Lidia Costa de Oliveira Brum Nascimento', 'telefone' : '73-8518117', 'email' : 'lc@rocketseat.com', 'favorito' : False},
               {'nome' : 'Marcos Antonio Galvão', 'telefone' : '73-99988554', 'email' : 'ximbinha@rocketseat.com', 'favorito' : False}
               ]


# lista_agenda = [] 



def print_menu():
    clear_screen()
    print('==============================')
    print('Bem-vindo à sua agenda de contatos!')
    print('1 - Listar contatos')
    print('2 - Adicionar contato')
    print('3 - Editar contato')
    print('4 - Excluir contato')
    print('5 - Favoritar/Desfavoritar contato')
    print('6 - Listar favoritos')
    print('7 - Sair')

def clear_screen():
    print("\n" * 100)

def lista_contatos(favoritos=False):
    clear_screen()
    size_max_nome = max(len(contato['nome']) for contato in lista_agenda) if lista_agenda else 0
    size_max_telefone = max(len(contato['telefone']) for contato in lista_agenda) if lista_agenda else 0
    size_max_email = max(len(contato['email']) for contato in lista_agenda) if lista_agenda else 0
    print(f'Lista de contatos{"(favoritos):" if favoritos else ":"}  ')
    total = 0
    for contato in lista_agenda:
        if favoritos and not contato['favorito']:
            continue
        print(f"Nome: {(contato['nome']).ljust(size_max_nome)}, Telefone: {(contato['telefone']).ljust(size_max_telefone)}, Email: {(contato['email']).ljust(size_max_email)}, Favorito: {'Sim' if contato['favorito'] else 'Não'}")
        total += 1
    print("Total de contatos:", total) 
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
        if escolha < 0 or escolha >= len(lista_agenda):
            raise ValueError('Número do contato inválido.')
        contato_selecionado = lista_agenda[escolha]
        print(f"Editando contato: {contato_selecionado['nome']} (Telefone: {contato_selecionado['telefone']}, Email: {contato_selecionado['email']}, Favorito: {'Sim' if contato_selecionado['favorito'] else 'Não'})")
        nome = input('Digite o novo nome do contato (deixe em branco para manter o nome atual): ').strip('\n')
        telefone = input('Digite o novo telefone do contato (deixe em branco para manter o telefone atual): ')
        email = input('Digite o novo email do contato (deixe em branco para manter o email atual): ')
        favorito = input('O contato é favorito? (s/n, deixe em branco para manter o status atual): ').lower()
        favorito = True if favorito in 'sy' else False if favorito in 'nf' else contato_selecionado['favorito']
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
        if escolha < 0 or escolha >= len(lista_agenda):
            raise ValueError('Número do contato inválido.')
        contato_selecionado = lista_agenda[escolha]
        lista_agenda.remove(contato_selecionado)
        
    except ValueError as e:    
        print(f"Escolha um numero válido ")
        input('Pressione Enter para continuar...')
    except Exception as e:
        print(f"Ocorreu um erro ao excluir o contato: {e}")
        input('Pressione Enter para continuar...')
    else:
        print('Contato excluído com sucesso!')
        input('Pressione Enter para continuar...')


def favoritar_desfavoritar_contato():
    try:
        if not lista_agenda:
            print('A agenda está vazia. Não há contatos para editar.')
            input('Pressione Enter para continuar...')
            return

        clear_screen()
        print('escolha o contato a ser favoritado/desfavoritado:')
        for i, contato in enumerate(lista_agenda, start=1):
            print(f"{i} - {contato['nome']} (Favorito: {'Sim' if contato['favorito'] else 'Não'})")
        escolha = int(input('Digite o número do contato: ')) - 1
        if escolha < 0 or escolha >= len(lista_agenda):
            raise ValueError('Número do contato inválido.')
        contato_selecionado = lista_agenda[escolha]
        favorito = not contato_selecionado['favorito']
        
    except Exception as e:
        print(f"Ocorreu um erro ao editar o contato: {e}")
        input('Pressione Enter para continuar...')
    else:
        contato_selecionado['favorito'] = favorito
        print(f'Contato {contato_selecionado["nome"]} {("favoritado" if favorito else "desfavoritado")} com sucesso!')
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
    if opcao == '7':    
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
        favoritar_desfavoritar_contato()
    elif opcao == '6':
        lista_contatos(favoritos=True)
    else:
        print('Opção inválida. Tente novamente.')
        input('Pressione Enter para continuar...')
