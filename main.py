import pyttsx3
import PyPDF2
# book
book = open('the_road_to_reality.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
page = pdfReader.getPage(1122)
text = page.extractText()
print(pages)

# speaker
speaker = pyttsx3.init()
speaker.setProperty("rate", 150)
speaker.setProperty('volume', 0.7)
speaker.say(text)
speaker.runAndWait()

book.close()