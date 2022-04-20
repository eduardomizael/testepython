from outra import OutraClasse

class Teste:
    cvar = 'cvar1'
    _cvar1 = 'cvar2'
    __cvar2 = 'cvar3'

    def __init__(self):
        self.var = 'ovar1'
        self._var2 = 'ovar2'
        self.__var3 = 'ovar3'


def main(*args, **kwargs):
    outra = OutraClasse()
    outra.metodo()
    print(outra.atributo)
    print(outra.__dict__)
    print(outra.__class__)
    print(outra.__class__.__dict__)
    print(outra.__class__.__name__)
    print(*args, **kwargs)


if __name__ == '__main__':
    main()
