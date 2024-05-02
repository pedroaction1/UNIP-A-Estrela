import cidade as gps
from tkinter import *
from tkinter import ttk as tk
from tkinter import messagebox
from tkinter import scrolledtext


def calcular_rota(inicial, final):
    gps.caminho = []
    gps.grafo.resetar_cidades()
    gps.grafo.setar_destino5()
    limpar_cidades()
    vertice_inicial = None
    vertice_final = None

    if inicial == 'Selecione a cidade de comeco' or final == 'Selecione a cidade de destino':
        messagebox.showinfo("Escolha suas localizações", "Por favor, escolha suas localizações.")
        return 0

    for cities in gps.grafo.lista_estacao:
        if cities.rotulo == inicial:
            vertice_inicial = cities
        if cities.rotulo == final:
            vertice_final = cities

    objetivo = gps.AEstrela(vertice_final)
    objetivo.buscar(vertice_inicial)

    visitados = objetivo.retonar_estacoes()
    pintar_cidades(visitados)
    pintar_linhas(visitados)


def saida():
    scroll_text.config(state=NORMAL)
    scroll_text.delete('1.0', END)
    caminho = gps.retonar_caminho()
    if len(caminho) == 0:
        caminho.append("Não há nenhum caminho sendo usado.")

    espacamento = 43
    texto = []
    borda = '|' + '-' * (espacamento + 2) + '|'
    for lugares in caminho:
        if lugares[0] == 'A' or lugares[0] == 'N':
            texto.append(borda)

        texto.append("| " + lugares.ljust(espacamento) + " |")
    texto.append(borda)

    scroll_text.insert('end', '\n'.join(texto))
    scroll_text.config(state=DISABLED)


def limpar_cidades():
    for cities in C:
        canvas.itemconfig(cities, fill="gray")
    for lines in linhas_cidades:
        canvas.itemconfig(lines, fill="black")


def pintar_cidades(visitados):
    for i in range(len(C)):
        nome = canvas.itemcget(N[i], "text")
        nome = nome.replace('\n', ' ')
        for visitado in visitados:
            if nome == visitado:
                canvas.itemconfig(C[i], fill="green")
                break


def pintar_linhas(visitados):
    for linha, (cidade1, cidade2) in linhas_cidades.items():
        if cidade1 in visitados and cidade2 in visitados:
            canvas.itemconfig(linha, fill='green')


janela = Tk()
janela.configure(background="black")

style = tk.Style()
style.configure("BW.TButton", borderwidth=0, font=("Arial", 17))

label = tk.Label(janela, text="GPS - Trens em Curitiba", font=("Arial", 14), anchor="center")
label.place(width=700, height=46, x=2, y=2)

cidade_inicial = tk.Combobox(janela, textvariable="burh", state="readonly", height=8, font=("Arial", 12))
cidade_inicial.place(width=350, height=50, x=2, y=50)
cidade_inicial['values'] = (
    "Porto União", "Paulo Frontin", "Canoinhas", "Três Barras", "São Mateus", "Irati", "Curitiba", "Palmeira",
    "Mafra", "Campo Largo", "Balsa Nova", "Lapa", "Tijucas do Sul", "Araucária", "São José dos Pinhais", "Contenda")
cidade_inicial.set("Selecione a cidade de comeco")

cidade_final = tk.Combobox(janela, textvariable="bruh", state="readonly", height=8, font=("Arial", 12))
cidade_final.place(width=350, height=50, x=352, y=50)
cidade_final['values'] = (
    "Porto União", "Paulo Frontin", "Canoinhas", "Três Barras", "São Mateus", "Irati", "Curitiba", "Palmeira",
    "Mafra", "Campo Largo", "Balsa Nova", "Lapa", "Tijucas do Sul", "Araucária", "São José dos Pinhais", "Contenda")
cidade_final.set("Selecione a cidade de destino")

botao = tk.Button(janela, text="Calcular Rota", style="BW.TButton",
                  command=lambda: calcular_rota(cidade_inicial.get(), cidade_final.get()))
botao.place(width=160, height=48, x=260, y=102)

botao_mostrar = tk.Button(janela, text="Mostar Rota", style="BW.TButton", command=lambda: saida())
botao_mostrar.place(width=394, height=98, x=704, y=2)

scroll_text = scrolledtext.ScrolledText(janela, width=47, height=28, state=DISABLED, bg="lightgray")
scroll_text.place(x=704, y=102)

canvas = Canvas(bg="lightgray", highlightbackground="black", highlightthickness=2, height=400, width=700)
canvas.place(x=0, y=145)

# C = Cidade / City
C_porto = canvas.create_rectangle(115, 195, 125, 205, fill="grey")
C_paulo = canvas.create_rectangle(155, 110, 165, 120, fill="grey")
C_canoinhas = canvas.create_rectangle(175, 315, 185, 325, fill="grey")
C_irati = canvas.create_rectangle(195, 55, 205, 65, fill="grey")
C_sao_mateus = canvas.create_rectangle(265, 175, 275, 185, fill="grey")
C_barras = canvas.create_rectangle(230, 230, 240, 240, fill="grey")
C_palmeira = canvas.create_rectangle(370, 55, 380, 65, fill="grey")
C_cotenda = canvas.create_rectangle(365, 140, 375, 150, fill="grey")
C_lapa = canvas.create_rectangle(345, 230, 355, 240, fill="grey")
C_mafra = canvas.create_rectangle(325, 305, 335, 315, fill="grey")
C_campo = canvas.create_rectangle(520, 55, 530, 65, fill="grey")
C_balsa = canvas.create_rectangle(445, 105, 455, 115, fill="grey")
C_araucaria = canvas.create_rectangle(470, 220, 480, 230, fill="grey")
C_tijucas = canvas.create_rectangle(455, 330, 465, 340, fill="grey")
C_sao_jose = canvas.create_rectangle(540, 270, 550, 280, fill="grey")
C_curitiba = canvas.create_rectangle(565, 205, 575, 215, fill="grey")

C = [locals()[city] for city in locals() if city.startswith('C_')]

# N = Nome / Name
N_porto = canvas.create_text(95, 200, text="Porto\nUnião", fill="black", font=('Arial', 8))
N_paulo = canvas.create_text(120, 115, text="Paulo Frontin", fill="black", font=('Arial', 8))
N_canoinhas = canvas.create_text(140, 320, text="Canoinhas", fill="black", font=('Arial', 8))
N_irati = canvas.create_text(200, 45, text="Irati", fill="black", font=('Arial', 8))
N_sao_mateus = canvas.create_text(230, 170, text="São Mateus", fill="black", font=('Arial', 8))
N_barras = canvas.create_text(195, 235, text="Três Barras", fill="black", font=('Arial', 8))
N_palmeira = canvas.create_text(375, 45, text="Palmeira", fill="black", font=('Arial', 8))
N_contenda = canvas.create_text(340, 145, text="Contenda", fill="black", font=('Arial', 8))
N_lapa = canvas.create_text(330, 235, text="Lapa", fill="black", font=('Arial', 8))
N_mafra = canvas.create_text(330, 325, text="Mafra", fill="black", font=('Arial', 8))
N_campo = canvas.create_text(525, 45, text="Campo Largo", fill="black", font=('Arial', 8))
N_balsa = canvas.create_text(425, 100, text="Balsa\nNova", fill="black", font=('Arial', 8))
N_araucaria = canvas.create_text(440, 225, text="Araucária", fill="black", font=('Arial', 8))
N_tijucas = canvas.create_text(460, 355, text="Tijucas\ndo Sul", fill="black", font=('Arial', 8))
N_sao_jose = canvas.create_text(510, 270, text="São José\ndos Pinhais", fill="black", font=('Arial', 8))
N_curitiba = canvas.create_text(600, 210, text="Curitiba", fill="black", font=('Arial', 8))

N = [locals()[name] for name in locals() if name.startswith('N_')]

# L = Linha / Line.
L_porto_paulo = canvas.create_line(120, 195, 155, 120, width=2)
L_porto_mateus = canvas.create_line(125, 200, 265, 180, width=2)
L_porto_canoinhas = canvas.create_line(120, 205, 175, 315, width=2)
L_paulo_irati = canvas.create_line(160, 110, 195, 65, width=2)
L_irati_mateus = canvas.create_line(205, 65, 265, 175, width=2)
L_irati_palmeira = canvas.create_line(205, 60, 370, 60, width=2)
L_mateus_barras = canvas.create_line(265, 185, 240, 230, width=2)
L_mateus_lapa = canvas.create_line(275, 185, 345, 230, width=2)
L_canoinhas_barras = canvas.create_line(180, 315, 235, 240, width=2)
L_canoinhas_mafra = canvas.create_line(185, 320, 325, 310, width=2)
L_lapa_mafra = canvas.create_line(350, 240, 330, 305, width=2)
L_lapa_contenda = canvas.create_line(350, 230, 370, 150, width=2)
L_palmeira_mateus = canvas.create_line(275, 175, 370, 65, width=2)
L_palmeira_campo = canvas.create_line(380, 60, 520, 60, width=2)
L_campo_balsa = canvas.create_line(520, 65, 455, 105, width=2)
L_campo_curitiba = canvas.create_line(530, 65, 570, 205, width=2)
L_contenda_balsa = canvas.create_line(375, 140, 450, 115, width=2)
L_curitiba_balsa = canvas.create_line(565, 205, 455, 115, width=2)
L_contenda_araucaria = canvas.create_line(375, 150, 470, 220, width=2)
L_curitiba_araucaria = canvas.create_line(565, 210, 480, 225, width=2)
L_curitiba_sao_jose = canvas.create_line(570, 215, 545, 270, width=2)
L_sao_jose_tijucas = canvas.create_line(545, 280, 465, 335, width=2)
L_tijucas_mafra = canvas.create_line(455, 335, 335, 310, width=2)

# L = Linha / Line.
linhas_cidades = {
    L_porto_paulo: ('Porto União', 'Paulo Frontin'),
    L_porto_mateus: ('Porto União', 'São Mateus'),
    L_porto_canoinhas: ('Porto União', 'Canoinhas'),
    L_paulo_irati: ('Paulo Frontin', 'Irati'),
    L_irati_mateus: ('Irati', 'São Mateus'),
    L_irati_palmeira: ('Irati', 'Palmeira'),
    L_mateus_barras: ('São Mateus', 'Três Barras'),
    L_mateus_lapa: ('São Mateus', '390Lapa'),
    L_canoinhas_barras: ('Canoinhas', 'Três Barras'),
    L_canoinhas_mafra: ('Canoinhas', 'Mafra'),
    L_lapa_mafra: ('Lapa', 'Mafra'),
    L_lapa_contenda: ('Lapa', 'Contenda'),
    L_palmeira_mateus: ('Palmeira', 'São Mateus'),
    L_palmeira_campo: ('Palmeira', 'Campo Largo'),
    L_campo_balsa: ('Campo Largo', 'Balsa Nova'),
    L_campo_curitiba: ('Campo Largo', 'Curitiba'),
    L_contenda_balsa: ('Contenda', 'Balsa Nova'),
    L_curitiba_balsa: ('Curitiba', 'Balsa Nova'),
    L_contenda_araucaria: ('Contenda', 'Araucária'),
    L_curitiba_araucaria: ('Curitiba', 'Araucária'),
    L_curitiba_sao_jose: ('Curitiba', 'São José dos Pinhais'),
    L_sao_jose_tijucas: ('São José dos Pinhais', 'Tijucas do Sul'),
    L_tijucas_mafra: ('Tijucas do Sul', 'Mafra')}

canvas.create_text(65, 345, text="Legenda:")
canvas.create_rectangle(0, 355, 150, 400)
canvas.create_rectangle(10, 360, 20, 370, fill='gray')
canvas.create_text(80, 365, text="Cidades não visitadas")
canvas.create_rectangle(10, 380, 20, 390, fill='green')
canvas.create_text(70, 385, text="Cidades visitadas")

janela.geometry("1100x550")
janela.mainloop()
