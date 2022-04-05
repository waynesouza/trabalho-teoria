def tratar_linha(linha):
    linha_tratada = list()

    for parte_da_linha in linha:
        # Se a parte da linha terminar com quebra de linha, remove a quebra de linha
        if parte_da_linha.endswith('\n'):
            parte_da_linha = parte_da_linha[:len(parte_da_linha) - 1]
        # Se a parte da linha for vazia ou '--', é ignorado
        if parte_da_linha == '' or parte_da_linha == '--' or parte_da_linha == '__':
            continue
        # Apenas o que interessa estaram nessa lista
        linha_tratada.append(parte_da_linha)

    # Retorna as partes da linha já tratadas
    return linha_tratada


def abrir_arquivo(nome_arquivo):
    # Abre o arquivo
    with open(nome_arquivo) as a:
        # Pega o conteúdo do arquivo
        linhas = a.readlines()
        # Verifica se contém informação útil
        for linha in linhas:
            args = tratar_linha(linha.split(' '))
            # Se a linha está vazia ou é um comentário ou é uma quebra de linha ou é um fechamento de bloco, é inútil
            if len(args) == 0 or args[0].endswith(';') or args[0].startswith('\n') or args[0].startswith('fim'):
                continue
