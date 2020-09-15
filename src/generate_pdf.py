
from fpdf import FPDF
required=False,
def gen_PDF(dateFrom,dateTo):
    
    pdf2 = FPDF('P','mm','A4')
    pdf2.add_page()
    pdf2.set_font('Arial', 'B', 16)
    pdf2.cell(190, 10, f"Evolución de las acciones de Apple desde {dateFrom} hasta {dateTo}",1,1,'C')
    pdf2.set_font('Arial', '',10)
    pdf2.cell(185, 10, f'Este reporte muestra la evolución de las acciones de Apple desde {dateFrom} hasta {dateTo}.','',1,'L')
    pdf2.cell(192, 10, f'En el segundo gráfico se aprecia una mayor tendencia al alza en la valoración de dicha entidad frente al Nasdaq-100,','',1,'L')
    pdf2.cell(193, 10, f'que agrupa a las 100 empresas tecnológicas más relevantes en EEUU. ','',1,'L')
    pdf2.image('output/candleplot.png',x=38, y=47, w=150)
    pdf2.image('output/lineplot.png',x=45, y=140, w=145)
    pdf2.image('output/statistics.png',x= 30, y=235, w=80)
    pdf2.image('output/models.png',x= 120, y=235, w=60)
    pdf2.output("output/report.pdf", "F")
    print("pdf correctly exported!")
 