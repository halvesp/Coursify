import tkinter as tk
from tkinter import ttk

def remover_cadeiras_cursadas(cadeiras_filtradas, cadeiras_cursadas, nenhuma_cursada):
    cadeiras_recomendadas = []
    for cadeira in cadeiras_filtradas:
        if cadeira not in cadeiras_cursadas:
            pre_requisitos = base_de_conhecimento[cadeira]["Pré-requisitos"]
            if nenhuma_cursada:
                if "Nenhum" in pre_requisitos:
                    cadeiras_recomendadas.append(cadeira)
            else:
                if any(pre_requisito in cadeiras_cursadas for pre_requisito in pre_requisitos) or "Nenhum" in pre_requisitos:
                    cadeiras_recomendadas.append(cadeira)
    return cadeiras_recomendadas

# Função para filtrar as cadeiras por nível de dificuldade
def filtrar_cadeiras(niveis, areas):
    cadeiras_filtradas = []

    for cadeira in base_de_conhecimento:
        if base_de_conhecimento[cadeira]["Nível de dificuldade"] in niveis and base_de_conhecimento[cadeira]["Área de estudo"] in areas:
            cadeiras_filtradas.append(cadeira)

    return cadeiras_filtradas

# Função para exibir cadeiras filtradas na interface gráfica
def exibir_cadeiras_filtradas():
    niveis = []
    if var_baixo.get():
        niveis.append("Baixo")
    if var_medio.get():
        niveis.append("Médio")
    if var_alto.get():
        niveis.append("Alta")

    cadeiras_cursadas = [cadeira for cadeira, var in cadeiras_cursadas_vars.items() if var.get()]
    cadeiras_filtradas = filtrar_cadeiras(niveis)
    cadeiras_filtradas = remover_cadeiras_cursadas(cadeiras_filtradas, cadeiras_cursadas, var_nenhuma_cursada.get())

    lista_cadeiras.delete(0, tk.END)
    for cadeira in cadeiras_filtradas:
        lista_cadeiras.insert(tk.END, cadeira)
def exibir_cadeiras_filtradas():
    niveis = []
    if var_baixo.get():
        niveis.append("Baixo")
    if var_medio.get():
        niveis.append("Médio")
    if var_alto.get():
        niveis.append("Alta")

    areas = []
    if var_programacao.get():
        areas.append("Programação")
    if var_matematica.get():
        areas.append("Matemática")
    if var_inteligencia.get():
        areas.append("Inteligência artificial")
    if var_engenharia.get():
        areas.append("Engenharia de software")
    if var_gerenciamento.get():
        areas.append("Gerenciamento")
    if var_visualizacao.get():
        areas.append("Visualização")
    if var_computabilidade.get():
        areas.append("Computabilidade")

    cadeiras_cursadas = [cadeira for cadeira, var in cadeiras_cursadas_vars.items() if var.get()]
    cadeiras_filtradas = filtrar_cadeiras(niveis, areas)
    cadeiras_filtradas = remover_cadeiras_cursadas(cadeiras_filtradas, cadeiras_cursadas, var_nenhuma_cursada.get())

    lista_cadeiras.delete(0, tk.END)
    for cadeira in cadeiras_filtradas:
        lista_cadeiras.insert(tk.END, cadeira)

# Base de conhecimento
base_de_conhecimento = {
    "Algoritmos e lógica de programação": {
        "Nível de dificuldade": "Baixo",
        "Pré-requisitos": ["Nenhum"],
        "Área de estudo": "Programação",
        "Habilidades específicas": "Desenvolvimento de software"
    },
    "Estruturas de dados": {
        "Nível de dificuldade": "Alta",
        "Pré-requisitos": ["Algoritmos e lógica de programação"],
        "Área de estudo": "Programação",
        "Habilidades específicas": "Desenvolvimento de software"
    },

    "Teoria da computação": {
        "Nível de dificuldade": "Baixo",
        "Pré-requisitos": ["Nenhum"],
        "Área de estudo": "Computabilidade",
        "Habilidades específicas": "Desenvolvimento de software"
    },
    "Inteligência artificial": {
        "Nível de dificuldade": "Alta",
        "Pré-requisitos": ["Estruturas de dados", "Programação orientada a objetos"],
        "Área de estudo": "Inteligência artificial",
        "Habilidades específicas": "Desenvolvimento de software"
    },
    "Engenharia de software": {
        "Nível de dificuldade": "Médio",
        "Pré-requisitos": ["Programação orientada a objetos", "Estruturas de dados"],
        "Área de estudo": "Engenharia de software",
        "Habilidades específicas": "Desenvolvimento de software"
    },
    "Matemática": {
        "Nível de dificuldade": "Baixo",
        "Pré-requisitos": ["Nenhum"],
        "Área de estudo": "Matemática",
        "Habilidades específicas": "Cálculo"
    },
    "Cálculo": {
        "Nível de dificuldade": "Alta",
        "Pré-requisitos": ["Matemática"],
        "Área de estudo": "Matemática",
        "Habilidades específicas": "Cálculo"
    },
    "Álgebra linear": {
        "Nível de dificuldade": "Alta",
        "Pré-requisitos": ["Matemática"],
        "Área de estudo": "Matemática",
        "Habilidades específicas": "Cálculo"
    },
    "Sistemas operacionais": {
        "Nível de dificuldade": "Baixo",
        "Pré-requisitos": ["Nenhum"],
        "Área de estudo": "Computabilidade",
        "Habilidades específicas": "Sistemas"
    },
    "Arquitetura de computadores": {
        "Nível de dificuldade": "Baixo",
        "Pré-requisitos": ["Nenhum"],
        "Área de estudo": "Computabilidade",
        "Habilidades específicas": "Sistemas"
    },
    "Banco de dados": {
        "Nível de dificuldade": "Médio",
        "Pré-requisitos": ["Algoritmos e lógica de programação", "Programação orientada a objetos", "Estrutura de dados"],
        "Área de estudo": "Gerenciamento",
        "Habilidades específicas": "Banco de dados"
    },
    "Redes de computadores": {
        "Nível de dificuldade": "Médio",
        "Pré-requisitos": ["Arquitetura de computadores", "Sistemas operacionais"],
        "Área de estudo": "Computabilidade",
        "Habilidades específicas": "Sistemas"
    },  
    "Computação gráfica": {
        "Nível de dificuldade": "Alta",
        "Pré-requisitos": ["Estruturas de dados", "Programação orientada a objetos"],
        "Área de estudo": "Visualização",
        "Habilidades específicas": "Desenvolvimento de software"
    },
    "Programação orientada a objetos": {
        "Nível de dificuldade": "Médio",
        "Pré-requisitos": ["Algoritmos e lógica de programação"],
        "Área de estudo": "Programação",
        "Habilidades específicas": "Desenvolvimento de software"
    },
    "Programação web": {
        "Nível de dificuldade": "Médio",
        "Pré-requisitos": ["Estruturas de dados", "Programação orientada a objetos"],
        "Área de estudo": "Programação",
        "Habilidades específicas": "Desenvolvimento de software"
    },
    "Programação para dispositivos móveis": {
        "Nível de dificuldade": "Médio",
        "Pré-requisitos": ["Estruturas de dados", "Programação orientada a objetos"],
        "Área de estudo": "Programação",
        "Habilidades específicas": "Desenvolvimento de software"
    },
    "Engenharia de dados": {
        "Nível de dificuldade": "Alta",
        "Pré-requisitos": ["Banco de dados", "Inteligência artificial"],
        "Área de estudo": "Gerenciamento",
        "Habilidades específicas": "Banco de dados"
    },
    "Jogos digitais": {
        "Nível de dificuldade": "Médio",
        "Pré-requisitos": ["Computação gráfica", "Programação Orientada a Objetos"],
        "Área de estudo": "Visualização",
        "Habilidades específicas": "Desenvolvimento de software"    
    },
}

# Criando a interface gráfica
root = tk.Tk()
root.title("Sistema Especialista")

# Crie um dicionário para armazenar as variáveis BooleanVar das disciplinas já cursadas
cadeiras_cursadas_vars = {cadeira: tk.BooleanVar() for cadeira in base_de_conhecimento}

frame_cadeiras_cursadas = tk.Frame(root)
label_cadeiras_cursadas = tk.Label(frame_cadeiras_cursadas, text="Cadeiras já cursadas:")
label_cadeiras_cursadas.grid(row=0, column=0, sticky=tk.W)

var_nenhuma_cursada = tk.BooleanVar()
check_nenhuma_cursada = tk.Checkbutton(frame_cadeiras_cursadas, text="Nenhuma", variable=var_nenhuma_cursada)
check_nenhuma_cursada.grid(row=1, column=0, sticky=tk.W)

for index, (cadeira, var) in enumerate(cadeiras_cursadas_vars.items(), start=1):
    check_cadeira = tk.Checkbutton(frame_cadeiras_cursadas, text=cadeira, variable=var)
    check_cadeira.grid(row=(index // 3) + 1, column=index % 3, sticky=tk.W)

frame_cadeiras_cursadas.pack(pady=10)

# Criando os elementos da interface
frame_niveis = tk.Frame(root)
var_baixo = tk.BooleanVar()
check_baixo = tk.Checkbutton(frame_niveis, text="Baixo", variable=var_baixo)
check_baixo.pack(side=tk.LEFT)
var_medio = tk.BooleanVar()
check_medio = tk.Checkbutton(frame_niveis, text="Médio", variable=var_medio)
check_medio.pack(side=tk.LEFT)
var_alto = tk.BooleanVar()
check_alto = tk.Checkbutton(frame_niveis, text="Alta", variable=var_alto)
check_alto.pack(side=tk.LEFT)

frame_niveis.pack(pady=10)

frame_areas = tk.Frame(root)
var_programacao = tk.BooleanVar()
check_programacao = tk.Checkbutton(frame_areas, text="Programação", variable=var_programacao)
check_programacao.pack(side=tk.LEFT)
var_matematica = tk.BooleanVar()
check_matematica = tk.Checkbutton(frame_areas, text="Matemática", variable=var_matematica)
check_matematica.pack(side=tk.LEFT)
var_inteligencia = tk.BooleanVar()
check_inteligencia = tk.Checkbutton(frame_areas, text="Inteligência artificial", variable=var_inteligencia)
check_inteligencia.pack(side=tk.LEFT)
var_engenharia = tk.BooleanVar()
check_engenharia = tk.Checkbutton(frame_areas, text="Engenharia de software", variable=var_engenharia)
check_engenharia.pack(side=tk.LEFT)
var_gerenciamento = tk.BooleanVar()
check_gerenciamento = tk.Checkbutton(frame_areas, text="Gerenciamento", variable=var_gerenciamento)
check_gerenciamento.pack(side=tk.LEFT)
var_visualizacao = tk.BooleanVar()
check_visualizacao = tk.Checkbutton(frame_areas, text="Visualização", variable=var_visualizacao)
check_visualizacao.pack(side=tk.LEFT)
var_computabilidade = tk.BooleanVar()
check_computabilidade = tk.Checkbutton(frame_areas, text="Computabilidade", variable=var_computabilidade)
check_computabilidade.pack(side=tk.LEFT)

frame_areas.pack(pady=10)

btn_filtrar = tk.Button(root, text="Filtrar Cadeiras", command=exibir_cadeiras_filtradas)
btn_filtrar.pack(pady=10)

lista_cadeiras = tk.Listbox(root, width=50, height=20)
lista_cadeiras.pack(pady=10)


# Iniciando a interface gráfica
root.mainloop()