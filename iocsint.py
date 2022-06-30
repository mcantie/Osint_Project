import csv
import codecs
import whois
import re
import json

from geoip import geolite2

# var
domains = []
domains_data = []
ip = []
tojson = []
dict_ip = {}

# path to file
sample = 'sample.csv'
output_ip = 'json_ip_data.json'
output_domains = 'json_domains_data.json'

# regex
regexip = "^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
regexdomains = "[A-Za-z0-9]{1,63}\.[a-z]{2,3}"


def printAscii():
    
	print("""
  _____ ____   _____  _____ _____ _   _ _______ 
 |_   _/ __ \ / ____|/ ____|_   _| \ | |__   __|
   | || |  | | |    | (___   | | |  \| |  | |   
   | || |  | | |     \___ \  | | | . ` |  | |   
  _| || |__| | |____ ____) |_| |_| |\  |  | |   
 |_____\____/ \_____|_____/|_____|_| \_|  |_|                                                                                                                                                                												  
	
    """)


# Open csv and extract cell by filtering whether they are IP or Domains
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


# Create json file from json string
def output_to_json(json_string, output_file): 

    with open(output_file, 'w') as file :
        file.write(json_string)


# use geoip to extract data from the ip and convert the file into a json
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
    return json_string


# use whois to extract data from domains name and put it into a json string
def domain():

    for row in domains:
        for cell in row:
            match = whois.whois(cell)
            domains_data.append(match)

    json_string = json.dumps(domains_data, default=str)
    return json_string


def main():

    printAscii()
    extract_csv(sample, regexip, regexdomains)

    json_ip_string = geoip()
    json_domains_string = domain()

    output_to_json(json_ip_string, output_ip)
    output_to_json(json_domains_string, output_domains)
    

if __name__ == '__main__':
	main()