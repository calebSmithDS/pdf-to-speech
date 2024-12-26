import re
from pdfminer.high_level import extract_text
import unicodedata
import sys
import pyttsx3
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

# this is basically setting the default output to utf-8, a lot of computers default to charmap
sys.stdout.reconfigure(encoding='utf-8')

# extracts the pdf document - creates a txt file and a mp3 file
def extract_text2(pdf):
    # extract text from pdf
    text = extract_text(pdf)
    # intialize the speaker
    speaker = pyttsx3.init()

# normalize text
    text = unicodedata.normalize("NFKC", text)
# strip newline characters from text - dont think working atm
    text = text.strip().replace('/n',' ')

# pattern matching and removing 
    refReg = re.compile(r'\(.+[,]\s*\d+\)')
    newtext = re.sub(refReg, '', text)
    refReg = re.compile(r'\[.+\]')
    newtext = re.sub(refReg, '', newtext)

    # handling newline characters 
    refReg = re.compile(r'\(.+\n.*[,]\s*\d+\)')
    newtext = re.sub(refReg, '', newtext)

    refReg = re.compile(r'\(.+[,]\s*\n\d+\)')
    newtext = re.sub(refReg, '', newtext)   

    # references
    refReg = re.compile(r'References\s*.*', re.DOTALL)
    newtext = re.sub(refReg, '', newtext)  

    # naming the files 
    mp3_file = pdf + "-output.mp3"
    txt_file = pdf + "-output.txt"

    # creating mp3 file
    speaker.save_to_file(newtext, mp3_file)
    speaker.runAndWait()
    speaker.stop()

    # creating text file
    with open(txt_file, 'w', encoding="utf-8", errors='replace') as txtfile:
        txtfile.write(newtext)

def open_file():
    # getting file path and opening window
    filename = filedialog.askopenfilename()
    return filename

try:
# this is used to take in arguments from the command line
    # file = sys.argv[1]
    # extract_text2(file)

# development and debug 
    file = open_file()
    extract_text2(file)
# prints to screen for debugging purposes
    with open('output.txt', 'r', encoding="utf-8", errors='replace') as file:
        content = file.read()
        print(content)
    # creating the tkinter gui window
    root = Tk()
    root.title("PDF to MP3")
    root.mainloop()

except Exception as e:
    print(f"Error reading file: {e}")