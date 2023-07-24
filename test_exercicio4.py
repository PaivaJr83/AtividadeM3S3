import pytest
from exercicio4 import GerenciadorPecas

@pytest.fixture
def gerenciador():
    return GerenciadorPecas()

def test_cadastrar_peca(gerenciador):
    gerenciador.cadastrar_peca("Peca1", "Fabricante1", 10.0)
    gerenciador.cadastrar_peca("Peca2", "Fabricante2", 15.0)

    assert len(gerenciador.pecas) == 2

def test_consultar_todas_pecas(gerenciador):
    gerenciador.cadastrar_peca("Peca1", "Fabricante1", 10.0)
    gerenciador.cadastrar_peca("Peca2", "Fabricante2", 15.0)

    pecas = gerenciador.consultar_todas_pecas()

    assert len(pecas) == 2

def test_consultar_peca_por_codigo(gerenciador):
    gerenciador.cadastrar_peca("Peca1", "Fabricante1", 10.0)
    gerenciador.cadastrar_peca("Peca2", "Fabricante2", 15.0)

    peca = gerenciador.consultar_peca_por_codigo(1)
    assert peca is not None
    assert peca['codigo'] == 1

    peca = gerenciador.consultar_peca_por_codigo(3)
    assert peca is None

def test_consultar_pecas_por_fabricante(gerenciador):
    gerenciador.cadastrar_peca("Peca1", "Fabricante1", 10.0)
    gerenciador.cadastrar_peca("Peca2", "Fabricante2", 15.0)
    gerenciador.cadastrar_peca("Peca3", "Fabricante1", 20.0)

    pecas_fabricante1 = gerenciador.consultar_pecas_por_fabricante("Fabricante1")
    assert len(pecas_fabricante1) == 2

    pecas_fabricante2 = gerenciador.consultar_pecas_por_fabricante("Fabricante2")
    assert len(pecas_fabricante2) == 1

def test_remover_peca(gerenciador):
    gerenciador.cadastrar_peca("Peca1", "Fabricante1", 10.0)
    gerenciador.cadastrar_peca("Peca2", "Fabricante2", 15.0)

    resultado1 = gerenciador.remover_peca(1)
    assert resultado1 is True
    assert len(gerenciador.pecas) == 1

    resultado2 = gerenciador.remover_peca(3)
    assert resultado2 is False
    assert len(gerenciador.pecas) == 1
