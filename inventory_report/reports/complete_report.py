from collections import OrderedDict, Counter

from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport, OrderedDict):
    def generate(list):
        resultado = SimpleReport.generate(list)
        empresas = Counter([element["nome_da_empresa"] for element in list])
        resultado += "\nProdutos estocados por empresa:\n"
        for key, value in empresas.items():
            resultado += f"- {key}: {value}\n"

        return resultado
