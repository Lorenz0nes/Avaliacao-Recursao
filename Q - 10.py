#b)
def numero_leituras_para_exceder(populacao_atual, objetivo, leituras):
    if populacao_atual > objetivo:
        return leituras
    else:
        return numero_leituras_para_exceder(populacao_atual * 3, objetivo, leituras + 1)

populacao_inicial = 50000
objetivo = 200000
leituras_necessarias = numero_leituras_para_exceder(populacao_inicial, objetivo, 0)

print(f"A população excederá 200,000 bactérias em {leituras_necessarias} leituras.")
