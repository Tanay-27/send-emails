# Satutary Warnings
#This program was created solely for personal use. The owner holds no credit or copyright for the codes or the libraries used. THe program is just an easy to use combination of libraries all of which were ethically downloaded and used.
#The sole purpose for sharing this was to reduce the effort or others to send multiple mails and small committees to send email. certificates by just providing the templates and list of names and email ids to which one needs to send an email.

#The use the files provided in this repository one needs to install the following libraries:-

#Yagmail - this is used to shorten and simplify the process of sending emails, each new email id needs to enter passowrd only once and it is then internally stored in a keyring form which is invisible and hence safe when just the code is shared.

#The following are the functions to read and draw name on a template image 
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# CSV 
This is used to read csv files

# string
This is used to typecast the name so as to maintain the alignment.

# U S E A G E
The file contains 3 functions:-
1> csv read:- this helps the user to simply give the csv file, specify the colloumn number containing the name and email id and it returns a list of tuples containing (name,email) this can be skipped is use, has been provided for novice users.

2> Mail Generation:- This is simply takes in the email address subject content and the attachment (if exists) and sned the email. In case the user wants to send custom certificates for each name the would have to use the certificate generation function before this and a file in the format specified by the user shall be generated with the name also as the filename which makes it look more personalised and avoids confusion. The first time one logs into this file they will have to specify their email id and passowrd and the keyring in the yagmail will save it for further use unless mentioned. 

3> Certificate Generation:- This takes emailId, fontname, size , RGB values for colour, and template image as input and provides a saved certificate ready to dispatch. This has been given a number of input just for the sake of flexibility of choice. 
There is one more input that is taken, that is the coordinate values where one wishes to draw the text. This is a slight difficulty which may require some trial and error to reach perfect fit for your own template. The owner had taken center of the certificate width as the common starting coordinate and subtracted the pixel width of each alphabet from the name half times for each side and thus Maintained the alignment. 
The owner has left the code as it is so that the reader may easily comprehend what is being said.
Any queries regarding the use can be emailed at the below address.

Email- tanayshah@live.com
P.S. Please mention send emails repository in the subject

Cheers!
Happy Coding
