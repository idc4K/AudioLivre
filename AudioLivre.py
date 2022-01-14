import pyttsx3
import PyPDF2


#ouverture du fichier
Livre = open("dci.pdf", "rb")

#lecture du pdf
lecture_pdf = PyPDF2.PdfFileReader(Livre)

#nombre de page
num_pages = lecture_pdf.numPages

play = pyttsx3.init()
print("lecture du PDF en audio")

for num in range(0,num_pages):
	page = lecture_pdf.getPage(num)
	donnee = page.extractText()

	play.say(donnee)
	play.runAndWait()