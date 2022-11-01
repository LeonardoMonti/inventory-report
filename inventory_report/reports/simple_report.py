from collections import Counter


class SimpleReport:
    def generate(list):
        lista_data_fabricacao = []
        lista_data_validade = []
        lista_nome_empresas = []

        for element in list:
            if "data_de_validade" in element.keys():
                lista_data_fabricacao.append(element["data_de_fabricacao"])
                lista_data_validade.append(element["data_de_validade"])
                lista_nome_empresas.append(element["nome_da_empresa"])

                fabricacao_mais_antiga = sorted(lista_data_fabricacao)[0]
                validade_mais_proxima = sorted(lista_data_validade)[0]

        empresa = Counter(lista_nome_empresas).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {fabricacao_mais_antiga}\n"
            f"Data de validade mais próxima: {validade_mais_proxima}\n"
            f"Empresa com mais produtos: {empresa}"
        )
