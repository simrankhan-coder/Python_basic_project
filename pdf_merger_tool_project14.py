import PyPDF2
import os

pdfs=['file1.pdf','file2.pdf','file3.pdf']
merger=PyPDF2.PdfMerger()
for pdf in pdfs:
    if os.path.exists(pdf):
        merger.append(pdf)
    else:
        print(f"Warning: The file '{pdf}' was not found and will be skipped.")

if merger.pages:
    merger.write("merged_output.pdf")
    print("PDFs merged successfully!")
else:
    print("No PDFs were found to merge. The output file was not created.")

merger.close()
