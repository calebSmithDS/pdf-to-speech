import re
from pdfminer.high_level import extract_text
import unicodedata
import sys

# this is basically setting the default output to utf-8, a lot of computers default to charmap
sys.stdout.reconfigure(encoding='utf-8')


def extract_text2(pdf):
   

    text = extract_text(pdf)

# normalize text
    text = unicodedata.normalize("NFKC", text)

    # refReg = re.compile(r'[\r\n]')
    # newtext = re.sub(refReg, '', text)  
    refReg = re.compile(r'\(.+[,]\s*\d+\)')
    newtext = re.sub(refReg, '', text)
    refReg = re.compile(r'\[.+\]')
    newtext = re.sub(refReg, '', newtext)

    # handling newline characters 
    refReg = re.compile(r'\(.+\n.*[,]\s*\d+\)')
    newtext = re.sub(refReg, '', newtext)

    refReg = re.compile(r'\(.+[,]\s*\n\d+\)')
    newtext = re.sub(refReg, '', newtext)   

    # refReg = re.compile(r'\(.+[,].*\d+\)', re.DOTALL)
    # newtext = re.sub(refReg, '', newtext) 

    # references
    refReg = re.compile(r'References\s*.*', re.DOTALL)
    newtext = re.sub(refReg, '', newtext)  

    # txt_file = "output.txt"
    txt_file = pdf + "-output.txt"

    with open(txt_file, 'w', encoding="utf-8", errors='replace') as txtfile:
        txtfile.write(newtext)



try:
# this is used to take in arguments from the command line
    file = sys.argv[1]
    extract_text2(file)

# development and debug 
    # extract_text2("1-s2.0-S030646032300326X-main (1).pdf")
# prints to screen for debugging purposes
    # with open('output.txt', 'r', encoding="utf-8", errors='replace') as file:
    #     content = file.read()
    #     # print(content)

except Exception as e:
    print(f"Error reading file: {e}")