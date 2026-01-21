import  logging
import requests
from bs4 import BeautifulSoup


def Trying(var,info,warning,error):
    try:
        if var:
            logging.info(info)
        else:
            logging.warning(warning)
        
    except Exception as e :
        logging.error(error +  e)     
        

class Scraping():
    
    def scr(self , day):
        
        try:
            respond = requests.get(f'https://www.yallakora.com/match-center?date={day}',timeout=12)
            respond.raise_for_status()
            logging.info('تم الوصول للموقع')
        except Exception as e  :
            logging.error(f'مدخلناش الموقع{e} ')
            raise
        
                
        # نخلي البرنامج يشوف كود الموقع و يبدأ يطلع منه البيانات  
        soup = BeautifulSoup(respond.text,'lxml')

        matches = soup.find_all('div' , class_ = 'matchCard')
        self.data = []
        for champ in matches :
            champion_title = champ.find('h2').text.strip()
            Trying(champion_title,f'تم  الوصول لعنوان البطولة {champion_title} ','موصلناش لاسم البطولة','اسم  البطولة مش موجود')
            all_matches = champ.find('div',class_='ul').find_all('div',class_ = 'allData')
            Trying(all_matches,'وصلنا لجميع مباريات البطولة','البطولة فاضية','موصلناش لمباريات البطولة')
            for i in all_matches:
                match_teamA = i.find('div',class_ = 'teamA').text.strip()
                Trying(match_teamA,f'وصلنا لاول  فريق ف المباراة {match_teamA}','اول فريق مش  موجود','الفريق  الاول موصلش')
                match_teamB = i.find('div',class_ = 'teamB').text.strip()
                Trying(match_teamB , f'وصلنا ل تاني فريق {match_teamB}','اسم الفريق الثاني مش موجود','اسم الفريق التاني مقدرناش نوصله')
                match_score = i.find('div',class_  = 'MResult').find_all('span',class_ = 'score')
                Trying(match_score,'وصلنا لنتيجة المباراة','نتيجة المباراة  فاضية','موصلناش لنتيجة المباراة')
                match_time = i.find('div',class_  = 'MResult').find('span',class_ = 'time').text.strip()
                Trying(match_time,'تم الوصول لوقت المباراة',"وقت المباراة فاضي","وقت المباراة مش  موجود")
                team_A_score =  match_score[0].text.strip()
                team_B_score =  match_score[1].text.strip()
                self.data.append({
                'Champion title' : champion_title,
                'Team A' : match_teamA,
                'Team B' : match_teamB,
                'Score' :f' {team_A_score} - {team_B_score}',
                'time' : match_time
                })
     
        return  self.data