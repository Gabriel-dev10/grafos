import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.widgets import Button

 
def CriaArvoreBinaria(vetor, item, inicio=0, fim=None, posicao=(0, 0), dx=4, graph=None, parent=None, node_colors=None):
    if fim is None:
        fim = len(vetor) - 1

    if graph is None:
        graph = nx.DiGraph()
        node_colors = {}

    if inicio <= fim:
        indice = (inicio + fim) // 2
        valor_meio = vetor[indice]
        node_label = valor_meio

        graph.add_node(node_label, pos=posicao)

        if item == valor_meio:
            node_colors[node_label] = 'green' 
        else:
            node_colors[node_label] = 'red'  

        if parent is not None:
            graph.add_edge(parent, node_label)

        dx /= 2
        CriaArvoreBinaria(vetor, item, inicio, indice - 1, (posicao[0] - dx, posicao[1] - 1), dx, graph, node_label, node_colors)
        CriaArvoreBinaria(vetor, item, indice + 1, fim, (posicao[0] + dx, posicao[1] - 1), dx, graph, node_label, node_colors)

    return graph, node_colors




def ExibirArvoreBinaria(graph, node_colors, visitados):
    passo_atual = -1  

    pos = nx.get_node_attributes(graph, 'pos')
    fig, ax = plt.subplots()
    color_map = ['gray'] * len(graph.nodes())
    labels = {node: node for node in graph.nodes()}

    def atualizar_cor():
        nonlocal color_map
        color_map = ['gray'] * len(graph.nodes())
        for i in range(min(passo_atual + 1, len(visitados))):
            color_map[list(graph.nodes()).index(visitados[i])] = 'green' if i == passo_atual else 'red'
        ax.clear()
        nx.draw(graph, pos, ax=ax, with_labels=True, node_size=2000, node_color=color_map, labels=labels, font_size=8, font_weight='bold')

    
    def avancar(event):
        nonlocal passo_atual
        if passo_atual < len(visitados) - 1:
            passo_atual += 1
            atualizar_cor()
            plt.draw()

   
    def retroceder(event):
        nonlocal passo_atual
        if passo_atual > 0:
            passo_atual -= 1
            atualizar_cor()
            plt.draw()

    
    ax_avancar = plt.axes([0.8, 0.01, 0.1, 0.075])
    ax_retroceder = plt.axes([0.6, 0.01, 0.1, 0.075])
    botao_avancar = Button(ax_avancar, 'Avançar')
    botao_retroceder = Button(ax_retroceder, 'Voltar')

    botao_avancar.on_clicked(avancar)
    botao_retroceder.on_clicked(retroceder)

    atualizar_cor()  
    plt.show()


    

def PesquisaBtn(vetor, item):
    inicio = 0
    fim = len(vetor) - 1
    visitados = [] 

    while inicio <= fim:
        indice = (inicio + fim) // 2
        valor_meio = vetor[indice]
        visitados.append(valor_meio)  
        print(f"Analisando o valor: {valor_meio}")

        if item == valor_meio:
            print("Item encontrado!")
            return indice, visitados
        elif item < valor_meio:
            fim = indice - 1
        else:
            inicio = indice + 1

    print("Item não encontrado.")
    return None, visitados


vetor = [15, 3, 9, 8, 6, 14, 4, 13, 11, 10, 1, 2, 5, 12, 7, 0]
vetor.sort()

item = 1
print("\nVetor ordenado:")
print(vetor)
print()
print()


indice_encontrado, passos = PesquisaBtn(vetor, item)

if indice_encontrado is not None:
    print(f"Item {item} encontrado na posição {indice_encontrado} do vetor.")
    grafo, cores_dos_nos = CriaArvoreBinaria(vetor, item)
    ExibirArvoreBinaria(grafo, cores_dos_nos, passos)  
else:
    print(f"Item {item} não está presente no vetor.")
