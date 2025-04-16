#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
SL language vitality and endangerment stats

UNCOMMENT sections for original usage

Author: euan.mcgill@upf.edu | 2024/04/22
'''

from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
from time import sleep

print("Ethnologue seems to use rate-limiting\n")

user_q = input("Type 1 for SLs only or 2 for all Ethnologue languages:  ")

if user_q == "1":
    sl_main = "https://www.ethnologue.com/subgroup/2/" # 2 for SLs, 3 for IE
    main_page = requests.get(sl_main)
    soup = BeautifulSoup(main_page.text, features="lxml")
    isos = soup.findAll(class_="chip")
    langs = []
    codes = []
    for lang in isos:
        cod = str(lang.get('href'))
        url = f'https://www.ethnologue.com{cod}'
        langs.append(url)
        # you forgot to regex process these lol
        cod_a = re.sub(r'(/language/)(.+?)(/)', r'\2', cod)
        codes.append(cod_a)
elif user_q == "2":
    langs = []
    data = pd.read_csv('LanguageCodes.tab',delimiter='\t')
    codes = data['LangID']
    for lang in codes:
        url = f'https://www.ethnologue.com/language/{lang}'
        #print(url)
        langs.append(url)

# langs = []
# data = pd.read_csv('LanguageCodes.tab',delimiter='\t')
# codes = data['LangID']
# for lang in codes:
#     url = f'https://www.ethnologue.com/language/{lang}'
#     #print(url)
#     langs.append(url)

with open('lang_vitality_1.csv', 'w', encoding='utf8') as out:
    descs = []
    supps = []
    popns = []
    for eth in langs[6786:]:
        print(eth)
        try:
            page = requests.get(eth)
            soup = BeautifulSoup(page.text, features="lxml")
            popn = "UNK"
            if soup.findAll('div', class_="pop_2 pop__level1 selected"):
                popn = "NoUsers"
            if soup.findAll('div', class_="pop_2 pop__level2 selected"):
                popn = "<10k"
            if soup.findAll('div', class_="pop_2 pop__level3 selected"):
                popn = "10k<1M"
            if soup.findAll('div', class_="pop_2 pop__level4 selected"):
                popn = "1M<1B"
            if soup.findAll('div', class_="pop_2 pop__level5 selected"):
                popn = ">1B"
            popns.append(popn)
            #else:
                #popns.append("UNK") # verify that this is ok
            #lab = soup.findAll('meta')[2]
            #desc = str(lab.get('content'))
            #desc_a = re.search(r'(institutional|stable|endangered|extinct)' ,desc)
            ### For the language vitality labels
            lab = soup.findAll('li', class_= "histogram__datum tooltip")
            desc="UNK"
            for eng in lab:
                if desc!="UNK":
                    break
                #print(eng)
                dcat = eng['data-category']
                #print(dcat)
                dcon = eng['data-count']
                #print(dcon)
                if dcat == '0' and dcon ==  '1':
                    desc = "Institutional"
                elif dcat == '1' and dcon == '1':
                    desc = "Stable"
                elif dcat == '2' and dcon == '1':
                    desc = "Endangered"
                elif dcat == '3' and dcon == '1':
                    desc = "Extinct"
                else:
                    desc = "UNK"
                #print(desc)
            descs.append(desc)
            # print(desc_a.group())
            # desc_b = desc_a.group()
            # descs.append(desc_b)
            ### For the Digital Language Support labels
            pic = soup.findAll('img')[1]
            supp = str(pic.get('src'))
            supp_a = re.sub(r'(\/img\/)(.+?)(\.png)', r'\2', supp)
            supps.append(supp_a)
            out.write(eth+","+supp_a+","+desc+","+popn+"\n")
            out.flush()
        except:
            print("Data Not Found")
            supps.append("LOOKUP")
            descs.append("LOOKUP")
            popns.append("LOOKUP")
            out.write(eth+"LOOKUP,LOOKUP,LOOKUP\n")
            out.flush()
        sleep(2.2) # to try and circumvent request restrictions
    print(len(codes), len(descs), len(supps), len(popns))

# with open('sl_vitality.csv', 'w', encoding='utf8') as out:
#     for a,b,c,d in zip(codes,descs,supps,popns):
#         line = a + ',' + b + ',' + c + ',' + d + '\n'
#         #print(line)
#         out.write(line)


#print(supps)