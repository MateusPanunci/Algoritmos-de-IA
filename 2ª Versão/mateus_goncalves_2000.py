#Sem reposição e método de desempate é a classe do vizinho mais próximo
def knn(k, df_treino, df_teste):
     labels = []
     for line in df_teste:
          valores = []

          for linha in df_treino:
              feats = []
              for i in range(0,len(linha)- 1):
                  feats.append((float(line[i]) - float(linha[i]))**2)


              temp = sum(feats)**0.5
              valores.append([linha, round(temp, 3)]) # Distância euclidiana de cada linha


          valores.sort(key = lambda valor: valor[1])
          neighbors = []

          for index in range(0, k):
              neighbors.append(valores[index])


          list_label = [0,0]
          for vizinho in neighbors:
              label_treino = vizinho[0][-1]
              if label_treino == "0":
                  list_label[0] += 1
              elif label_treino == "1":
                  list_label[1] += 1


          if list_label[0] < list_label[1]:
              line.append("1")
              labels.append("1")


          elif list_label[0] > list_label[1]:
              line.append("0")
              labels.append("0")


          else:
              min_neighbor = neighbors[0][0]
              for linha in df_treino:
                  if linha == min_neighbor:
                       line.append(linha[-1])
                       labels.append(linha[-1])

     return labels