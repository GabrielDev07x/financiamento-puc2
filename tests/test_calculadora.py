import pytest
from financiamento import calculadora

def test_calcular_valor_parcela():
    parcela = calculadora.calcular_valor_parcela(100000, 6, 30)
    assert round(parcela, 2) == 599.55

def test_calcular_montante_final():
    montante = calculadora.calcular_montante_final(100000, 6, 30)
    assert round(montante, 2) == 215838.0

def test_calcular_juros_simples():
    juros = calculadora.calcular_juros_simples(1000, 10, 2)
    assert juros == 200

def test_calcular_juros_compostos():
    juros = calculadora.calcular_juros_compostos(1000, 10, 2)
    assert round(juros, 2) == 210.0

def test_financiamento_viavel():
    assert calculadora.financiamento_viavel(5000, 1400) == True
    assert calculadora.financiamento_viavel(4000, 1400) == False