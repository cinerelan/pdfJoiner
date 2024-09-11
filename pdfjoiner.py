import os
import fitz  # PyMuPDF

def merge_pdfs_mupdf(filepaths, output_path):
    merger = fitz.open()

    for filepath in filepaths:
        print(f"Processing file: {filepath}")
        if not os.path.exists(filepath):
            print(f"Error: File does not exist: {filepath}")
        else:
            pdf = fitz.open(filepath)
            merger.insert_pdf(pdf)

    if merger.page_count == 0:
        print("Error: No pages to merge. Check the input PDF files.")
    else:
        merger.save(output_path)
        print(f"Merged PDF saved to: {output_path}")
        merger.close()

if __name__ == "__main__":
    # Specify the list of PDF file paths to merge
    pdf_files_to_merge = [
        os.path.join(r'C:\Users\Mohammad\Desktop\My_Folder', 'pdf_one.pdf'),
        os.path.join(r'C:\Users\Mohammad\Desktop\My_Folder', 'pdf_two.pdf'),
        os.path.join(r'C:\Users\Mohammad\Desktop\My_Folder', 'pdf_three.pdf'),
        os.path.join(r'C:\Users\Mohammad\Desktop\My_Folder', 'pdf_four.pdf')
    ]

    # Specify the output file path with an absolute path
    output_file_path = os.path.join(r'C:\Users\Mohammad\Desktop\My_Folder', 'output.pdf')

    # Merge the PDFs
    merge_pdfs_mupdf(pdf_files_to_merge, output_file_path)
