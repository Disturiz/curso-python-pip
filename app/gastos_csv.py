import csv

def read_csv(path):
   with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter= ",")
      dic = { j: k for j,k in reader}
      total = 0
      for valor in dic.values():
         print(dic +'\n')
         total += int(valor)
      return int(total)
   

total = read_csv('./app/gastos.csv')
print(total)