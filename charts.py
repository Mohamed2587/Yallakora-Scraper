import matplotlib.pyplot  as plt
import pandas  as pd 
import arabic_reshaper
from bidi  import get_display
import logging
class Charts ():
    def __init__ (self,csv):
        self.csv =  csv 
    def reader(self):
        # نعمل الرسومات البيانية لتوضيح عدد مباريات كل بطولة
        read  = pd.read_csv(self.csv)
        #نعمل Bar chart
        champions = []
        for r in read['Champion'].to_list():
            re_shape = arabic_reshaper.reshape(r)
            ar_champion = get_display(re_shape)
            champions.append(ar_champion)
        try:
            plt.figure(figsize=(10,10))
            plt.title('Bar Report')
            plt.barh(champions ,read['Amount'].to_list())
            plt.tight_layout()
            plt.savefig('Barh.png')
            plt.close()
            logging.info('Barh chart done')
        except Exception as e:
            logging.error( e +'فيه مشكلة ف الBarh chart')
        
        #Pie chart
        try:
            plt.figure(figsize=(7,7))
            plt.title('Pie Report')
            plt.pie(read['Amount'].to_list(),labels=champions,autopct='%1.1f%%')
            plt.tight_layout()
            plt.legend(loc = 'best',title = 'Champions')
            plt.savefig('Pie.png')
            plt.close()
            logging.info('Pie chart done')
        except Exception as e :
            logging.error(e + 'حصل مشكلة ف ال pie chart')
        
