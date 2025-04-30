# Método k-NN (k-Nearest Neighbors) de IA

Fiz este algoritmo como parte de uma atividade do meu primeiro semestre na UEL, para a matéria de Introdução à Ciência de Dados e IA 🤖👨‍💻

## Descrição do k-NN

O método KNN é modelo de machine learning utilizado para classsificar amostras novas com uma base prévia de dados de treinamento. Seu funcionamento consiste no cálculo da distância dos dados de treinamento em relação ao dado a ser classificado; depois são selecionados os k vizinhos mais próximos (sendo k um número inteiro maior que 0) e é contado a quantidade de cada classe deles; ao final, o rótulo mais frequente dentre os vizinhos é atribuído ao dado que está sendo classificado.

### _Função knn()_

!! _*Aviso inicial*_ !! : as amostras não devem ser do formato de dataframe (não funciona com o Pandas). Deve-se colocar o nome do arquivo + .csv entre aspas. Ou também pode atribuir essa nomenclatura a variáveis para servirem de entrada.

```
# Exemplo de como chamar a função

knn(3, "Aula 18 - dataset_alterado_2.csv", "teste_2.csv")
```

1. Recebe o valor k (número de vizinhos próximos a serem considerados), a amostra*treino (variável \*\*\_df_treino***), a amostra_teste (variável **_df_teste_**), e um valor para a variável **_cabecalho_\*\* que pode compartar os seguintes valores:

```
Cabecalho == 0: Não tem em nenhuma das amostras
Cabecalho == 1: Tem na df_treino
Cabecalho == 2: Tem na df_teste
Cabecalho == 3: Tem nos dois (valor padrão).
```

2. Dentro da função, são abertos os dois arquivos csv e é identificado se o que foi passado no parâmetro está correto, se não tiver o código não funcionará ou imprimirá uma mensagem de erro.

3. É feito a formatação as duas amostras para preencher as lacunas vazias com o número 0 e para transformá-las em matrizes bidimensionais.

4. É feito o cálculo da distância euclidiana de todas as linhas do **_df_treino_** em relação a primeira linha de **_df_teste_**, e são armazenadas na váriavel **_valores_**.

5. Utiliza-se na variável **_valores_** a função sort para ordena-lá de forma ascendente. Ainda com **_valores_** , é coletado a quantidade k dos valores mais próximos (em relação a linha da amostra teste que está sendo iterada) e são armazenados na variável **_neighbors_**.

6. Conta-se a quantidade de cada rótulo que aparece na variável **_neighbors_**, a qual são registradas na variável **_list_label_**.

7. Se a frequência de um rótulo for maior que a do outro, ele é atribuído à uma lista chamada **_labels_**, o qual detém os rótulos encontrados pela função k-nn. Se houver um empate, então é adicionado o rótulo do vizinho mais próximo (menor distância euclidiana).

8. O mesmo processo é realizado para as demais linhas de **_df_teste_** e, por fim, é retornado para a função main() a variável **_labels_**, que contém as classes encontradas pela função.

## Outros Detalhes

. _Critério de desempate_: voto do vizinho mais próximo

. _Métrica de distância_: euclidiana

. _Bibliotecas de python utilizadas_: nenhuma

. _Porcentagem da amostra treino_: 80%

. _Porcentagem da amostra teste_: 20%

. _Última informação_: o número de colunas entre as amostras tem que ser o mesmo, porém o conjunto de dados de onde foram tiradas pode ter qualquer quantidade de atributos.
