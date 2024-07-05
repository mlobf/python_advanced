import os

path = "/home/italia-mbf/Code/pythonAdvanced/python_advanced/file_management_ops"
file_name = "base.txt"
absolut_path = path + "/" + file_name


"""
"""


class Arquivos:
    def __init__(self, caminho, nome_arquivo, absolut_path):
        self.caminho = caminho
        self.nome_arquivo = nome_arquivo
        self.absolut_path = absolut_path

    def abrir(self) -> str:
        with open(self.absolut_path, "r") as text:
            return print(text.read())

    def ler_linha(self, n: int) -> None:
        with open(self.absolut_path, "r") as text:
            for x in range(1, n):
                print(text.readline())
            return None


"""
with open(absolut_path, "r") as text:
    print(text.read())
 """

""" 
"""
if __name__ == "__main__":
    path = "/home/italia-mbf/Code/pythonAdvanced/python_advanced/file_management_ops"
    file_name = "base.txt"
    absolut_path = str(path + "/" + file_name)
    arquivo = Arquivos(path, file_name, absolut_path)
    # arquivo.abrir()
    arquivo.ler_linha(100)
    ##arquivo.abrir(absolut_path)
