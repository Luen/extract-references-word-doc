""" Extract references from Word document """
import re
import docx


def get_text(filename):
    """ Get text from .docx files """
    doc = docx.Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return "\n".join(full_text)


def has_year(input_string):
    """ Returns true or false if string contains four consecutive numbers """
    return bool(re.search(r"[0-9]{4}", input_string))


# Edit the word file name/location here:
TEXT = get_text("./Chapter 23 Climate Change and Sharks, Rummer et al., 5Feb.2021.docx")

pattern = re.compile(r"\((.*?)\)")  # get everything in brackets
for match in re.findall(pattern, TEXT):  # loop through results
    if has_year(match):  # if text contains year
        print(match)
