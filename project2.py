from scraping import Scraping
from pdf import Pdf
from charts import Charts
import logging
from  sheet import Csv_Sheet
import argparse 
from datetime import datetime, date
from google_sheet import  Google_Sheet
logging.basicConfig(filename='match.log',level=logging.INFO,format = '%(asctime)s - %(levelname)s - %(message)s',filemode='a' ,encoding='utf-8' )
#  نحط اللينك اللي هنشتغل عليه و نخلي المستخدم يدخل اليوم اللي هو عايز المباريات فيه 
logging.info('Start')

parser = argparse.ArgumentParser(description= 'Scraping of Yalla koora, generate CSV report, Pdf report with  charts') 

parser.add_argument('--date',help = 'Enter day what you want matches in',default = date.today().strftime('%m/%d/%Y'))

args = parser.parse_args()
day= args.date

try :
    datetime.strptime(day,'%m/%d/%Y')
except ValueError:
    print ('Worng date form , Use this MM/DD/YYYY')
    exit()


scrap  = Scraping().scr(day)
Csv_Sheet(scrap).sheets()
Google_Sheet.make_sheet(scrap)
Charts('Champions.csv').reader()
Pdf().report()
logging.info('Progam is Done')
logging.info('End')
logging.info('-'*50)
