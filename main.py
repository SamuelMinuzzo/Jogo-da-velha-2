import tkinter as tk

# Cores
azul_fraco = "#295264" 
vermelho = "#bd2f28"
bordo = "#89373d"
azul_forte = "#142433"
branco = "#ffffff"

# Janela principal
window = tk.Tk()
window.title("Jogo da Velha 2")
window.geometry("800x800")
window.configure(bg=azul_forte)

main_container = tk.Frame(window, bg=azul_forte)
main_container.pack(expand=True, fill='both')

control_frame = tk.Frame(main_container, bg=azul_forte)
control_frame.pack(side="top", pady=20)

board_wrapper = tk.Frame(main_container, bg=azul_forte)
board_wrapper.pack(expand=True)

# Tabela do jogo
tabela = [['' for _ in range(9)] for _ in range(9)]
jogando = 'X'
cont = 0
buttons = {}

# Dimensões
cell_size = 60
canvas_size = cell_size * 9

# Canvas para desenhar linhas
canvas = tk.Canvas(board_wrapper, width=canvas_size, height=canvas_size, bg=azul_forte, highlightthickness=0)
canvas.grid(row=0, column=0)

# Desenhar linhas do tabuleiro (a cada 3 células)
for i in range(1, 9):
    width = 4 if i % 3 == 0 else 1
    # Linhas horizontais
    canvas.create_line(0, i * cell_size, canvas_size, i * cell_size, fill=branco, width=width)
    # Linhas verticais
    canvas.create_line(i * cell_size, 0, i * cell_size, canvas_size, fill=branco, width=width)

# Frame para os botões sobre o canvas
buttons_frame = tk.Frame(board_wrapper, bg=azul_forte, width=canvas_size, height=canvas_size)
buttons_frame.place(x=0, y=0)

# Função de controle
def controlar(i, j):
    global jogando, cont
    if tabela[i][j] == '':
        tabela[i][j] = jogando
        btn = buttons[(i, j)]
        cor = vermelho if jogando == 'X' else azul_fraco
        btn.config(text=jogando, fg=cor, font=('Ivy', 20, 'bold'))
        cont += 1
        jogando = 'O' if jogando == 'X' else 'X'
        if cont == 81:
            print('Deu velha')

# Reiniciar o jogo
def iniciar_jogo():
    global tabela, jogando, cont
    tabela = [['' for _ in range(9)] for _ in range(9)]
    jogando = 'X'
    cont = 0
    for btn in buttons.values():
        btn.config(text='', fg=azul_forte)

# Criar botões (sobrepostos ao canvas)
for i in range(9):
    for j in range(9):
        btn = tk.Button(buttons_frame,
                        width=4, height=2,
                        text='',
                        bg=azul_forte,
                        fg=azul_forte,
                        relief='flat',
                        command=lambda i=i, j=j: controlar(i, j))
        btn.place(x=j * cell_size, y=i * cell_size, width=cell_size, height=cell_size)
        buttons[(i, j)] = btn

# Botão "Jogar"
b_jogar = tk.Button(control_frame, text='Jogar', command=iniciar_jogo,
                     font=('Ivy', 10, 'bold'), bg=bordo, fg=branco)
b_jogar.pack()

window.mainloop()
