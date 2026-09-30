"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st

from dados import ler_livros


def preco_para_numero(texto_preco):
    """Transforma "£51.77" em 51.77."""
    return float(texto_preco.replace("£", ""))


def calcular_preco_medio(lista_livros):
    """Soma todos os preços e divide pela quantidade de livros."""
    total = 0
    for livro in lista_livros:
        total += preco_para_numero(livro["preco"])
    return total / len(lista_livros)


def contar_cinco_estrelas(lista_livros):
    """Conta quantos livros têm nota "Five"."""
    quantidade = 0
    for livro in lista_livros:
        if livro["nota"] == "Five":
            quantidade += 1
    return quantidade


def achar_livro_mais_caro(lista_livros):
    """Devolve o livro de maior preço."""
    campeao = lista_livros[0]  # "mais caro até agora"
    for livro in lista_livros:
        if preco_para_numero(livro["preco"]) > preco_para_numero(campeao["preco"]):
            campeao = livro
    return campeao


def main():
    st.title("📚 Dashboard de Livros")

    lista_livros = ler_livros()
    mais_caro = achar_livro_mais_caro(lista_livros)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total de livros", len(lista_livros))
    col2.metric("Preço médio", f"£{calcular_preco_medio(lista_livros):.2f}")
    col3.metric("Livros com 5 estrelas", contar_cinco_estrelas(lista_livros))
    col4.metric("Livro mais caro", mais_caro["preco"])
    col4.caption(mais_caro["titulo"])

    st.dataframe(lista_livros)


if __name__ == "__main__":
    main()