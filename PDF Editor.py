# Prorgam: This is a simple pdf tool to merge, extract split pdfs
# Input: the input should be the path to pdf files and positive integers for page numbers
# Author 1: George Malak Madgy - 20231042
# Version: V0
# Date: 2/3/2023

# This is the library needed for this project
import PyPDF2

def merge_pdfs(files, output):
    merger = PyPDF2.PdfMerger()
    for pdf in files:
        merger.append(pdf)
    with open(output, 'wb') as f:
        merger.write(f)
    print(f"\nPDFs merged in {output} successfully!")
    
def extractPageFromFile(fileName, pageNum):
    # Get File
    try:
        srcPdf = PyPDF2.PdfReader(fileName)
    except FileNotFoundError:
        print(f"\nError! file {fileName} doesn't exist.")
        return
	# Get Page Number
    try:
        pageNum = int(pageNum)
        if pageNum <= 0:
            raise ValueError
    except ValueError:
        print("\nError! invalid page number.")
        return
    try:
        page = srcPdf.pages[pageNum - 1]
    except IndexError:
        print(f"\nError! page number {pageNum} doesn't exist.") 
        return   
	# Save new pdf
    try:
        newPdf = PyPDF2.PdfWriter()
        newPdf.add_page(page)
        newPdf.write(f"{fileName[0:-4]}-{pageNum}.pdf")
        print(f"\n{fileName[0:-4]}-{pageNum}.pdf saved successfully.")
    except:
        print("\nSome unexpected error happened.")

def splitFileIntoSeperatePages(fileName):
    print('\nNot done yet!')

# Main Code
print("Welcome To This Pdf Tool")
print("==============================")
print("1- Merge two pdfs\n2- Extract page from pdf\n3- Split pdf into pages\n4- Exit")

choice = input("Enter your choice: ")

if choice == '1':
    fileNames = input('Enter file names seperated by a spaces: ')
    outputFileName = input('Enter output file name: ')
    merge_pdfs(fileNames.split(), outputFileName)

elif choice == '2':
    fileName = input('Enter File Name: ')
    pageNum = input('Enter Page Number: ')
    extractPageFromFile(fileName, pageNum)
elif choice == '3':
    print("\nUnder Work!")
elif choice == '4':
    print('\nGood Bye!')
else:
    print('\nError! This is invalid choice!')