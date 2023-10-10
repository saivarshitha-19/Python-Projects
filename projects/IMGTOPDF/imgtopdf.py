from fpdf import FPDF
pdf=FPDF()
imagelist = ['image1.png']
for image in imagelist:
 pdf.add_page()
 pdf.image(image,100,100,75,75)
 pdf.output('varshitha.pdf','f')