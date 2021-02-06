# Импортируем библиотеки
from sklearn import datasets
from sklearn.cluster import KMeans

# Загружаем набор данных (файл iris.csv отредактирован)

menu_df = datasets.load_iris()

# Описываем модель
model = KMeans(n_clusters=3)

# Проводим моделирование
model.fit(menu_df.data)

# Предсказание на первом примере
predicted_label = model.predict([[1,750,45]])
#7.2, 3.5, 0.8, 1.6

# Предсказание на всем наборе данных
all_predictions = model.predict(menu_df.data)

# Выводим предсказания
print(predicted_label)
print(all_predictions)

