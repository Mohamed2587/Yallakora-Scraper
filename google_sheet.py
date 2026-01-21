import gspread
import pandas as pd

class Google_Sheet:
    def make_sheet(data):
        SA = gspread.service_account(filename='My_file.json')

        SH = SA.open_by_url('https://docs.google.com/spreadsheets/d/17IH8ILWmOqWRBDKBNCJTQCQ9HEFx_oQGTkLla7qJ-Jw/edit?gid=0#gid=0').sheet1

        SH.clear()
        
        df = pd.DataFrame(data)
        
        SH.update([df.columns.values.tolist()] + df.values.tolist())
        