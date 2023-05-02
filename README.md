# Trabalho prático 2

* Nome do Aluno: ________
* Número de Matrícula: ________
* Disciplina: Aprendizado de Máquina
* Semestre: 2023/1
* Data: 19/04/2023
* Data da entrega: 03/05/2023
* Valor: 2,0

> Orientações: preencher com seus dados antes da data de entrega

## Como entregar este trabalho

Faça um fork deste repositório e faça os commits com o código que você utilizou para chegar nos resultados. Serão aceitos os commits até a data de 03/05/2023 às 18:59:59 (antes da aula).

No dia 03/05/2023 haverá uma apresentação expositiva das técnicas utilizadas e resultado.

**Códigos duplicados ou com bastante semelhança terão suas notas zeradas**

## Classificação

Para este trabalho, utilize o dataset do trabalho 1 e os seguintes algoritmos de classificação

* [Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html)
* [Árvores de decisão](https://scikit-learn.org/stable/modules/tree.html)
* [KNN](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)

Compare os resultados de classificação dos três algoritmos. Apresente as métricas da classificação (matriz de confusão, acurária, precisão e revocação das classes) e as fronteiras de decisão para as features escolhidas.

## Tópicos de avaliação

* Detalhamento e justificativa das metodologias utilizadas;
* Análise dos códigos entregues;
* Apresentação expositiva dos resultados.

# Métricas de Sucesso

## Matriz de Confusão 

Antes de apresentas as métricas de sucesso do modelo de classificação, da por sua matriz de confusão, precisamos nos familiarizar com certos termos e nomenclaturas.

**True Negative (tn)** = verdadeiro negativo
**False Positive (fp)** = falso positivo
**False Negative (fn)** = falso negativo
**True Positive (tp)** = verdadeiro positivo

## Medidas

### PRECISÃO 
```
    precision = tp / (tp + fp)
```
quantifica amostras recuperadas que são relevantes
****
### REVOCAÇÃO (RECALL)
```
    recall = tp / (tp + fn)
```
quantifica amostras relevantes que são recuperadas
****
### ACURÁCIA 
```python
    accuracy = (tp + tn) / (tp + tn + fp + fn)
```
### F1-SCORE
```
    f1-score = 2 * (p * r) / (p + r)
```