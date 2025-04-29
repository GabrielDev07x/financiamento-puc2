def calcular_valor_parcela(valor_financiado, taxa_juros_anual, anos):
    taxa_mensal = taxa_juros_anual / 12 / 100
    meses = anos * 12
    if taxa_mensal == 0:
        return valor_financiado / meses
    parcela = valor_financiado * (taxa_mensal * (1 + taxa_mensal) ** meses) / ((1 + taxa_mensal) ** meses - 1)
    return parcela

#Calculadoraaa
def calcular_montante_final(valor_financiado, taxa_juros_anual, anos):
    parcela = calcular_valor_parcela(valor_financiado, taxa_juros_anual, anos)
    return parcela * anos * 12

def calcular_juros_simples(capital, taxa_anual, anos):
    return capital * (taxa_anual / 100) * anos

def calcular_juros_compostos(capital, taxa_anual, anos):
    return capital * ((1 + taxa_anual/100) ** anos - 1)

def financiamento_viavel(renda_mensal, valor_parcela):
    return valor_parcela <= renda_mensal * 0.3