from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "Product",
        "Enterprise",
        "2022-10-28",
        "2023-10-28",
        "0001 1111 1222 1333 1444 4",
        "instrucao",
    )

    tag_product = (
        "O produto Product "
        "fabricado em 2022-10-28 "
        "por Enterprise com validade "
        "até 2023-10-28 precisa ser armazenado instrucao."
    )

    assert str(product) == tag_product
