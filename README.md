# Osint_Project
Osint Project for UTT (Mastère expert forensic &amp; Cybersecurity)

![image](https://user-images.githubusercontent.com/50552002/176748975-615e85b8-11bb-4fb7-8706-5aa6ee8b03e2.png)


IOCSINT is a project used to extract data from ioc (ip + domains) and converting them into a json to analyze and ingest them if needed in tools (ex : elk).

In input a csv file containing IP and/or domains name is needed. 

![image](https://user-images.githubusercontent.com/50552002/176748128-980135ed-67e6-487a-8edd-ef6ef2042166.png)

## Python librairies 

they are used to search data :

ip - with geoip from MaxMind
domains - whois

### IP output :

![image](https://user-images.githubusercontent.com/50552002/176748646-5f5aff13-9258-4584-9350-abc2a022c84d.png)

### Domains output :


## Prerequisite

Project use python 2.7

'pip install -r requirements.txt'

## Usage

python iocsint.py
