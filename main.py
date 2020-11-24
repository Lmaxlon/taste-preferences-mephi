##обработанные данные определяют похожесть записей из k-means
# coding=utf-8
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
def ReadFile (filename = r"C:\Users\user\PycharmProjects\pythonProject\menu.csv"):
   f = open (filename)
   r = csv.reader (f)
   mentions = dict()
   for line in r:
        user = line[0]
        product = line[1]
        rate = float(line[2])
        if not user in mentions:
            mentions[user] = dict()
        mentions[user][product] = rate
   f.close()
   return mentions

def makeRecommendation(userID, userRates, nBestUsers, nBestProducts):
    ##Для каждого из пользователей умножить его оценки на вычисленную величину меры
    matches = [(u, distCosine(userRates[userID], userRates[u])) for u in userRates if u != userID]
    bestMatches = sorted(matches, key=lambda x_y: (x_y[1], x_y[0]), reverse=True)[:nBestUsers]
    print("Most correlated with '%s' users:" % userID)
    for line in bestMatches:
        print("  UserID: %6s  Coeff: %6.4f" % (line[0], line[1]))
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
    print("Most correlated products:")
    for prodInfo in bestProducts:
        print("  ProductID: %6s  CorrelationCoeff: %6.4f" % (prodInfo[0], prodInfo[1]))
    ##sim — выбранная нами мера схожести двух пользователей, U — множество пользователей, r — выставленная оценка, k — нормировочный коэффициент
    return [(x[0], x[1]) for x in bestProducts]


##выведение рекомендации
rec = makeRecommendation('ivan', ReadFile(), 5, 5)
