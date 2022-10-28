from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Product",
        "Enterprise",
        "2022-10-28",
        "2023-10-28",
        "0001 1111 1222 1333 1444 4",
        "instrucao",
    )

    assert product.id == 1
    assert product.nome_do_produto == "Product"
    assert product.nome_da_empresa == "Enterprise"
    assert product.data_de_fabricacao == "2022-10-28"
    assert product.data_de_validade == "2023-10-28"
    assert product.numero_de_serie == "0001 1111 1222 1333 1444 4"
    assert product.instrucoes_de_armazenamento == "instrucao"
