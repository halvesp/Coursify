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

def filtrar_cadeiras(niveis, areas, habilidades):
    cadeiras_filtradas = []

    for cadeira in base_de_conhecimento:
        if base_de_conhecimento[cadeira]["Nível de dificuldade"] in niveis:
            if (not areas or base_de_conhecimento[cadeira]["Área de estudo"] in areas) and (not habilidades or base_de_conhecimento[cadeira]["Habilidades específicas"] in habilidades):
                cadeiras_filtradas.append(cadeira)

    return cadeiras_filtradas

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
    if var_todos_niveis.get():
        niveis = ["Baixo", "Médio", "Alta"]
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

    habilidades = []
    if var_habilidades_opcional.get():
        habilidades = None
    else:
        if var_desenvolvimento.get():
            habilidades.append("Desenvolvimento de software")
        if var_calculo.get():
            habilidades.append("Cálculo")
        if var_banco_de_dados.get():
            habilidades.append("Banco de dados")
        if var_sistemas.get():
            habilidades.append("Sistemas")
    
    cadeiras_cursadas = [cadeira for cadeira, var in cadeiras_cursadas_vars.items() if var.get()]
    cadeiras_filtradas = filtrar_cadeiras(niveis, areas, habilidades)
    cadeiras_filtradas = remover_cadeiras_cursadas(cadeiras_filtradas, cadeiras_cursadas, var_nenhuma_cursada.get())

    lista_cadeiras.delete(0, tk.END)
    for cadeira in cadeiras_filtradas:
        lista_cadeiras.insert(tk.END, cadeira)

def atualizar_nenhuma_cursada():
    if any(var.get() for var in cadeiras_cursadas_vars.values()):
        var_nenhuma_cursada.set(False)
    else:
        var_nenhuma_cursada.set(True)

def atualizar_todos_niveis():
    if not (var_baixo.get() or var_medio.get() or var_alto.get()):
        var_todos_niveis.set(True)

def desmarcar_todos_niveis():
    var_todos_niveis.set(False)
    atualizar_todos_niveis()

def atualizar_todas_habilidades():
    if not (var_desenvolvimento.get() or var_calculo.get() or var_banco_de_dados.get() or var_sistemas.get()):
        var_habilidades_opcional.set(True)

def desmarcar_todas_habilidades():
    var_habilidades_opcional.set(False)
    atualizar_todas_habilidades()

def atualizar_todas_areas():
    if not (var_programacao.get() or var_matematica.get() or var_inteligencia.get() or var_engenharia.get() or var_gerenciamento.get() or var_visualizacao.get() or var_computabilidade.get()):
        var_areas_opcional.set(True)

def desmarcar_todas_areas():
    var_areas_opcional.set(False)
    atualizar_todas_areas()


root = tk.Tk()
root.title("Sistema Especialista")


cadeiras_cursadas_vars = {cadeira: tk.BooleanVar() for cadeira in base_de_conhecimento}

frame_cadeiras_cursadas = tk.Frame(root)
label_cadeiras_cursadas = tk.Label(frame_cadeiras_cursadas, text="Cadeiras já cursadas:")
label_cadeiras_cursadas.grid(row=0, column=0, sticky=tk.W)

var_nenhuma_cursada = tk.BooleanVar()
check_nenhuma_cursada = tk.Checkbutton(frame_cadeiras_cursadas, text="Nenhuma", variable=var_nenhuma_cursada, command=atualizar_nenhuma_cursada)
check_nenhuma_cursada.grid(row=1, column=0, sticky=tk.W)

for index, (cadeira, var) in enumerate(cadeiras_cursadas_vars.items(), start=1):
    check_cadeira = tk.Checkbutton(frame_cadeiras_cursadas, text=cadeira, variable=var, command=atualizar_nenhuma_cursada)
    check_cadeira.grid(row=(index // 3) + 1, column=index % 3, sticky=tk.W)

frame_cadeiras_cursadas.pack(pady=10)

frame_niveis = tk.Frame(root)

var_todos_niveis = tk.BooleanVar(value=True)
label_niveis_title = tk.Label(root, text="Níveis de dificuldade:")
label_niveis_title.pack(pady=(10, 0))
check_todos_niveis = tk.Checkbutton(frame_niveis, text="Todos", variable=var_todos_niveis)
check_todos_niveis.pack(side=tk.LEFT)

var_baixo = tk.BooleanVar()
check_baixo = tk.Checkbutton(frame_niveis, text="Baixo", variable=var_baixo, command=desmarcar_todos_niveis)
check_baixo.pack(side=tk.LEFT)

var_medio = tk.BooleanVar()
check_medio = tk.Checkbutton(frame_niveis, text="Médio", variable=var_medio, command=desmarcar_todos_niveis)
check_medio.pack(side=tk.LEFT)

var_alto = tk.BooleanVar()
check_alto = tk.Checkbutton(frame_niveis, text="Alta", variable=var_alto, command=desmarcar_todos_niveis)
check_alto.pack(side=tk.LEFT)

frame_niveis.pack(pady=10)

frame_areas = tk.Frame(root)

var_areas_opcional = tk.BooleanVar(value=True)
label_areas_title = tk.Label(root, text="Áreas de conhecimento:")
label_areas_title.pack(pady=(10, 0))
check_areas_opcional = tk.Checkbutton(frame_areas, text="Todas", variable=var_areas_opcional)
check_areas_opcional.pack(side=tk.LEFT)

var_programacao = tk.BooleanVar()
check_programacao = tk.Checkbutton(frame_areas, text="Programação", variable=var_programacao, command=desmarcar_todas_areas)
check_programacao.pack(side=tk.LEFT)

var_matematica = tk.BooleanVar()
check_matematica = tk.Checkbutton(frame_areas, text="Matemática", variable=var_matematica, command=desmarcar_todas_areas)
check_matematica.pack(side=tk.LEFT)

var_inteligencia = tk.BooleanVar()
check_inteligencia = tk.Checkbutton(frame_areas, text="Inteligência artificial", variable=var_inteligencia, command=desmarcar_todas_areas)
check_inteligencia.pack(side=tk.LEFT)

var_engenharia = tk.BooleanVar()
check_engenharia = tk.Checkbutton(frame_areas, text="Engenharia de software", variable=var_engenharia, command=desmarcar_todas_areas)
check_engenharia.pack(side=tk.LEFT)

var_gerenciamento = tk.BooleanVar()
check_gerenciamento = tk.Checkbutton(frame_areas, text="Gerenciamento", variable=var_gerenciamento, command=desmarcar_todas_areas)
check_gerenciamento.pack(side=tk.LEFT)

var_visualizacao = tk.BooleanVar()
check_visualizacao = tk.Checkbutton(frame_areas, text="Visualização", variable=var_visualizacao, command=desmarcar_todas_areas)
check_visualizacao.pack(side=tk.LEFT)

var_computabilidade = tk.BooleanVar()
check_computabilidade = tk.Checkbutton(frame_areas, text="Computabilidade", variable=var_computabilidade, command=desmarcar_todas_areas)
check_computabilidade.pack(side=tk.LEFT)

frame_areas.pack(pady=10)

frame_habilidades = tk.Frame(root)

tk.Label(frame_habilidades, text="Habilidades")

var_habilidades_opcional = tk.BooleanVar(value=True)
label_habilidades_title = tk.Label(root, text="Habilidades específicas:")
label_habilidades_title.pack(pady=(10, 0))
check_habilidades_opcional = tk.Checkbutton(frame_habilidades, text="Todas", variable=var_habilidades_opcional)
check_habilidades_opcional.pack(side=tk.LEFT)

var_desenvolvimento = tk.BooleanVar()
check_desenvolvimento = tk.Checkbutton(frame_habilidades, text="Desenvolvimento de software", variable=var_desenvolvimento, command=desmarcar_todas_habilidades)
check_desenvolvimento.pack(side=tk.LEFT)

var_calculo = tk.BooleanVar()
check_calculo = tk.Checkbutton(frame_habilidades, text="Cálculo", variable=var_calculo, command=desmarcar_todas_habilidades)
check_calculo.pack(side=tk.LEFT)

var_banco_de_dados = tk.BooleanVar()
check_var_banco_de_dados = tk.Checkbutton(frame_habilidades, text="Banco de dados", variable=var_banco_de_dados, command=desmarcar_todas_habilidades)
check_var_banco_de_dados.pack(side=tk.LEFT)

var_sistemas = tk.BooleanVar()
check_sistemas = tk.Checkbutton(frame_habilidades, text="Sistemas", variable=var_sistemas, command=desmarcar_todas_habilidades)
check_sistemas.pack(side=tk.LEFT)

frame_habilidades.pack(pady=10)

btn_filtrar = tk.Button(root, text="Filtrar Cadeiras", command=exibir_cadeiras_filtradas)
btn_filtrar.pack(pady=10)

lista_cadeiras = tk.Listbox(root, width=50, height=20)
lista_cadeiras.pack(pady=10)

atualizar_nenhuma_cursada()
atualizar_todos_niveis()
atualizar_todas_areas()
atualizar_todas_habilidades()

root.mainloop()