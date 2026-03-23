from calculadora import calcular_total, validar_pedido

def test_calcular_valor_itens():
    assert calcular_total(4, 2) == 8

def test_erro_calcular_valor_itens():
    assert calcular_total(4, 4) == 8

def test_erro_calcular_valor_itens():
    assert calcular_total(4, 3) == 8

def test_validar_pedido_valor_itens():
    assert validar_pedido("teste", 4, 2) == 8

def test_erro_validar_pedido_valor_itens():
    assert validar_pedido("teste", 4, 4) == 8