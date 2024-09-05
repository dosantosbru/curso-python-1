from metodos import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet', True)
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Flavia', 8)
restaurante_praca.receber_avaliacao('Emily', 5)


# restaurante_japones = Restaurante('jun', 'japonesa', True)
# restaurante_hamburgueira = Restaurante('Mania', 'Hamburgueria', False)
# restaurante_japones.alternar_estado()


def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
