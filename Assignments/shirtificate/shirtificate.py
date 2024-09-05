from PIL import Image
from fpdf import FPDF, Align

name = input('Name: ')

image = Image.open('shirtificate.png')

size = image.size

class PDF(FPDF):
    def add_image(self):
        self.image('shirtificate.png', w = 190, h = 190 * size[1] / size[0], x = Align.C, y = 65)

    def add_header(self):
        self.set_font("helvetica", "B", 40)
        self.set_text_color(r = 0, g = 0, b = 0)
        self.cell(text = 'CS50 Shirtificate', w = 190, h = 50, align = Align.C)

    def add_shirt_text(self, name):
        self.set_font("helvetica", "B", 30)
        self.set_text_color(r = 255, g = 255, b = 255)
        self.text(x = 105 - len(name) * 3, y = 150, text=name)
        # self.cell(text = name, w = 210, h = 100, align = Align.C)

    def render_pdf(self):
        self.output('shirtificate.pdf')


pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.add_header()
pdf.add_image()
pdf.add_shirt_text(name)
pdf.render_pdf()

