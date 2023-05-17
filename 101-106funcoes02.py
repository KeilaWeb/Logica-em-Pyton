#101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.#
'''def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano
    if idade < 16:
        return f'Com apenas {idade} ANOS: NÃO VOTA'
    elif idade <= 18 or anoatual > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

resp = int(input('Ano de nascimento: '))
print(voto(resp))'''

#102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.#
def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
help(fatorial)