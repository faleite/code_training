import requests


class ListaRepositorios:
    def __init__(self, usuario):
        self._usuario = usuario

    def requisicao_api(self):
        reposta = requests.get(f'https://api.github.com/users/{self._usuario}/repos')
        if reposta.status_code == 200:
            return reposta.json()
        else:
            return reposta.status_code

    def imprimir_repositorios(self):
        dados_api = self.requisicao_api()
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                print(dados_api[i]['name'])
        else:
            print(dados_api)


repositorios = ListaRepositorios('faleite')
repositorios.imprimir_repositorios()
