import gspread
from PIL import Image, ImageDraw, ImageFont
from oauth2client.service_account import ServiceAccountCredentials
i = 1
scope = ['https://www.googleapis.com/auth/drive.readonly']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json',scope)
client = gspread.authorize(credentials)
sheet = client.open('PSOC WORKSHOP').worksheet('Certificate of Participation')
data = sheet.row_values(i)
sheet1 = client.open('PSOC WORKSHOP').worksheet('Certificate of Appreciation')
data1 = sheet1.row_values(i)
sheet2 = client.open('PSOC WORKSHOP').worksheet('Certificate of Merit')
data2= sheet2.row_values(i)
for m in range(3):
	if m==0:
		while data[0] != '0':
			data = sheet.row_values(i)
			image = Image.open('FINAL.png')
			draw = ImageDraw.Draw(image)
			font = ImageFont.truetype('Calibri.ttf', size=150)
			(x, y) = (1300, 1000)
			color = 'rgb(0, 0, 0)' # white 
			draw.text((x, y), data[0], fill=color, font=font)
			image.save("C:/analog/praticipation/"+data[0]+'.png')
			i=i+1
	if m==1 :
		i=1
		while data1[0] !='0':
			data1 = sheet1.row_values(i)
			image = Image.open('FINAL.png')
			draw = ImageDraw.Draw(image)
			font = ImageFont.truetype('Calibri.ttf', size=150)
			(x, y) = (1300, 1000)
			color = 'rgb(0, 0, 0)' # white 
			draw.text((x, y), data1[0], fill=color, font=font)
			image.save("C:/analog/merit/"+data1[0]+'1.png')
			i=i+1
	if m==2 :
		i=1
		while data2[0] !='0':
			data2 = sheet2.row_values(i)
			image = Image.open('FINAL.png')
			draw = ImageDraw.Draw(image)
			font = ImageFont.truetype('Calibri.ttf', size=150)
			(x, y) = (1300, 1000)
			color = 'rgb(0, 0, 0)' # white 
			draw.text((x, y), data2[0], fill=color, font=font)
			image.save("C:/analog/appreciation/"+data2[0]+'2.png')
			i=i+1