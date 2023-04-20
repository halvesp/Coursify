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
    "Práticas de engenharia de software": {
        "Nível de dificuldade": "Alto",
        "Pré-requisitos": ["Engenharia de software"],
        "Área de estudo": "Engenharia de software",
        "Habilidades específicas": "Desenvolvimento de software"
    },
    "Matemática": {
        "Nível de dificuldade": "Baixo",
        "Pré-requisitos": ["Nenhum"],
        "Área de estudo": "Matemática",
        "Habilidades específicas": "Desenvolvimento de software"
    },
    "Cálculo": {
        "Nível de dificuldade": "Alta",
        "Pré-requisitos": ["Matemática"],
        "Área de estudo": "Matemática",
        "Habilidades específicas": "Desenvolvimento de software"
    },
    "Álgebra linear": {
        "Nível de dificuldade": "Alta",
        "Pré-requisitos": ["Matemática"],
        "Área de estudo": "Matemática",
        "Habilidades específicas": "Desenvolvimento de software"
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

# Importa o módulo tkinter e o renomeia como "tk"
import tkinter as tk
# Importa o módulo messagebox do tkinter para exibir caixas de mensagem
from tkinter import messagebox
# Importa o módulo ttk do tkinter para utilizar temas e estilos de widget
from tkinter import ttk

# Função para remover cadeiras já cursadas da lista de cadeiras filtradas
def remover_cadeiras_cursadas(cadeiras_filtradas, cadeiras_cursadas, nenhuma_cursada):
    # Inicializa a lista de cadeiras recomendadas
    cadeiras_recomendadas = []
    # Itera sobre as cadeiras filtradas
    for cadeira in cadeiras_filtradas:
        # Verifica se a cadeira não foi cursada
        if cadeira not in cadeiras_cursadas:
            # Obtém os pré-requisitos da cadeira
            pre_requisitos = base_de_conhecimento[cadeira]["Pré-requisitos"]
             # Verifica se nenhuma cadeira foi cursada
            if nenhuma_cursada:
                # Adiciona a cadeira à lista de recomendadas se não há pré-requisitos
                if "Nenhum" in pre_requisitos:
                    cadeiras_recomendadas.append(cadeira)
            else:
                # Adiciona a cadeira à lista de recomendadas se os pré-requisitos forem atendidos
                if any(pre_requisito in cadeiras_cursadas for pre_requisito in pre_requisitos) or "Nenhum" in pre_requisitos:
                    cadeiras_recomendadas.append(cadeira)
    # Retorna a lista de cadeiras recomendadas
    return cadeiras_recomendadas


# Função para filtrar cadeiras com base nos níveis de dificuldade, áreas de estudo e habilidades específicas
def filtrar_cadeiras(niveis, areas, habilidades):
    # Inicializa a lista de cadeiras filtradas
    cadeiras_filtradas = []

    # Itera sobre todas as cadeiras no banco de conhecimento
    for cadeira in base_de_conhecimento:
        # Verifica se o nível de dificuldade da cadeira está nos níveis selecionados
        if base_de_conhecimento[cadeira]["Nível de dificuldade"] in niveis:
             # Verifica se a área de estudo e as habilidades específicas da cadeira estão nas áreas e habilidades selecionadas, ou se essas opções não foram selecionadas
            if (not areas or base_de_conhecimento[cadeira]["Área de estudo"] in areas) and (not habilidades or base_de_conhecimento[cadeira]["Habilidades específicas"] in habilidades):
                # Adiciona a cadeira à lista de cadeiras filtradas
                cadeiras_filtradas.append(cadeira)

    # Retorna a lista de cadeiras filtradas
    return cadeiras_filtradas

# Função para exibir a lista de cadeiras filtradas no widget da lista de cadeiras
def exibir_cadeiras_filtradas():
     # Inicializa as listas de níveis, áreas e habilidades com base nas opções selecionadas
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
        if var_banco_de_dados.get():
            habilidades.append("Banco de dados")
        if var_sistemas.get():
            habilidades.append("Sistemas")
    
    # Cria a lista de cadeiras cursadas com base nas opções selecionadas
    cadeiras_cursadas = [cadeira for cadeira, var in cadeiras_cursadas_vars.items() if var.get()]
    # Filtra as cadeiras com base nos níveis, áreas e habilidades
    cadeiras_filtradas = filtrar_cadeiras(niveis, areas, habilidades)
    # Remove as cadeiras já cursadas da lista de cadeiras filtradas
    cadeiras_filtradas = remover_cadeiras_cursadas(cadeiras_filtradas, cadeiras_cursadas, var_nenhuma_cursada.get())

    lista_cadeiras.delete(0, tk.END)        
    if len(cadeiras_filtradas) == 0:
        messagebox.showinfo("Resultado", "Não há cadeiras que preencham estes requisitos")
    else:
        for cadeira in cadeiras_filtradas:
            lista_cadeiras.insert(tk.END, cadeira)

# Função para redefinir todos os filtros e a lista de cadeiras exibida
def reset_filters():
    # Redefine todas as opções selecionadas
    for var in cadeiras_cursadas_vars.values():
        var.set(False)
    var_nenhuma_cursada.set(True)

    var_todos_niveis.set(True)
    var_baixo.set(False)
    var_medio.set(False)
    var_alto.set(False)

    var_areas_opcional.set(True)
    var_programacao.set(False)
    var_matematica.set(False)
    var_inteligencia.set(False)
    var_engenharia.set(False)
    var_gerenciamento.set(False)
    var_visualizacao.set(False)
    var_computabilidade.set(False)

    var_habilidades_opcional.set(True)
    var_desenvolvimento.set(False)
    var_banco_de_dados.set(False)
    var_sistemas.set(False)

    # Limpa a lista de cadeiras exibida no widget
    lista_cadeiras.delete(0, tk.END)

# Funções para atualizar as opções selecionadas com base nas ações do usuário
def atualizar_nenhuma_cursada():
    if any(var.get() for var in cadeiras_cursadas_vars.values()):
        var_nenhuma_cursada.set(False)
    else:
        var_nenhuma_cursada.set(True)

# Função para atualizar a opção "Todos os níveis" com base nas opções selecionadas
def atualizar_todos_niveis():
    if not (var_baixo.get() or var_medio.get() or var_alto.get()):
        var_todos_niveis.set(True)

# Função para desmarcar a opção "Todos os níveis" e verificar se é necessário reativá-la
def desmarcar_todos_niveis():
    var_todos_niveis.set(False)
    atualizar_todos_niveis()

# Função para atualizar a opção "Todas as habilidades" com base nas opções selecionadas
def atualizar_todas_habilidades():
    if not (var_desenvolvimento.get() or var_banco_de_dados.get() or var_sistemas.get()):
        var_habilidades_opcional.set(True)

# Função para desmarcar a opção "Todas as habilidades" e verificar se é necessário reativá-la
def desmarcar_todas_habilidades():
    var_habilidades_opcional.set(False)
    atualizar_todas_habilidades()

# Função para atualizar a opção "Todas as áreas" com base nas opções selecionadas
def atualizar_todas_areas():
    if not (var_programacao.get() or var_matematica.get() or var_inteligencia.get() or var_engenharia.get() or var_gerenciamento.get() or var_visualizacao.get() or var_computabilidade.get()):
        var_areas_opcional.set(True)

# Função para desmarcar a opção "Todas as áreas" e verificar se é necessário reativá-la
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
label_habilidades_title = tk.Label(root, text="Objetivo de carreira:")
label_habilidades_title.pack(pady=(10, 0))
check_habilidades_opcional = tk.Checkbutton(frame_habilidades, text="Todas", variable=var_habilidades_opcional)
check_habilidades_opcional.pack(side=tk.LEFT)

var_desenvolvimento = tk.BooleanVar()
check_desenvolvimento = tk.Checkbutton(frame_habilidades, text="Desenvolvimento de software", variable=var_desenvolvimento, command=desmarcar_todas_habilidades)
check_desenvolvimento.pack(side=tk.LEFT)

var_banco_de_dados = tk.BooleanVar()
check_var_banco_de_dados = tk.Checkbutton(frame_habilidades, text="Banco de dados", variable=var_banco_de_dados, command=desmarcar_todas_habilidades)
check_var_banco_de_dados.pack(side=tk.LEFT)

var_sistemas = tk.BooleanVar()
check_sistemas = tk.Checkbutton(frame_habilidades, text="Sistemas", variable=var_sistemas, command=desmarcar_todas_habilidades)
check_sistemas.pack(side=tk.LEFT)

frame_habilidades.pack(pady=10)

btn_filtrar = tk.Button(root, text="Filtrar Cadeiras", command=exibir_cadeiras_filtradas)
btn_filtrar.pack(pady=10)

btn_reset = tk.Button(root, text="Reset", command=reset_filters)
btn_reset.pack(pady=10)

lista_cadeiras = tk.Listbox(root, width=50, height=20)
lista_cadeiras.pack(pady=10)

atualizar_nenhuma_cursada()
atualizar_todos_niveis()
atualizar_todas_areas()
atualizar_todas_habilidades()

root.mainloop()
