import pandas as pd

# Загрузите датасет
df = pd.read_csv('titanic.csv')

# Выберите нужные столбцы
df_subset = df[['Pclass', 'Sex', 'Age']]

# Сохраните новый датасет
df_subset.to_csv('titanic_subset.csv', index=False)
