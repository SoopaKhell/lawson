import pdftotext
import re

# Load your PDF
with open("HOA.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

text = "".join(pdf)
text = re.sub(" +", " ", text)
text = text.replace(" ", "")
text = text.replace("---\n\n\n\n---", "")

print(text)
