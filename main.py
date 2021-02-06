##обработанные данные определяют похожесть записей из k-means
# coding=utf-8
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

import math
def distCosine (vecA, vecB):
    def dotProduct (vecA, vecB):
        d = 0.0
        for dim in vecA:
            if dim in vecB:
                d += vecA[dim]*vecB[dim]
        return d
    return dotProduct (vecA,vecB) / math.sqrt(dotProduct(vecA,vecA)) / math.sqrt(dotProduct(vecB,vecB))
import csv
def ReadFile (filename = r"C:\Users\user\PycharmProjects\pythonProject\vybor.csv"):
   f = open (filename)
   r = csv.reader (f)
   mentions = dict()
   for line in r:
        user = line[0]
        product = line[1]
        rate = float(all_predictions[0])
        if not user in mentions:
            mentions[user] = dict()
        mentions[user][product] = rate
   f.close()
   return mentions

def makeRecommendation(userID, userRates, nBestUsers, nBestProducts):
    ##Для каждого из пользователей умножить его оценки на вычисленную величину меры
    matches = [(u, distCosine(userRates[userID], userRates[u])) for u in userRates if u != userID]
    bestMatches = sorted(matches, key=lambda x_y: (x_y[1], x_y[0]), reverse=True)[:nBestUsers]
    print("Наиболее похожие с '%s' дни:" % userID)
    for line in bestMatches:
        print("  Day: %6s  Coeff: %6.4f" % (line[0], line[1]))
    sim = dict()
    sim_all = sum([x[1] for x in bestMatches])
    bestMatches = dict([x for x in bestMatches if x[1] > 0.0])
    ##с присвоением id
    for relatedUser in bestMatches:
        for product in userRates[relatedUser]:
            if not product in userRates[userID]:
                if not product in sim:
                    sim[product] = 0.0
                sim[product] += userRates[relatedUser][product] * bestMatches[relatedUser]
    for product in sim:
        sim[product] /= sim_all
    bestProducts = sorted(iter(sim.items()), key=lambda x_y1: (x_y1[1], x_y1[0]), reverse=True)[:nBestProducts]
    print("Наиболее схожие блюда с теми, которые выбирал пользователь:")
    for prodInfo in bestProducts:
        print("  ProductID: %6s  CorrelationCoeff: %6.4f" % (prodInfo[0], prodInfo[1]))
    ##sim — выбранная нами мера схожести двух пользователей, U — множество пользователей, r — выставленная оценка, k — нормировочный коэффициент
    return [(x[0], x[1]) for x in bestProducts]


##выведение рекомендации
rec = makeRecommendation('3day', ReadFile(), 5, 5)
