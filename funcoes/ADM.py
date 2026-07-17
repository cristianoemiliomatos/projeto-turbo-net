from dataclasses import dataclass
import csv
import os


@dataclass
class ADM:
    nome: str
    login: str
    senha_hash: str
    papel: str
    status: str = "ativo"

    def cadastrar_tecnico(self):
        
        pasta_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_arquivo = os.path.abspath(os.path.join(pasta_atual,"..", "dados", "lista_tecnicos.csv"))

        if not os.path.exists(caminho_arquivo):
            with open(caminho_arquivo, "w", newline="", encoding="utf-8") as arquivo:
                escritor = csv.DictWriter(arquivo, fieldnames=["ID", "nome", "cpf", "senha"])
                escritor.writeheader()

        
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = list(csv.DictReader(arquivo))

        if linhas:
            proximo_id = int(linhas[-1]["ID"]) + 1
        else:
            proximo_id = 1

        
        nome_tec = input("Digite o nome: ")
        cpf_tec = input("Digite o CPF: ")
        senha_tec = input("Digite a senha do técnico: ")

        
        campos = ["ID", "nome", "cpf", "senha"]

        with open(caminho_arquivo, "a", newline="", encoding="utf-8") as arquivo:
            escrever = csv.DictWriter(arquivo, fieldnames=campos)
            escrever.writerow({
                "ID": proximo_id,
                "nome": nome_tec,
                "cpf": cpf_tec,
                "senha": senha_tec
            })

        print(f"Cadastrado! ID gerado: {proximo_id}")





    def adicionar_plano(self):
        pasta_atual = os.path.dirname(os.path.abspath(__file__))
        caminho = os.path.abspath(os.path.join(pasta_atual, "..", "dados", "planos.csv"))
        

        plano = input("Digite o nome do plano: ")
        velocidade = int(input("Digite a velocidade do plano: "))
        preco = float(input("Digite o preço do plano: "))

        dados = {
                "plano": plano,
                "velocidade":velocidade,
                "preco":preco
            }
        campos = ["plano", "velocidade", "preco"]
        with open(caminho, "a", newline="", encoding="utf-8") as arquivo:
                adicionar = csv.DictWriter(arquivo, fieldnames=campos)
                adicionar.writerow(dados)

    def remover_tecnico(self):
        id_remover = input("Digite o ID do técnico: ")
        pasta_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_arquivo = os.path.abspath(os.path.join(pasta_atual,"..", "dados", "lista_tecnicos.csv"))
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            tecnicos = list(csv.DictReader(arquivo))

        tecnicos_filtrados = []

        for tecnico in tecnicos:
            if tecnico["ID"] != id_remover:
                tecnicos_filtrados.append(tecnico)

        with open(caminho_arquivo, "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.DictWriter(
                arquivo,
                fieldnames=["ID", "nome", "cpf", "senha"]
            )

            escritor.writeheader()
            escritor.writerows(tecnicos_filtrados)

        print("Técnico removido.")
