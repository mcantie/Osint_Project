import csv
import codecs
import whois
import re
import json

from geoip import geolite2

ip = []
domains = []
tojson = []
dict_ip = {}
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


def output_to_json(json_string): 

    with open('json_ip_data.json', 'w') as file :
        file.write(json_string)


def geoip():

    for row in ip:
        for cell in row:
            match = geolite2.lookup(cell)
            dict_geoip = {
                "ip": match.ip,
                "country" : match.country,
                "timezone" : match.timezone,
                "continent" : match.continent,
                "location" : match.location
            }
            dict_temp = dict_geoip.copy()
            tojson.append(dict_temp)

    json_string = json.dumps(tojson)
    print(json_string)
    return json_string



def domain():

    for row in domains:
        for cell in row:
            match = whois.whois(cell)
            print(match)


def main():

    printAscii()
    extract_csv(sample, regexip, regexdomains)
    json_string = geoip()
    #domain()
    output_to_json(json_string)
    

if __name__ == '__main__':
	main()
