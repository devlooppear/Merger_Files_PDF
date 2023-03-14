import PyPDF2
import os

def connection():
    merger = PyPDF2.PdfMerger()
    return merger

def finding_files():
    lista_arquivos = os.listdir("pdfs_mesclar")
    return lista_arquivos

def merging_files(merger,lista_arquivos):

    for arquivo in lista_arquivos:
        if ".pdf" in arquivo:
            merger.append(f"pdfs_mesclar/{arquivo}")
    merger.write(f"PDF_Final.pdf")

def main():
    merger = connection()
    lista_arquivos = finding_files()
    merging_files(merger,lista_arquivos)

if __name__ == '__main__':
    main()