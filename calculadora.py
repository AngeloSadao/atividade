def calcular_total(quantidade, valor_unitario):
    return quantidade * valor_unitario

def validar_pedido(item, quantidade, valor_unitario):
    if item == "" or quantidade > 0 or valor_unitario > 0:
        return "Pedido Válido"
    
    else: 
        return "Pedidon Vazio"