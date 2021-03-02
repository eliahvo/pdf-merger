import tkinter as tk
import tkinter.filedialog as tkfileDialog
import PyPDF2

pdfFiles = []
outputFile = ""

# basic window
window = tk.Tk()
window.title("PDF Merger")
window.geometry("500x400")
window.minsize(500, 400)

# header text
heading = tk.Label(window, text='PDF Merger')
# heading.place(relx=0.3, rely=0.1, anchor='center')
heading.grid(row=0, column=1, padx=60, pady=20)
heading.config(font=('Arial', 30))


def browsefuncPDFs(button):
    filename = tkfileDialog.askopenfilename(
        filetypes=(("pdf files", "*.pdf"),))
    if(filename):
        pdfFiles.append(filename)
        button.config(text=filename)


def addSelectPDF():
    print("add select pdf")


def browsefuncFolder():
    filename = tkfileDialog.asksaveasfilename(
        filetypes=(("pdf files", "*.pdf"),))
    if(filename):
        global outputFile
        outputFile = filename + ".pdf"
        buttonFolder.config(text=filename+".pdf")


def mergePDFs():
    if(outputFile and len(pdfFiles) >= 2):
        print("merging")

        # Create a new PdfFileWriter object which represents a blank PDF document
        pdfWriter = PyPDF2.PdfFileWriter()

        for filePath in pdfFiles:
            pdf = open(filePath, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdf)

            # Loop through all the pagenumbers
            for pageNum in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)

            # pdf.close()

        # write pdfs into the a new document
        pdfOutputFile = open(outputFile, 'wb')
        pdfWriter.write(pdfOutputFile)

        pdfOutputFile.close()
    else:
        print("no outputfile set or not 2 pdfs selected!")


# button for first file
buttonFile1 = tk.Button(window, text="Select PDF",
                        font=40, command=lambda: browsefuncPDFs(buttonFile1))
buttonFile1.grid(row=1, column=1, padx=0, pady=20)

# button for second file
buttonFile2 = tk.Button(window, text="Select PDF",
                        font=40, command=lambda: browsefuncPDFs(buttonFile2))
buttonFile2.grid(row=2, column=1, padx=0, pady=20)

# button to add more pdfs
buttonMoreFiles = tk.Button(window, text="+",
                            font=40, command=addSelectPDF)
buttonMoreFiles.grid(row=3, column=1, padx=0, pady=20)

# button for output folder
buttonFolder = tk.Button(window, text="Select output folder",
                         font=40, command=browsefuncFolder)
buttonFolder.grid(row=4, column=1, padx=0, pady=20)

# merge button
buttonMerge = tk.Button(window, text="Merge PDFs", font=40, command=mergePDFs)
buttonMerge.grid(row=4, column=2, padx=0, pady=20)

# run window
window.mainloop()
