"""Leitura dos arquivos CSV do projeto.
"""

import csv
from pathlib import Path

# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"


def ler_livros():
    """Lê o CSV e devolve uma lista de dicionários (um por livro).

    Tudo vem como texto, por exemplo:
    {"titulo": "Sharp Objects", "preco": "£47.82", "nota": "Four", ...}
    """
    lista_livros = []
    with open(CAMINHO_LIVROS, encoding="utf-8") as arq:
        for linha in csv.DictReader(arq):
            lista_livros.append(linha)
    return lista_livros


if __name__ == "__main__":
    dados_lidos = ler_livros()
    print(f"{len(dados_lidos)} livros carregados")
    print("Primeiro livro:", dados_lidos[0])