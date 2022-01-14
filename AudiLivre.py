import pyttsx3
import PyPDF2


#ouverture du fichier
Livre = open("idc.pdf", "rb")

#lecture du pdf
lecture_pdf = PyPDF2.PdfFileReader(book)

#nombre de page