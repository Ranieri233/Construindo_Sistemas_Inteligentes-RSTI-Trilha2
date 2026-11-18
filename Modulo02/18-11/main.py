
# importe a biblioteca tkinter com o apelido de 'tk'
import tkinter as tk

# a função TK() vem pronta da biblioteca tkinter
# cria a janela principal do nosso programa
janela = tk.Tk()

# janela.title() -> função do tkinter para dar nome a essa janela
janela.title("Minha primeira aplicação")
#janela.geometry(tamanho) -> função do tkinter para dar tamanho á janela, em pixels
janela.geometry("400x300")

# vamos criar um componente de texto
texto = tk.Label(
    janela, # em que tela ele aparece
    text = " Seja bem-vindo(a)", # qual o texto e o tamanho
    font = ("Arial", 14), # qual a fonte de texto e o tamanho
    fg = "blue" # qual a cor do texto
)

texto.pack(pady=20)

entrada = tk.Entry(
    janela, # em qual tela ele vai
    width=30
)

entrada.pack(pady=10)

def exibir_mensagem():
    print(f'Texto: {entrada.get()}')


botao = tk.Button(
    janela,
    text="Clique aqui",
    command=exibir_mensagem
)

botao.pack(pady=10)


# janela.mainloop() é uma função que mantém a nossa aplicação em execução, aguardando alguma ação nossa
janela.mainloop()




