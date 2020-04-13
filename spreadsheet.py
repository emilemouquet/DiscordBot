import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('FeuillePerso.json', scope)
client = gspread.authorize(creds)

sheet = client.open('feuilledeperso').sheet1

pp = pprint.PrettyPrinter()
value = sheet.cell(2,3)
pp.pprint((value).value)
