import cidade
import tkinter as tk
from tkinter import scrolledtext


def criar_janela_com_scroll(caminho_total):
    janela = tk.Tk()
    janela.title('Janela com Scroll')

    st = scrolledtext.ScrolledText(janela, width=45, height=10, font=('Courier', 13))
    st.pack()

    st.insert(tk.INSERT, '\n'.join(caminho_total))

    janela.mainloop()


vertice_inicial, vertice_final = None, None
inicial = 'Canoinhas'
final = 'Mafra'

for estacao in cidade.grafo.lista_estacao:
    if estacao.rotulo == inicial:
        vertice_inicial = estacao
    elif estacao.rotulo == final:
        vertice_final = estacao

objetivo = cidade.AEstrela(vertice_final)
objetivo.buscar(vertice_inicial)

caminho = cidade.retonar_caminho()

# espacamento = max(len(espaco) for espaco in caminho)
espacamento = 41

texto = []
borda = '|' + '-' * (espacamento + 2) + '|'
for cidade in caminho:
    if cidade[0] == 'A':
        texto.append(borda)

    texto.append("| " + cidade.ljust(espacamento) + " |")
texto.append(borda)
criar_janela_com_scroll(texto)
