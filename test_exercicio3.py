import pytest
from exercicio3 import CalculadorFrete

@pytest.fixture
def calculador():
    return CalculadorFrete()

def test_ler_dimensoes_objeto(calculador):
    volume = calculador.ler_dimensoes_objeto(10, 5, 2)
    assert volume == 100

    with pytest.raises(ValueError):
        calculador.ler_dimensoes_objeto(0, 10, 5)

def test_calcular_preco_volume(calculador):
    preco_volume = calculador.calcular_preco_volume(500)
    assert preco_volume == 10.0

    preco_volume = calculador.calcular_preco_volume(10000)
    assert preco_volume == 30.0

def test_validar_medida(calculador):
    medida = calculador.validar_medida("10")
    assert medida == 10

    with pytest.raises(ValueError):
        calculador.validar_medida("abc")

def test_ler_peso_objeto(calculador):
    multiplicador_peso = calculador.ler_peso_objeto(15)
    assert multiplicador_peso == 3.0

    with pytest.raises(ValueError):
        calculador.ler_peso_objeto(35)

def test_calcular_multiplicador_peso(calculador):
    multiplicador = calculador.calcular_multiplicador_peso(0.05)
    assert multiplicador == 1.0

    multiplicador = calculador.calcular_multiplicador_peso(5)
    assert multiplicador == 2.0

def test_ler_rota(calculador):
    rota = calculador.ler_rota("br")
    assert rota == "br"

    with pytest.raises(ValueError):
        calculador.ler_rota("xyz")

def test_calcular_multiplicador_rota(calculador):
    multiplicador = calculador.calcular_multiplicador_rota("rs")
    assert multiplicador == 1.0

    multiplicador = calculador.calcular_multiplicador_rota("sb")
    assert multiplicador == 1.2

def test_calcular_frete(calculador):
    total = calculador.calcular_frete(5000, 2.0, 1.5)
    assert total == 150

