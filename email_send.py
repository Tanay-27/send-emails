import yagmail
import csv
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def certicicate_generation(name_to_write):
    img = Image.open("certi_base.jpg")
    draw = ImageDraw.Draw(img)
    font_name,size = input('Enter name of Font file(.ttf): '),input('Enter size ')
    selectFont = ImageFont.truetype("times-new-roman.ttf", size=90)
    text = name_to_write
    length = len(text) // 2 - 1
    lenght = 800 - 37 * length
    draw.text((lenght, 525), text, (100, 0, 200), font=selectFont)
    cn = text + '.pdf'
    img.save(cn, "PDF", resolution=500.0)

yag = yagmail.SMTP('nssvitw@gmail.com', 'nss2020login')
file_name = input('Enter file name: ')
subject = input('Enter Subject: ')
body = "Hey Participant: thankyou for attending the session, following is the certificate attached, \n reply to tanay when u get this message \n\n Regards Python"
with open(file_name) as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    yag = yagmail.SMTP('nssvitw@gmail.com')
    for name, email in reader:
        certicicate_generation(name)
        certi = name+'.pdf'
        yag.send(
            to = email,
            subject = subject,
            contents =body,
            attachments = certi,
        )
