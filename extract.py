import docx
import re

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def hasYear(inputString):
    return bool(re.search(r'[0-9]{4}', inputString))

text = getText("./Chapter 23 Climate Change and Sharks, Rummer et al., 5Feb.2021.docx")

pattern = re.compile(r'\((.*?)\)')
# get everything in brackets
for match in re.findall(pattern, text):
    #if text contains year
    if (hasYear(match)):
        print(match)



#print(text)
