import csv
import os

def cadastrar_cto():
    pasta = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(pasta, "ctos.csv")

    ultimo_id = 0

    if os.path.exists(caminho):
        with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
            leitura = csv.reader(arquivo)

            next(leitura, None)  # pula o cabeçalho

            for linha in leitura:
                ultimo_id = int(linha[0])

    novo_id = ultimo_id + 1

    
    bairro = input("Bairro: ")
    capacidade = input("Capacidade: ")

    arquivo_existe = os.path.exists(caminho)

    with open(caminho, "a", newline="", encoding="utf-8") as arquivo:
        escrita = csv.writer(arquivo)

        if not arquivo_existe:
            escrita.writerow(["id", "bairro", "capacidade"])

        escrita.writerow([
            novo_id,
            bairro,
            capacidade
        ])

    print(f"CTO cadastrada com ID {novo_id}.")

