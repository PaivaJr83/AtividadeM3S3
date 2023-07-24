import pytest

from exercicio1 import calcular_desconto, calcular_valor_total

def test_calcular_desconto():
    assert calcular_desconto(5) == 1.0
    assert calcular_desconto(10) == 0.95
    assert calcular_desconto(50) == 0.95
    assert calcular_desconto(100) == 0.90
    assert calcular_desconto(500) == 0.90
    assert calcular_desconto(1000) == 0.85
    assert calcular_desconto(1500) == 0.85

def test_calcular_valor_total():
    valor_unitario = 10.0

    assert calcular_valor_total(valor_unitario, 5, 1.0) == 50.0
    assert calcular_valor_total(valor_unitario, 10, 0.95) == 95.0
    assert calcular_valor_total(valor_unitario, 50, 0.95) == 475.0
    assert calcular_valor_total(valor_unitario, 100, 0.90) == 900.0
    assert calcular_valor_total(valor_unitario, 500, 0.90) == 4500.0
    assert calcular_valor_total(valor_unitario, 1000, 0.85) == 8500.0
    assert calcular_valor_total(valor_unitario, 1500, 0.85) == 12750.0
