import string


liczba_wierszy = int(input())

zania_lista = []
for wiersz in range(int(liczba_wierszy)):
    zdanie = input().strip() 
    zania_lista.append(zdanie)

liczba_slow = input()

zapytania = []
for wiersz in range(int(liczba_slow)):
    zapytanie = input().strip()
    zapytania.append(zapytanie)

indeks = dict()

for nr_dokumentu, zdanie in enumerate(zania_lista):
  wyczyszczony_dokument = zdanie.translate(str.maketrans('','',string.punctuation))
  wyczyszczony_dokument =  wyczyszczony_dokument.lower()
  wyczyszczony_dokument =  wyczyszczony_dokument.split(' ')


  for wyraz in wyczyszczony_dokument:
    if wyraz not in indeks:
      indeks[wyraz] = dict()
    if nr_dokumentu not in indeks[wyraz]:
      indeks[wyraz][nr_dokumentu] =0
    indeks[wyraz][nr_dokumentu] +=1

for zapytanie in zapytania:
  if zapytanie not in indeks:
    print([])
  else:
    czestosc_slowa = indeks[zapytanie]
    czestosc_slowa = list(czestosc_slowa.items())
    posortowane_czestosci = sorted(czestosc_slowa, key= lambda x: x[1], reverse = True)
    print ([i[0]for i in posortowane_czestosci])
