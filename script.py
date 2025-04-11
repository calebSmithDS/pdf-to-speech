"""
This module contains custom classes to achieve the following functions: extracts text from pdf, removes intext and reference list, saves file to computer
"""

import re
from pdfminer.high_level import extract_text
import unicodedata
import sys
import pyttsx3

# this is basically setting the default output to utf-8, a lot of computers default to charmap
sys.stdout.reconfigure(encoding='utf-8')

################
# Saving files
################

# not currently in use
def text_to_mp3(text, filename):
    '''
    Takes input text file and converts the file to mp3

    Args:
        text (str): string to convert
        filename(str): name of the file - this will control where the file is saved and what format
    '''

    # intialize the speaker engine 
    engine = pyttsx3.init(driverName='sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    # creating mp3 file
    engine.save_to_file(text, filename)
    engine.runAndWait()
    engine.stop()

def text_to_pdf(text, filename):
    """
    creates pdf file from text

    Args:
        text (str): string to convert
        filename(str): name of the file - this will control where the file is saved and what format (pdf)
    """

    with open(filename, 'w', encoding="utf-8", errors='replace') as txtfile:
        txtfile.write(text)
    

#################
# extracting text from pff
#################

def clean_text(pdf):
    """
    extracts text from pdf document - removes references from text file

    Args:
        pdf (pdf file): pdf file in need of cleaning

    Return: 
        newText (str): str of cleaned text
    """
    # local constants 
    # mp3_file = pdf + "-output.mp3"
    # txt_file = pdf + "-output.txt"

    # extract text from pdf
    text = extract_text(pdf)

    #################
    # cleaning text and removing references
    #################

    # normalize text
    text = unicodedata.normalize("NFKC", text)
    # strip newline characters from text - dont think working atm
    text = text.replace('\n','')

    # pattern matching and removing 
    refReg = re.compile(r'\([A-Za-z0-9\.,\s]*\s*\d+\)')
    newtext = re.sub(refReg, '', text)
    refReg = re.compile(r'\[[^A-Za-z,]*\]')
    newtext = re.sub(refReg, '', newtext)

    # references
    refReg = re.compile(r'References\s*.*', re.DOTALL)
    newtext = re.sub(refReg, '', newtext)  

    return newtext
    
    # naming the files 
    text_to_mp3(newtext, mp3_file)
    text_to_pdf(newtext, txt_file)


"""
code that isnt being used at the moment
"""

# def open_file():
#     # getting file path and opening window
#     filename = filedialog.askopenfilename()
#     return filename

# try:
# # this is used to take in arguments from the command line
#     # file = sys.argv[1]
#     # extract_text2(file)

#     file = "1-s2.0-S030646032300326X-main (1).pdf"

# # development and debug 
#     # file = open_file()
#     # clean_text(file)
# # prints to screen for debugging purposes
#     # with open('output.txt', 'r', encoding="utf-8", errors='replace') as file:
#     #     content = file.read()
#     #     print(content)

# except Exception as e:
#     print(f"Error reading file: {e}")