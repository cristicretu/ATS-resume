## Prerequisites 

- PyPDF library should be installed
- SpaCy for getting keywords, education and more

```bash
pip install -r requirements.txt
```

```
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download xx_ent_wiki_sm
```
> Check out [the spacy installation page](https://spacy.io/usage) for more help.


## Usage

```bash
python3 main.py path/to/pdf/file

```

### Input

- path/to/pdf/file: The path to the PDF file you want to extract text from. Could be a relative or a global path.

### Output

- The script will output the extracted text from the PDF file to the console
- Also, there will be three arrays, containing keywords, education, and work experience.

Please note that this script is just one step of a bigger process, and is not designed to check the ATS compliance yet.
