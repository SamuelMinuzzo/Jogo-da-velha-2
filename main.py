from tkinter import *

#cores
azul_fraco = "#295264" 
bege = "#fad9a6"
vermelho = "#bd2f28"
bordo = "#89373d"
azul_forte = "#142433"
branco = "#ffffff"

window = Tk()
window.title("Jogo da Velha 2")
window.geometry("1720x900")
window.configure(bg=azul_forte)


frame_principal = Frame(window, width=1720, height=900, bg=azul_forte, relief='flat')
frame_principal.grid(row=1, column=0, sticky=NW)

#lógica do jogo
jogador_1 = 'X'
jogador_2 = 'O'

tabela = [['','','','','','','','',''],
          ['','','','','','','','',''],
          ['','','','','','','','',''],
          ['','','','','','','','',''],
          ['','','','','','','','',''],
          ['','','','','','','','',''],
          ['','','','','','','','',''],
          ['','','','','','','','',''],
          ['','','','','','','','','']]

jogando = 'X'
jogar = ''
cont = 0


def iniciar_jogo():

    def controlar(i,j,bt):
        global jogando
        global cont
        global jogar
        cor = vermelho
        
        
        if tabela[i-1][j-1] == '':
            tabela[i-1][j-1] = jogando
            bt['fg'] = cor
            bt['text'] = jogando
            bt['font'] = ('Ivy', 20, 'bold')  
            bt['width'] = 3 
            bt['height'] = 1
            if jogando == 'X':
                jogar = 'O'
                jogando = 'O'
                cor = azul_fraco
            else:
                jogar = 'X'
                jogando = 'X'
                cor = vermelho
            cont += 1
            #verificar_vitoria()
            if cont == 81:
                print('Deu velha')


    def vencedor():
        pass


    def terminar():
        pass


    #Linhas principais vertical
    app_ = Label(frame_principal, text='',width=2,height=107,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=730,y=64)
    app_ = Label(frame_principal, text='',width=2,height=107,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=987,y=64)

    #Linhas principais horizontal
    app_ = Label(frame_principal, text='',width=190,relief='flat',padx=2,pady=1,anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=474,y=311)
    app_ = Label(frame_principal, text='',width=190,relief='flat',padx=2,pady=1,anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=474,y=568)

    #Linhas secundarias vertical
    app_ = Label(frame_principal, text='',height=25,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco, fg=azul_forte)
    app_.place(x=563,y=90)
    app_ = Label(frame_principal, text='',height=25,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=627,y=90)
    app_ = Label(frame_principal, text='',height=25,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco, fg=azul_forte)
    app_.place(x=820,y=90)
    app_ = Label(frame_principal, text='',height=25,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=884,y=90)
    app_ = Label(frame_principal, text='',height=25,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco, fg=azul_forte)
    app_.place(x=1077,y=90)
    app_ = Label(frame_principal, text='',height=25,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=1141,y=90)

    app_ = Label(frame_principal, text='',height=25,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco, fg=azul_forte)
    app_.place(x=563,y=359)
    app_ = Label(frame_principal, text='',height=25,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=627,y=359)
    app_ = Label(frame_principal, text='',height=25,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco, fg=azul_forte)
    app_.place(x=820,y=359)
    app_ = Label(frame_principal, text='',height=25,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=884,y=359)
    app_ = Label(frame_principal, text='',height=25,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco, fg=azul_forte)
    app_.place(x=1077,y=359)
    app_ = Label(frame_principal, text='',height=25,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=1141,y=359)

    app_ = Label(frame_principal, text='',height=25,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco, fg=azul_forte)
    app_.place(x=563,y=628)
    app_ = Label(frame_principal, text='',height=25,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=627,y=628)
    app_ = Label(frame_principal, text='',height=25,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco, fg=azul_forte)
    app_.place(x=820,y=628)
    app_ = Label(frame_principal, text='',height=25,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=884,y=628)
    app_ = Label(frame_principal, text='',height=25,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco, fg=azul_forte)
    app_.place(x=1077,y=628)
    app_ = Label(frame_principal, text='',height=25,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=1141,y=628)



    #Linhas secundarias horizontal
    app_ = Label(frame_principal, text='',width=45,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=503,y=147)
    app_ = Label(frame_principal, text='',width=45,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=503,y=208)
    app_ = Label(frame_principal, text='',width=45,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=760,y=147)
    app_ = Label(frame_principal, text='',width=45,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=760,y=208)
    app_ = Label(frame_principal, text='',width=45,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=1017,y=147)
    app_ = Label(frame_principal, text='',width=45,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=1017,y=208)

    app_ = Label(frame_principal, text='',width=45,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=503,y=417)
    app_ = Label(frame_principal, text='',width=45,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=503,y=478)
    app_ = Label(frame_principal, text='',width=45,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=760,y=417)
    app_ = Label(frame_principal, text='',width=45,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=760,y=478)
    app_ = Label(frame_principal, text='',width=45,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=1017,y=417)
    app_ = Label(frame_principal, text='',width=45,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=1017,y=478)

    app_ = Label(frame_principal, text='',width=45,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=503,y=687)
    app_ = Label(frame_principal, text='',width=45,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=503,y=748)
    app_ = Label(frame_principal, text='',width=45,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=760,y=687)
    app_ = Label(frame_principal, text='',width=45,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=760,y=748)
    app_ = Label(frame_principal, text='',width=45,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=1017,y=687)
    app_ = Label(frame_principal, text='',width=45,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=branco,fg=azul_forte)
    app_.place(x=1017,y=748)

    #Botões
    #legenda b_linha-grande_ linha-menor_posição
    #Linha 1 - 1
    b_1_1_1 = Button(frame_principal,command=lambda:controlar(1,1,b_1_1_1) ,text='',width=13,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_1_1.place(x=503,y=90)
    b_1_1_2 = Button(frame_principal,command=lambda:controlar(1,2,b_1_1_2) ,text='',width=11,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_1_2.place(x=569,y=90)
    b_1_1_3 = Button(frame_principal,command=lambda:controlar(1,3,b_1_1_3) ,text='',width=13,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_1_3.place(x=634,y=90)
    b_1_1_4 = Button(frame_principal,command=lambda:controlar(1,4,b_1_1_4) ,text='',width=13,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_1_4.place(x=760,y=90)
    b_1_1_5 = Button(frame_principal,command=lambda:controlar(1,5,b_1_1_5) ,text='',width=11,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_1_5.place(x=826,y=90)
    b_1_1_6 = Button(frame_principal,command=lambda:controlar(1,6,b_1_1_6) ,text='',width=13,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_1_6.place(x=891,y=90)
    b_1_1_7 = Button(frame_principal,command=lambda:controlar(1,7,b_1_1_7) ,text='',width=13,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_1_7.place(x=1017,y=90)
    b_1_1_8 = Button(frame_principal,command=lambda:controlar(1,8,b_1_1_8) ,text='',width=11,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_1_8.place(x=1083,y=90)
    b_1_1_9 = Button(frame_principal,command=lambda:controlar(1,9,b_1_1_9) ,text='',width=13,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_1_9.place(x=1148,y=90)


    #Linha 1 - 2
    b_1_2_1 = Button(frame_principal,command=lambda:controlar(2,1,b_1_2_1) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_2_1.place(x=503,y=157)
    b_1_2_2 = Button(frame_principal,command=lambda:controlar(2,2,b_1_2_2) ,text='',width=11,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_2_2.place(x=569,y=157)
    b_1_2_3 = Button(frame_principal,command=lambda:controlar(2,3,b_1_2_3) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_2_3.place(x=634,y=157)
    b_1_2_4 = Button(frame_principal,command=lambda:controlar(2,4,b_1_2_4) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_2_4.place(x=760,y=157)
    b_1_2_5 = Button(frame_principal,command=lambda:controlar(2,5,b_1_2_5) ,text='',width=11,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_2_5.place(x=826,y=157)
    b_1_2_6 = Button(frame_principal,command=lambda:controlar(2,6,b_1_2_6) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_2_6.place(x=891,y=157)
    b_1_2_7 = Button(frame_principal,command=lambda:controlar(2,7,b_1_2_7) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_2_7.place(x=1017,y=157)
    b_1_2_8 = Button(frame_principal,command=lambda:controlar(2,8,b_1_2_8) ,text='',width=11,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_2_8.place(x=1083,y=157)
    b_1_2_9 = Button(frame_principal,command=lambda:controlar(2,9,b_1_2_9) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_2_9.place(x=1148,y=157)



    #Linha 1 - 3
    b_1_3_1 = Button(frame_principal,command=lambda:controlar(3,1,b_1_3_1) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_3_1 .place(x=503,y=218)
    b_1_3_2 = Button(frame_principal,command=lambda:controlar(3,2,b_1_3_2) ,text='',width=11,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_3_2 .place(x=569,y=218)
    b_1_3_3 = Button(frame_principal,command=lambda:controlar(3,3,b_1_3_3) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_3_3 .place(x=634,y=218)
    b_1_3_4 = Button(frame_principal,command=lambda:controlar(3,4,b_1_3_4) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_3_4.place(x=760,y=218)
    b_1_3_5 = Button(frame_principal,command=lambda:controlar(3,5,b_1_3_5) ,text='',width=11,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_3_5.place(x=826,y=218)
    b_1_3_6 = Button(frame_principal,command=lambda:controlar(3,6,b_1_3_6) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_3_6.place(x=891,y=218)
    b_1_3_7 = Button(frame_principal,command=lambda:controlar(3,7,b_1_3_7) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_3_7.place(x=1017,y=218)
    b_1_3_8 = Button(frame_principal,command=lambda:controlar(3,8,b_1_3_8) ,text='',width=11,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_3_8.place(x=1083,y=218)
    b_1_3_9 = Button(frame_principal,command=lambda:controlar(3,9,b_1_3_9) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_1_3_9.place(x=1148,y=218)


    #Linha 2 - 1
    b_2_1_1 = Button(frame_principal,command=lambda:controlar(4,1,b_2_1_1) ,text='',width=13,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_1_1.place(x=503,y=359)
    b_2_1_2 = Button(frame_principal,command=lambda:controlar(4,2,b_2_1_2) ,text='',width=11,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_1_2.place(x=569,y=359)
    b_2_1_3 = Button(frame_principal,command=lambda:controlar(4,3,b_2_1_3) ,text='',width=13,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_1_3.place(x=634,y=359)
    b_2_1_4 = Button(frame_principal,command=lambda:controlar(4,4,b_2_1_4) ,text='',width=13,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_1_4.place(x=760,y=359)
    b_2_1_5 = Button(frame_principal,command=lambda:controlar(4,5,b_2_1_5) ,text='',width=11,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_1_5.place(x=826,y=359)
    b_2_1_6 = Button(frame_principal,command=lambda:controlar(4,6,b_2_1_6) ,text='',width=13,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_1_6.place(x=891,y=359)
    b_2_1_7 = Button(frame_principal,command=lambda:controlar(4,7,b_2_1_7) ,text='',width=13,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_1_7.place(x=1017,y=359)
    b_2_1_8 = Button(frame_principal,command=lambda:controlar(4,8,b_2_1_8) ,text='',width=11,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_1_8.place(x=1083,y=359)
    b_2_1_9 = Button(frame_principal,command=lambda:controlar(4,9,b_2_1_9) ,text='',width=13,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_1_9.place(x=1148,y=359)

    #Linha 2 - 2
    b_2_2_1 = Button(frame_principal,command=lambda:controlar(5,1,b_2_2_1) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_2_1.place(x=503,y=426)
    b_2_2_2 = Button(frame_principal,command=lambda:controlar(5,2,b_2_2_2) ,text='',width=11,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_2_2.place(x=569,y=426)
    b_2_2_3 = Button(frame_principal,command=lambda:controlar(5,3,b_2_2_3) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_2_3.place(x=634,y=426)
    b_2_2_4 = Button(frame_principal,command=lambda:controlar(5,4,b_2_2_4) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_2_4.place(x=760,y=426)
    b_2_2_5 = Button(frame_principal,command=lambda:controlar(5,5,b_2_2_5) ,text='',width=11,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_2_5.place(x=826,y=426)
    b_2_2_6 = Button(frame_principal,command=lambda:controlar(5,6,b_2_2_6) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_2_6.place(x=891,y=426)
    b_2_2_7 = Button(frame_principal,command=lambda:controlar(5,7,b_2_2_7) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_2_7.place(x=1017,y=426)
    b_2_2_8 = Button(frame_principal,command=lambda:controlar(5,8,b_2_2_8) ,text='',width=11,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_2_8.place(x=1083,y=426)
    b_2_2_9 = Button(frame_principal,command=lambda:controlar(5,9,b_2_2_9) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_2_9.place(x=1148,y=426)



    #Linha 2 - 3
    b_2_3_1 = Button(frame_principal,command=lambda:controlar(6,1,b_2_3_1) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_3_1 .place(x=503,y=487)
    b_2_3_2 = Button(frame_principal,command=lambda:controlar(6,2,b_2_3_2) ,text='',width=11,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_3_2 .place(x=569,y=487)
    b_2_3_3 = Button(frame_principal,command=lambda:controlar(6,3,b_2_3_3) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_3_3 .place(x=634,y=487)
    b_2_3_4 = Button(frame_principal,command=lambda:controlar(6,4,b_2_3_4) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_3_4.place(x=760,y=487)
    b_2_3_5 = Button(frame_principal,command=lambda:controlar(6,5,b_2_3_5) ,text='',width=11,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_3_5.place(x=826,y=487)
    b_2_3_6 = Button(frame_principal,command=lambda:controlar(6,6,b_2_3_6) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_3_6.place(x=891,y=487)
    b_2_3_7 = Button(frame_principal,command=lambda:controlar(6,7,b_2_3_7) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_3_7.place(x=1017,y=487)
    b_2_3_8 = Button(frame_principal,command=lambda:controlar(6,8,b_2_3_8) ,text='',width=11,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_3_8.place(x=1083,y=487)
    b_2_3_9 = Button(frame_principal,command=lambda:controlar(6,9,b_2_3_9) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_2_3_9.place(x=1148,y=487)

    #Linha 3 - 1
    b_3_1_1 = Button(frame_principal,command=lambda:controlar(7,1,b_3_1_1) ,text='',width=13,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_1_1.place(x=503,y=628)
    b_3_1_2 = Button(frame_principal,command=lambda:controlar(7,2,b_3_1_2) ,text='',width=11,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_1_2.place(x=569,y=628)
    b_3_1_3 = Button(frame_principal,command=lambda:controlar(7,3,b_3_1_3) ,text='',width=13,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_1_3.place(x=634,y=628)
    b_3_1_4 = Button(frame_principal,command=lambda:controlar(7,4,b_3_1_4) ,text='',width=13,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_1_4.place(x=760,y=628)
    b_3_1_5 = Button(frame_principal,command=lambda:controlar(7,5,b_3_1_5) ,text='',width=11,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_1_5.place(x=826,y=628)
    b_3_1_6 = Button(frame_principal,command=lambda:controlar(7,6,b_3_1_6) ,text='',width=13,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_1_6.place(x=891,y=628)
    b_3_1_7 = Button(frame_principal,command=lambda:controlar(7,7,b_3_1_7) ,text='',width=13,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_1_7.place(x=1017,y=628)
    b_3_1_8 = Button(frame_principal,command=lambda:controlar(7,8,b_3_1_8) ,text='',width=11,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_1_8.place(x=1083,y=628)
    b_3_1_9 = Button(frame_principal,command=lambda:controlar(7,9,b_3_1_9) ,text='',width=13,height=8,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_1_9.place(x=1148,y=628)

    #Linha 3 - 2
    b_3_2_1 = Button(frame_principal,command=lambda:controlar(8,1,b_3_2_1) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_2_1.place(x=503,y=695)
    b_3_2_2 = Button(frame_principal,command=lambda:controlar(8,2,b_3_2_2) ,text='',width=11,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_2_2.place(x=569,y=695)
    b_3_2_3 = Button(frame_principal,command=lambda:controlar(8,3,b_3_2_3) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_2_3.place(x=634,y=695)
    b_3_2_4 = Button(frame_principal,command=lambda:controlar(8,4,b_3_2_4) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_2_4.place(x=760,y=695)
    b_3_2_5 = Button(frame_principal,command=lambda:controlar(8,5,b_3_2_5) ,text='',width=11,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_2_5.place(x=826,y=695)
    b_3_2_6 = Button(frame_principal,command=lambda:controlar(8,6,b_3_2_6) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_2_6.place(x=891,y=695)
    b_3_2_7 = Button(frame_principal,command=lambda:controlar(8,7,b_3_2_7) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_2_7.place(x=1017,y=695)
    b_3_2_8 = Button(frame_principal,command=lambda:controlar(8,8,b_3_2_8) ,text='',width=11,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_2_8.place(x=1083,y=695)
    b_3_2_9 = Button(frame_principal,command=lambda:controlar(8,9,b_3_2_9) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_2_9.place(x=1148,y=695)



    #Linha 3 - 3
    b_3_3_1 = Button(frame_principal,command=lambda:controlar(9,1,b_3_3_1) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_3_1.place(x=503,y=756)
    b_3_3_2 = Button(frame_principal,command=lambda:controlar(9,2,b_3_3_2) ,text='',width=11,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_3_2.place(x=569,y=756)
    b_3_3_3 = Button(frame_principal,command=lambda:controlar(9,3,b_3_3_3) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_3_3.place(x=634,y=756)
    b_3_3_4 = Button(frame_principal,command=lambda:controlar(9,4,b_3_3_4) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_3_4.place(x=760,y=756)
    b_3_3_5 = Button(frame_principal,command=lambda:controlar(9,5,b_3_3_5) ,text='',width=11,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_3_5.place(x=826,y=756)
    b_3_3_6 = Button(frame_principal,command=lambda:controlar(9,6,b_3_3_6) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_3_6.place(x=891,y=756)
    b_3_3_7 = Button(frame_principal,command=lambda:controlar(9,7,b_3_3_7) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_3_7.place(x=1017,y=756)
    b_3_3_8 = Button(frame_principal,command=lambda:controlar(9,8,b_3_3_8) ,text='',width=11,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_3_8.place(x=1083,y=756)
    b_3_3_9 = Button(frame_principal,command=lambda:controlar(9,9,b_3_3_9) ,text='',width=13,height=7,relief='flat',anchor='center',font=('Ivy 5 bold'),bg=azul_forte,fg=azul_forte)
    b_3_3_9.place(x=1148,y=756)

b_jogar = Button(frame_principal, command=iniciar_jogo,text='Jogar',width=7,height=2,relief='flat',anchor='center',font = ('Ivy 10 bold'),bg=bordo,fg=branco)
b_jogar.place(x=826,y=850)


window.mainloop()