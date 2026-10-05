def calcular_variacao(preco_anterior, preco_atual):
    variacao = ((preco_atual - preco_anterior) / preco_anterior) * 100

    return variacao


def classificar_variacao(variacao):
    if variacao < 0:
        return "queda"

    if variacao > 0:
        return "alta"

    if variacao == 0:
        return "sem alteração"


def analisar_preco(preco_anterior, preco_atual):
    variacao = calcular_variacao(preco_anterior, preco_atual)
    status = classificar_variacao(variacao)

    return {
        "preco_anterior": preco_anterior,
        "preco_atual": preco_atual,
        "variacao": variacao,
        "status": status
    }