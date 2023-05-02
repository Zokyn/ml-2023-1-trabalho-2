import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# lendo o dataset
df = pd.read_excel('dataset.xlsx')

### PRE-PROCESSAMENTO
# removendo colunas irrelevantes
df = df.drop(columns=['Patient ID', 'Patient addmited to regular ward (1=yes, 0=no)', 'Patient addmited to semi-intensive unit (1=yes, 0=no)', 'Patient addmited to intensive care unit (1=yes, 0=no)'])

# mapeando dados categorizados
for y in df.columns:
      if df[y].dtype == 'object': 
            lbl = LabelEncoder()
            lbl.fit(list(df[y].values))
            df[y] = lbl.transform(list(df[y].values))

# checando a coluna de resultados
print(df['SARS-Cov-2 exam result'].value_counts(normalize=True))
print('\n\n')

# removendo colunas com mais de 90% de dados faltantes
df = df[df.columns[df.isna().sum()/df.shape[0] < 0.9]]
# print((df.isna().sum()/df.shape[0]).sort_values(ascending=True))
# print('\n\n')

# preenchendo dados com mediana
df = df.fillna(df.median())

### CORRELAÇÕES
# exibindo correlações
correlations = df.corrwith(df['SARS-Cov-2 exam result'])
print('columns with greater correlations')
print(correlations.sort_values(ascending=False).head(10))
print('\n\n')
print('columns with smaller correlations')
print(correlations.sort_values(ascending=True).head(10))
print('\n\n')
print(correlations.abs().sort_values(ascending=False).head(10))
print('\n\n')

### TREINAMENTO
# criando listas X (features) e y (resultado esperado)
# X = df.drop(columns=['SARS-Cov-2 exam result'])
X = df[['Platelets', 'Leukocytes', 'Monocytes', 'Patient age quantile']]
y = df['SARS-Cov-2 exam result']

# separando 66% do dataset para treinamento e 33% para validação
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state=101)

# criando o modelo e treinando
# model = KNeighborsClassifier(n_neighbors=7)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

### RESULTADOS
# calculando acurácia

prds = model.predict(X_test)
tn, fp, fn, tp = confusion_matrix(y_test, prds).ravel()
print(f'tn {tn}, fp {fp}, fn {fn}, tp {tp}', '\n\n',
      'Accuracy:', (accuracy_score(y_test, prds)), '\n\n',
      'Classification Report:\n', (classification_report(y_test, prds)))

