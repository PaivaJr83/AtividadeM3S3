import pytest

from exercicio2 import calcular_pedido

def test_calcular_pedido():
    assert calcular_pedido(100) == 9.00
    assert calcular_pedido(101) == 11.00
    assert calcular_pedido(102) == 12.00
    assert calcular_pedido(103) == 12.00
    assert calcular_pedido(104) == 14.00
    assert calcular_pedido(105) == 17.00
    assert calcular_pedido(200) == 5.00
    assert calcular_pedido(201) == 4.00

def test_calcular_pedido_quantidade():
    assert calcular_pedido(100, 2) == 18.00
    assert calcular_pedido(103, 3) == 36.00

def test_calcular_pedido_opcao_invalida():
    try:
        calcular_pedido(999)
    except ValueError as e:
        assert str(e) == "Opção inválida"
