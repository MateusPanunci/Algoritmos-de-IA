import random, copy

def separador():
    print("_" * 150, "\n" )

def knn(k, df_treino, df_teste, cabecalho = 0):
     if cabecalho == 0:
        None
     elif cabecalho == 1:
        df_treino.pop(0)
     elif cabecalho == 2:
        df_teste.pop(0)
     elif cabecalho == 3:
        df_treino.pop(0)
        df_teste.pop(0)
     else:
        return "Os valores para a variável cabeçalho variam de 0 a 3 apenas!"


     labels = []
     for line in df_teste:
          valores = []

          for linha in df_treino:
              feats = []
              for i in range(0, len(linha) - 1):
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
              labels.append("1")


          elif list_label[0] > list_label[1]:
              labels.append("0")


          else:
              min_neighbor = neighbors[0][0]
              for linha in df_treino:
                  if linha == min_neighbor:
                       labels.append(linha[-1])

     return labels



def main(): 
      separador()
      df = input("Digite o arquivo CSV (com o .csv): ")
      labels_teste, amostras = [], []


      separador()
      with open(df, "r") as arq:
          dataset = arq.readlines()


      dataset.pop(0)
      for i, linha in enumerate(dataset):
           linha = linha.strip().split(";")

           for j in range(len(linha)):
                  if linha[j] == "":
                        linha[j] = "0"

           dataset[i] = linha


      qtd_grupo, inicio, cont = round((len(dataset) * (0.1))), 0, 10
      fim = qtd_grupo


      random.shuffle(dataset)
      while cont > 0:
            amostras.append([dataset[j] for j in range(inicio, fim)])
            inicio += qtd_grupo
            fim += qtd_grupo
            cont -= 1


      for grupo in amostras:
            labels_teste.append([linha[-1] for linha in grupo])


      acuracias = {}
      for k in range(4,7):
            separador()
            print(f"---------- K = {k}----------")
            separador()

            order, amostra_treino, acuracia = 0, [], []

            while order != len(amostras):
                  for i, grupo in enumerate(amostras):
                      if i == order:
                          sem_label = copy.deepcopy(grupo)
                          for linha in sem_label:
                              linha.pop(-1)
                          amostra_teste = sem_label
                      else:
                          for linha in grupo:
                              amostra_treino.append(linha)

                  labels_knn = knn(k, amostra_treino, amostra_teste)
                  
                  print(f"Labels da amostra teste\n {labels_teste[order]}")
                  print(f"\nLabels do KNN:\n {labels_knn}")
                

                  acertos = 0
                  for i in range(len(labels_teste)):
                        if labels_teste[order][i] == labels_knn[i]:
                            acertos += 1


                  porcentagem_acertos = (acertos / len(labels_teste)) * 100
                  acuracia.append(porcentagem_acertos)
                  print(order)
                  print(f"\nAcurácia: {round(porcentagem_acertos, 2)}%")
                  separador()

                  
                  order += 1


            acuracias[f"k = {k}"] = acuracia


      print(acuracias)

     # print(f"Labels da amostra teste\n {labels_teste}")
     # print(f"\nLabels do KNN:\n {labels_knn}")



main()


