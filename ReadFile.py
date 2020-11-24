import csv
def ReadFile (filename = "<menu.csv>"):
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