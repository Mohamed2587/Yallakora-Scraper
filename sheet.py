import pandas as pd 
import logging

class Csv_Sheet():
    def __init__(self,data):
        self.data = data
    def sheets(self):
        try :
            csv_file = pd.DataFrame(self.data)
            csv_file.to_csv('matches_report.csv',index=False,encoding='utf-8-sig')
            match_report = pd.read_csv('matches_report.csv')
            logging.info('ملف  الماتشات و النتايج اتعمل')
        except Exception as e :
            logging.error( e +'الملف متعملش')
            raise

        #نعمل ملف نحط فيه عدد مباريات كل  بطولة 
        try:
            num_matches = pd.DataFrame(match_report["Champion title"].value_counts().reset_index())
            num_matches.columns = ['Champion','Amount']
            num_matches.to_csv('Champions.csv',index=False,encoding='utf-8-sig')
            logging.info('تم عمل الملف (عدد مباريات كل بطولة)')
        except Exception as e:
            logging.error( e +'ملف عدد مباريات كل بطولة متعملش ')
            raise
        