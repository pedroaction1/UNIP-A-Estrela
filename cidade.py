import numpy as np
# import math


class Vertice:
    def __init__(self, rotulo, distancia_objetivo=0):
        self.rotulo = rotulo
        self.distancia_objetivo = distancia_objetivo
        self.distancia_lista = []
        self.visitado = False
        self.adjacentes = []

    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def adiciona_custo_objetivo(self, custo):
        self.distancia_lista.append(custo)

    def retona_adjacente(self):
        return self.adjacentes

    def mostra_adjacente(self):
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo)
    
    def mostrar_lista_objetivo(self):
        return self.distancia_lista


class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice #classe vertice com o rotulo (nome) da cidade
        self.custo = custo #O custo no arquivo Adjacentes para a cidade adjacente
        self.distancia_aestrela = vertice.distancia_objetivo + self.custo #O custo no arquivo Adjacentes para a cidade alvo


# Classe que junta as duas classes (vértice e adjacente - Grafo completo)
class Grafo:
    lista_estacao = []
    linha = []
    custo_reta = []
    linha_atual = 0

    # Cadastro das cidades
    cidades = open('vertices.txt', 'r', encoding='utf-8')
    for i in range(0, 16):
        lista_estacao.append(Vertice(cidades.readline().replace("\n", '')))
    cidades.close()

    # Cadastro dos adjacentes de cada cidade (nó)
    adjacentes = open('adjacentes.txt', 'r', encoding="utf-8")
    linha = adjacentes.readlines()

    i = 0
    while i != len(linha):
        if linha[i][:1].isupper():
            i += 1
            linha_atual += 1

        if linha[i][:1].islower or linha[i].isalnum:
            cidade = linha[i].replace("\n", '')
            indice_cidade = 0
            for indice_cidade in range(0, len(lista_estacao)):
                if cidade == lista_estacao[indice_cidade].rotulo.lower():
                    break
            i += 1
            custo = int(linha[i].replace("\n", ''))
            lista_estacao[linha_atual - 1].adiciona_adjacente(Adjacente(lista_estacao[indice_cidade], custo))

        i += 1
    adjacentes.close()


    retas_cidades = open('linha_reta.txt', 'r', encoding='utf-8')
    custo_reta = retas_cidades.readlines()

    j = 0
    k = 0
    linha_atual = 0
    while j != len(custo_reta):
        if custo_reta[j][:1].isupper():
            j+= 1
            linha_atual += 1
        
        if custo_reta[j][:1].islower or custo_reta[j].isalnum:
            cidade = custo_reta[j].replace("\n", '') #Curitiba, Campo largo, Canoinhas, Tijucas, Irati
            indice_cidade = 0
            for indice_cidade in range(0, len(lista_estacao)):
                if cidade == lista_estacao[indice_cidade].rotulo.lower():
                    break
            k = j + 1
            custo = int(custo_reta[k].replace("\n", ''))
            j += 2
            lista_estacao[indice_cidade].adiciona_custo_objetivo(custo)

    def resetar_cidades(self):
        for i in range(16):
            self.lista_estacao[i].visitado = False
    def setar_destino5(self):
        for i in range(16):
            self.lista_estacao[i].distancia_lista.append(0)


grafo = Grafo()
caminho = []


# Classe que ordena os valores pelo custo (distancia)
class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        # Mudança no tipo de dados
        self.valores = np.empty(self.capacidade, dtype=object)

    def insere(self, vertice, destino):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            for j in range(len(self.valores[i].adjacentes)):
                if (int(self.valores[i].adjacentes[j].distancia_aestrela + self.valores[i].distancia_lista[destino]) >
                        int(vertice.adjacentes[i].distancia_aestrela + vertice.distancia_lista[destino])):
                    break
                if i == self.ultima_posicao:
                    posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = vertice
        self.ultima_posicao += 1

    def imprime(self, atual, destino):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                for j in range(len(self.valores[i].adjacentes)):
                    if self.valores[i].adjacentes[j].vertice.rotulo == atual.rotulo:
                        string = f'{i + 1} - {self.valores[i].rotulo} --> {self.valores[i].adjacentes[j].custo} + {self.valores[i].distancia_lista[destino]} = {self.valores[i].adjacentes[j].custo + self.valores[i].distancia_lista[destino]}'
                        print(string)
                        caminho.append(string)


# Classe que realiza a busca A Estrela
class AEstrela:
    def __init__(self, _objetivo):
        self.objetivo = _objetivo
        self.encontrado = False
        self.estacoes = []

    def buscar(self, atual):
        print('-------------------------')
        string = f'Atual: {atual.rotulo}'
        print(string)
        atual.visitado = True
        caminho.append(string)
        self.estacoes.append(atual.rotulo)

        if atual == self.objetivo:
            string = "Voce chegou no seu destino."
            print(string)
            caminho.append(string)
            self.encontrado = True
        else:
            desitno = 0
            if self.objetivo.rotulo == 'Curitiba':
                destino = 0
            elif self.objetivo.rotulo == 'Campo Largo':
                destino = 1
            elif self.objetivo.rotulo == 'Canoinhas':
                destino = 2
            elif self.objetivo.rotulo == 'Tijucas do Sul':
                destino = 3
            elif self.objetivo.rotulo == 'Irati':
                destino = 4
            elif self.objetivo.rotulo != 'Irati' and 'Tijucas do Sul' and 'Canoinhas' and 'Campo Largo' and 'Curitiba':
                destino = 5
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if not adjacente.vertice.visitado:
                    vetor_ordenado.insere(adjacente.vertice, destino)
            vetor_ordenado.imprime(atual, destino)

            if vetor_ordenado.valores[0] is not None:
                self.buscar(vetor_ordenado.valores[0])

    def retonar_estacoes(self):
        return self.estacoes


def retonar_caminho():
    return caminho