# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 18:42:43 2015

@author: Vilja Hulden

A script for converting a JSTOR data for research citations file (.csv) into a JSON catalog file of the format required by bookworm (http://bookworm.culturomics.org/). You need this file, a file called "field_descriptions.json" and a directory with the full text files to create your own bookworm. For details, see http://bookworm.culturomics.org/docs.php

"""

import re


"""SECTION FOR LOCAL DEFINITIONS -- YOU NEED TO CHANGE THESE"""

# Change workdir and filedir to suit your needs.
workdir = "/Users/miki/work/research/digital/scriptsforgithub/createbookwormjson/"
readfile = "samplecitations.csv"
writefile = "jsoncatalog.txt" #don't change
"""END SECTION FOR LOCAL DEFINITIONS, CODE FOLLOWS"""

with open(workdir+readfile) as f:
    entriestemp = f.read()
    entries = [line for line in entriestemp.split('\n') if line.strip() != '']


jsonlines = []

for entry in entries[1:]:
    #get all necessary data
    #note that sometime JSTOR citation files come with the fields in a different
    #...order, in which case you would need to adjust here accordingly.
    entrylist = entry.split('\t')
    thisid = entrylist[0]
    title = entrylist[2]
    authorfield = entrylist[3]
    authors = re.sub(',',' and ',authorfield)
    journal = entrylist[4]
    volume = entrylist[5]
    number = entrylist[6] 
    pdate = entrylist[7]
    pyear = int(pdate[:4])
    pmonth = int(pdate[6:7])
    thisidfn = re.sub('/','_',thisid)
    thisidfn = str(pyear)+ "_ocr_"+thisidfn
    #this s my version, not for the publishe one
    
    
    #then let's transform into a bookworm JSON catalog
    
    searchstring = authors + " - " + title
    jsonline = '{"searchstring": "'+ searchstring +'", '
    jsonline += '"date": "' + str(pyear) + '-' + str(pmonth) + '", '
    jsonline += '"filename": "' + thisidfn + '"}'
    
    jsonlines.append(jsonline)   
    
jsonlinestxt = "\n".join(jsonlines)


with open(workdir+writefile, 'w') as f:
    f.write(jsonlinestxt)
    
    
