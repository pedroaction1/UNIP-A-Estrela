import cidade
from tkinter import *
from tkinter import ttk as tk
from tkinter import messagebox


def pesquisar(inicial='', final=''):
    cidade.grafo.resetar_cidades()
    vertice_inicial = None
    vertice_final = None
    jornada.config(text="Caminho: ")

    if inicial == '' or final == '':
        messagebox.showinfo("Escolha suas localizações", "Por favor, escolha suas localizações.")
        return 0

    for estacao in cidade.grafo.lista_estacao:
        if estacao.rotulo == inicial:
            vertice_inicial = estacao
        elif estacao.rotulo == final:
            vertice_final = estacao

    objetivo = cidade.AEstrela(vertice_final)
    objetivo.buscar(vertice_inicial)
    estacoes = objetivo.retonar_estacoes()

    for estacao in estacoes:
        texto = jornada.cget("text") + " --> " + estacao
        jornada.config(text=texto)
    return 0


# Inicialização da Tela
janela = Tk()
janela.title("Minha Interface")
janela.resizable(False, False)

# Configuração do Grid
janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=3)

# titulo
titulo = tk.Label(janela, text="GPS - Trens em Curitiba", font=('Arial', 13))
titulo.grid(column=1, row=0, padx=5, pady=5)

# Cidade Inicial
label_Inicial = tk.Label(janela, text="Local Inicial")
label_Inicial.grid(column=0, row=1, padx=0, pady=0)

# Combobox das Cidades Iniciais
cidade_inicial = tk.Combobox(janela, textvariable="bruh", state="readonly")
cidade_inicial['values'] = (
    "Porto União", "Paulo Frontin", "Canoinhas", "Três Barras", "São Mateus do Sul", "Irati", "Curitiba", "Palmeira",
    "Mafra", "Campo Largo", "Balsa Nova", "Lapa", "Tijucas do Sul", "Araucária", "São José dos Pinhais", "Contenda")
cidade_inicial.grid(column=0, row=2, padx=10, pady=10)

# Destino/Cidade Final
destino = tk.Label(janela, text="Destino Final")
destino.grid(column=2, row=1, padx=10, pady=10)

# Combobox de Destino/Cidade Final
caixa_final = tk.Combobox(janela, textvariable="burh", state="readonly")
caixa_final['values'] = (
    "Porto União", "Paulo Frontin", "Canoinhas", "Três Barras", "São Mateus do Sul", "Irati", "Curitiba", "Palmeira",
    "Mafra", "Campo Largo", "Balsa Nova", "Lapa", "Tijucas do Sul", "Araucária", "São José dos Pinhais", "Contenda")
caixa_final.grid(column=2, row=2, padx=10, pady=10)

# Botão de Pesquisar a Jornada
botao = tk.Button(janela, text="Calcular Rota", command=lambda: pesquisar(cidade_inicial.get(), caixa_final.get()))
botao.grid(column=1, row=3, padx=5, pady=5)

# Jornada Percorrida
jornada = tk.Label(janela, text="Caminho: ")
jornada.grid(column=0, columnspan=3, row=4, padx=10, pady=10)

canvas = Canvas(bg="lightgray", highlightbackground="black", highlightthickness=3, height=400, width=700)
canvas.grid(column=0, row=5, sticky=S, columnspan=3)

E_porto = canvas.create_text(100, 200, text="Porto\nUnião", fill="black", font=('Arial', 8))
E_paulo = canvas.create_text(160, 110,  text="Paulo Frontin", fill="black", font=('Arial', 8))
E_canoinhas = canvas.create_text(170, 320, text="Canoinhas", fill="black", font=('Arial', 8))
E_irati = canvas.create_text(200, 60,  text="Irati", fill="black", font=('Arial', 8))
E_sao_mateus = canvas.create_text(270, 180, text="São Mateus", fill="black", font=('Arial', 8))
E_barras = canvas.create_text(240, 240, text="Três Barras", fill="black", font=('Arial', 8))
E_palmeira = canvas.create_text(370, 60,  text="Palmeira", fill="black", font=('Arial', 8))
E_contenda = canvas.create_text(370, 145, text="Contenda", fill="black", font=('Arial', 8))
E_lapa = canvas.create_text(350, 230, text="Lapa", fill="black", font=('Arial', 8))
E_mafra = canvas.create_text(335, 310, text="Mafra", fill="black", font=('Arial', 8))
E_campo = canvas.create_text(520, 60,  text="Campo Largo", fill="black", font=('Arial', 8))
E_balsa = canvas.create_text(460, 120, text="Balsa\nNova", fill="black", font=('Arial', 8))
E_araucaria = canvas.create_text(480, 220, text="Araucária", fill="black", font=('Arial', 8))
E_tijucas = canvas.create_text(460, 335, text="Tijucas\ndo Sul", fill="black", font=('Arial', 8))
E_sao_jose = canvas.create_text(540, 270, text="São José\ndos Pinhais", fill="black", font=('Arial', 8))
E_curitiba = canvas.create_text(570, 210, text="Curitiba", fill="black", font=('Arial', 8))


L_porto_paulo = canvas.create_line(120, 200, 160, 115, width=2)
L_porto_mateus = canvas.create_line(120, 200, 240, 180, width=2)
L_porto_canoinhas = canvas.create_line(120, 200, 175, 315, width=2)
L_paulo_irati = canvas.create_line(160, 100, 200, 65, width=2)
L_irati_mateus = canvas.create_line(200, 65, 270, 170, width=2)
L_irati_palmeira = canvas.create_line(210, 60, 345, 60, width=2)
L_mateus_barras = canvas.create_line(270, 190, 240, 230, width=2)
L_mateus_lapa = canvas.create_line(300, 180, 335, 230, width=2)
L_canoinhas_barras = canvas.create_line(200, 320, 240, 250, width=2)
L_canoinhas_mafra = canvas.create_line(200, 320, 320, 310, width=2)
L_lapa_mafra = canvas.create_line(350, 240, 335, 300, width=2)
L_lapa_contenda = canvas.create_line(365, 230, 370, 155, width=2)
L_palmeira_mateus = canvas.create_line(270, 170, 370, 70, width=2)
L_palmeira_campo = canvas.create_line(395, 60, 485, 60, width=2)
L_campo_balsa = canvas.create_line(520, 70, 460, 105, width=2)
L_campo_curitiba = canvas.create_line(555, 60, 570, 200, width=2)
L_contenda_balsa = canvas.create_line(370, 135, 445, 120, width=2)
L_contenda_araucaria = canvas.create_line(395, 145, 455, 220, width=2)
L_curitiba_araucaria = canvas.create_line(550, 210, 505, 220, width=2)
L_curitiba_sao_jose = canvas.create_line(570, 220, 540, 260, width=2)
L_sao_jose_tijucas = canvas.create_line(540, 290, 475, 335, width=2)
L_tijucas_mafra = canvas.create_line(440, 335, 350, 310, width=2)


janela.geometry("750x600")
janela.mainloop()
