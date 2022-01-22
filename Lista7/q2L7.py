# B. string_splosion
# string_splosion('Code') -> 'CCoCodCode'
# string_splosion('abc') -> 'aababc'
# string_splosion('ab') -> 'aab'
def string_splosion(s):
    saida = ''
    k = 1
    while k <= len(s):
        saida = saida + s[0:k]
        k = k + 1
    return saida


def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print('%s obtido: %s esperado: %s'
          % (prefixo, repr(obtido), repr(esperado)))


def main():
    print()
    print('String Explosion')
    test(string_splosion('Code'), 'CCoCodCode')
    test(string_splosion('abc'), 'aababc')
    test(string_splosion('ab'), 'aab')
    test(string_splosion('x'), 'x')
    test(string_splosion('fade'), 'ffafadfade')
    test(string_splosion('There'), 'TThTheTherThere')
    test(string_splosion('Kitten'), 'KKiKitKittKitteKitten')
    test(string_splosion('Bye'), 'BByBye')
    test(string_splosion('Good'), 'GGoGooGood')
    test(string_splosion('Bad'), 'BBaBad')


if __name__ == '__main__':
    main()
