from dataclasses import dataclass
import csv
import os


@dataclass
class Cliente:
    nome: str
    residencia: str
    cpf: str
    telefone: str
    gmail: str
    plano: str
    ativo: bool = True

    def escolher_plano(self):
        pasta_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_csv = os.path.join(pasta_atual, "planos.csv")

        with open(caminho_csv, "r", newline="", encoding="utf-8") as arquivo:
            leitura = csv.reader(arquivo)

            next(leitura)  

            for linha in leitura:
                print(f"Plano: {linha[0]} | Velocidade: {linha[1]} | Preço: R$ {linha[2]}")

    def salvar(self):
        pasta_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_csv = os.path.join(pasta_atual, "clientes.csv")

        arquivo_existe = os.path.exists(caminho_csv)

        with open(caminho_csv, "a", newline="", encoding="utf-8") as arquivo:
            escrita = csv.writer(arquivo)

            if not arquivo_existe:
                escrita.writerow([
                    "nome",
                    "residencia",
                    "cpf",
                    "telefone",
                    "gmail",
                    "plano",
                    "ativo"
                ])

            escrita.writerow([
                self.nome,
                self.residencia,
                self.cpf,
                self.telefone,
                self.gmail,
                self.plano,
                self.ativo
            ])


cliente = Cliente(
    nome="Estefany",
    residencia="Rua das Flores, 123",
    cpf="12345678901",
    telefone="11987654321",
    gmail="cris281107@gmail.com",
    plano="500 Mega"
)

cliente.salvar()