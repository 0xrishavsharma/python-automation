import pyttsx3, PyPDF2

pdfReader = PyPDF2.PdfReader(open("Lorem_ipsum.pdf", "rb"));
speaker =  pyttsx3.init()

for page_num in range(pdfReader.numPages):
  text = pdfReader.getPage(page_num).extractText()
  clean_text = text.strip().replace('/n', ' ')
  print("Cleaned Text", clean_text)
  
console.log("Good till now :)")
speaker.save_to_file(clean_text, 'Lorem_ipsum.mp3')
speaker.runAndWait()

speaker.stop()