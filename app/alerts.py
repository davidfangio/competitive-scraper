def deve_alertar(variacao):
    if variacao <= -10:
        return True

    return False

def gerar_alerta(resultado, produto):
    return (
        f"🚨 ALERTA DE PREÇO\n"
        f"Produto: {produto}\n"
        f"Preço anterior: £{resultado['preco_anterior']:.2f}\n"
        f"Preço atual: £{resultado['preco_atual']:.2f}\n"
        f"Variação: {resultado['variacao']:.2f}%"
    )

def processar_alerta(resultado, produto):
    if deve_alertar(resultado["variacao"]):
        return gerar_alerta(resultado, produto)

    return None