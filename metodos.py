from avaliacao import Avaliacao


class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria, ativo):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = ativo
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome:<20} | {self._categoria:<20}'

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'

    @classmethod
    def listar_restaurantes(cls):
        print(
            f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status".ljust(26)} | {"Avaliação".ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo:<25} | {str(restaurante.media_avaliacoes).ljust(25)}')

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @ property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas // quantidade_notas, 1)
        return media
