import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('aquarium-6506130665bf.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open("aquarium").sheet1
values_list=wks.row_values(2)
print values_list
