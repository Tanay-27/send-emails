import yagmail
import csv
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def certicicate_generation(name_to_write):
    img = Image.open("template.jpg")
    draw = ImageDraw.Draw(img)
    font_name,size = input('Enter name of Font file(.ttf): '),input('Enter size ')
    selectFont = ImageFont.truetype("textformat.ttf", size=90)
    text = name_to_write
    length = len(text) // 2 - 1
    lenght = 800 - 37 * length
    draw.text((lenght, 525), text, (100, 0, 200), font=selectFont)
    cn = text + '.pdf'
    img.save(cn, "PDF", resolution=500.0)

file_name = input('Enter file name: ')
subject = input('Enter Subject: ')
body = "content"
with open(file_name) as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    yag = yagmail.SMTP(yourgmail account)
    for name, email in reader:
        certicicate_generation(name)
        certi = name+'.pdf'
        yag.send(
            to = email,
            subject = subject,
            contents =body,
            attachments = certi,
        )
