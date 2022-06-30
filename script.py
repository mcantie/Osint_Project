import csv
import codecs
import whois
import re

from geoip import geolite2

ip = []
domains = []
sample = "sample.csv"

regexip = "^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
regexdomains = "[A-Za-z0-9]{1,63}\.[a-z]{2,3}"


def printAscii():
	"""
	ASCII Art
	"""
	print("""
  _____ ____   _____  _____ _____ _   _ _______ 
 |_   _/ __ \ / ____|/ ____|_   _| \ | |__   __|
   | || |  | | |    | (___   | | |  \| |  | |   
   | || |  | | |     \___ \  | | | . ` |  | |   
  _| || |__| | |____ ____) |_| |_| |\  |  | |   
 |_____\____/ \_____|_____/|_____|_| \_|  |_|                                                                                                                                                                												  
	
    """)


def extract_csv(csvfile, regexip, regexdomains):

    with open(csvfile, 'r') as file:
        csvreader = csv.reader(codecs.EncodedFile(file, 'utf-8', 'utf-8-sig'), delimiter=";")
        for row in csvreader:
            for cell in row:
                match_ip = re.match(regexip, cell)
                match_domains = re.match(regexdomains, cell)
                if match_ip:
                    ip.append(row)
                if match_domains:
                    domains.append(row)

    print("ip :",ip)
    print("domains :", domains)
        

def geoip():
    match = geolite2.lookup('8.8.8.8')
    match.country
    print(match.country)


def domain():
    w = whois.whois('utt.fr')
    print(w)


def main():

    printAscii()
    extract_csv(sample, regexip, regexdomains)
    

if __name__ == '__main__':
	main()
