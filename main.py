import os
import sys
from pypdf import PdfReader

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
