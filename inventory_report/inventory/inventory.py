import csv
import json

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory(CompleteReport, SimpleReport):
    def import_data(path, tipo):
        file = Inventory.get_file(path)
        resultado = ""
        if tipo == "simples":
            resultado = SimpleReport.generate(file)
        if tipo == "completo":
            resultado = CompleteReport.generate(file)
        return resultado

    def get_file(path):
        extensao = path.split(".")[-1]
        resultado = ""
        if extensao.upper() == "CSV":
            resultado = Inventory.get_file_csv(path)
        if extensao.upper() == "JSON":
            resultado = Inventory.get_file_json(path)
        return resultado

    def get_file_csv(path):
        try:
            lista_de_produtos = []
            with open(path, encoding="utf-8") as file:
                dados = csv.DictReader(file)
                for row in dados:
                    lista_de_produtos.append(row)
                return lista_de_produtos
        except Exception:
            print("Error: dados inválidos.")
            return

    def get_file_json(path):
        try:
            lista_de_produtos = []
            with open(path) as file:
                dados = json.load(file)
                for row in dados:
                    lista_de_produtos.append(row)
                return lista_de_produtos
        except Exception:
            print("Error: dados inválidos.")
            return
