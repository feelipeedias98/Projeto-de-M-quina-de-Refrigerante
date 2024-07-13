import tkinter as tk
from tkinter import simpledialog, messagebox

def exibir_menu():
    # Cria a lista de produtos com preços
    lista = [
        (1, "Coca Cola R$3,50", 3.50),
        (2, "Pepsi R$3,50", 3.50),
        (3, "Guaraná R$3,50", 3.50),
        (4, "Sprite R$3,50", 3.50),
        (5, "Fanta Laranja R$3,50", 3.50)
    ]
    
    # Cria a janela principal
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    
    # Exibe a lista de produtos em uma caixa de diálogo
    menu_text = "Aqui está a lista de produtos:\n\n"
    for numero, nome, _ in lista:
        menu_text += f"{numero}: {nome}\n"
    
    messagebox.showinfo("Menu de Produtos", menu_text)
    return lista

def selecionar_produto(lista_de_produtos):
    # Pergunta ao usuário para selecionar um produto
    select = simpledialog.askinteger("Seleção de Produto", "Por favor selecione o seu refrigerante:\n")
    
    # Encontra o produto selecionado na lista de produtos
    produto_selecionado = None
    for numero, nome, preco in lista_de_produtos:
        if select == numero:
            produto_selecionado = (nome, preco)
            break
    
    return produto_selecionado

def realizar_pagamento(valor_produto):
    # Solicita o pagamento
    pag = simpledialog.askfloat("Pagamento", f"Realize o pagamento para liberar o produto (R${valor_produto}):\n")
    return pag

# Executa o menu e armazena a lista de produtos
lista_de_produtos = exibir_menu()

if lista_de_produtos:
    produto_selecionado = selecionar_produto(lista_de_produtos)
    
    if produto_selecionado:
        nome_produto, valor_produto = produto_selecionado
        messagebox.showinfo("Produto Selecionado", f"Você selecionou: {nome_produto}")

        # Realiza o pagamento
        pag = realizar_pagamento(valor_produto)

        # Calcula o troco
        result = pag - valor_produto

        # Verifica se o pagamento é suficiente
        if pag >= valor_produto:
            if pag > valor_produto:
                messagebox.showinfo("Troco", f"Seu troco é de R${result}. Seu produto será liberado em alguns segundos!")
            messagebox.showinfo("Obrigado", "Obrigado pela preferência! Volte sempre!")
        else:
            messagebox.showwarning("Pagamento Insuficiente", "Pagamento insuficiente. Por favor, insira o valor correto.")
    else:
        messagebox.showerror("Erro", "Produto selecionado não encontrado.")
else:
    messagebox.showinfo("Nenhum Produto", "Nenhum produto foi selecionado.")
