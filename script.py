import csv
import codecs
import whois
from geoip import geolite2

rows = []

with open("sample.csv", 'r') as file:
    csvreader = csv.reader(codecs.EncodedFile(file, 'utf-8', 'utf-8-sig'), delimiter=";")
    for row in csvreader:
        rows.append(row)

print(rows)

match = geolite2.lookup('8.8.8.8')
match.country

print(match.country)

w = whois.whois('utt.fr')

print(w)