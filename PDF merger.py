import PyPDF2
import sys
import os

merger = PyPDF2.PdfMerger()
# The files that you want to merge must be in this directory
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)

# Select the name that you want to give to the new file
merger.write("lastMerged.pdf")
merger.close()
