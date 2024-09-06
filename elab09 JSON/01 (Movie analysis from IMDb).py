import json
#from zipfile import ZipFile
#import sys

#!wget 'https://mike.cpe.ku.ac.th/download/IMDB_movies_merged.zip' -O '/tmp/IMDB_movies_merged.zip'
def read_json(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    return data

# specifying the zip file name
filename = "IMDB_movies_merged.json"
data = read_json(filename)
dir = []
imdbnum = []
rating = []
def q1():
  for i in range (len(data)):
    try:
      for j in range(len(data[i]['cast'])):
        if data[i]['cast'][j]['name_id'] == 'nm0000148':
          dirname = data[i]['director']['name']
          imdbnum.append(data[i]['ImdbId'])
          rating.append([dirname,data[i]['ratingValue']])
    except:
      pass
  
  for i in range(len(rating)):
    if rating[i][0] == 'Steven Spielberg':
      rating[i][1] = 0.0
  sorted_rating = sorted(rating, key=lambda x: float(x[1]) if len(x) > 1 and x[1] != '' else 0.0, reverse=True)

  count = 0
  i = 0
  while count != 5:
    
    if sorted_rating[i][1] != sorted_rating[i+1][1]:
      count += 1
      dir.append(sorted_rating[i][0])
      i += 1
    elif sorted_rating[i][1] == sorted_rating[i+1][1]:
      dir.append(sorted_rating[i][0])
      i += 1

  dir.sort()
  for i in dir:
    print(i)

def q2():
  for i in range (len(data)):
    cst = 0
    try:
      for j in range(len(data[i]['cast'])):
        if data[i]['cast'][j]['name_id'] == 'nm0000148' or data[i]['cast'][j]['name_id'] == 'nm0000169':
          cst += 1
      if cst == 2:
        imdbnum.append(data[i]['ImdbId'])
        rating.append([data[i]['name'],data[i]['ratingValue']])
    except:
      pass
  sorted_rating = sorted(rating, key=lambda x: float(x[1]) if len(x) > 1 and x[1] != '' else 0.0, reverse=True)
  print(sorted_rating[0][0])

print('(1) Answer of Q1')
print('(2) Answer of Q2')
ans = input('or just press (Enter): ')
if ans == '1':
  q1()
elif ans == '2':
  q2()
else:
    print('Nothing to do..')