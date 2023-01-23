import os
import sys

from pypdf import PdfReader
import spacy

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

if __name__ == "__main__":
    res = sys.argv[1]
    if not os.path.exists(res):
        print("File does not exist")
        sys.exit()

    # file exits
    text = ""

    with open(res, 'rb') as pdf_file:
        # pdf reader object
        reader = PdfReader(pdf_file)
        # get no. of pages
        num_pages = len(reader.pages) 
    
        for i in range(num_pages):
            page = reader.pages[i]
            text += page.extract_text()

    print(text)
    print('----------------------------')

    # Process the text with SpaCy
    doc = nlp(text)

    # Extract the keywords
    keywords = [token.text for token in doc if token.is_stop != True and token.is_punct != True]

    # Extract the education
    education = []
    for ent in doc.ents:
        if ent.label_ == "DEGREE":
            education.append(ent.text)

    # Extract the work experience
    experience = []
    for sent in doc.sents:
        if "experience" in sent.text.lower():
            experience.append(sent.text)

    print(keywords)
    print(education)
    print(experience)
