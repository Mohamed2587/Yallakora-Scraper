from fpdf import FPDF

import logging
class Pdf():
        #نعمل ملف pdf نحط فيه الرسومات 
    def  report(self):
        try:
            pdf = FPDF(format='A3')
            pdf.add_page()
            pdf.set_font('Arial' ,size = 40)
            text_height = pdf.font_size
            page_height = pdf.h
            pdf.set_xy(0,(page_height -text_height)/2)
            pdf.cell(0,10,txt='Report',ln = 0 , align='C' )
            pdf.add_page()
            pdf.image('Barh.png')
            pdf.image('Pie.png')
            pdf.output('Report of Matches.pdf')
            logging.info('pdf done')
        except Exception as e :
            logging.error(e + 'حصل مشكلة ف الpdf')