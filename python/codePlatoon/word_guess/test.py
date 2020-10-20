import csv

easy = []
medium = []
hard = []
with open('words.csv', mode='r') as rfile:
            words = csv.reader(rfile)
            for row in words:
                if row[0] == 'e':
                    easy = row[1:10] #11000000000
                if row[0] == 'm':
                    medium = row[1:10]
                if row[0] == 'h':
                    hard = row[1:10]

print('easy,',easy)
print('medium,',medium)
print('hard,', hard)


