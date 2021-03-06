from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import mm, inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image

import xlrd

# excel inputs
# extract a particular row value

loc = ("tc_input.xls")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)

print(sheet.row_values(1))



pdf = canvas.Canvas('tc.pdf',pagesize=letter)
pdf.setTitle('serial no')
# help scale
def drawMyRuler(pdf):
    pdf.drawString(100,780, 'x100')
    pdf.drawString(200,780, 'x200')
    pdf.drawString(300,780, 'x300')
    pdf.drawString(400,780, 'x400')
    pdf.drawString(500,780, 'x500')

    pdf.drawString(10,100, 'y100')
    pdf.drawString(10,200, 'y200')
    pdf.drawString(10,300, 'y300')
    pdf.drawString(10,400, 'y400')
    pdf.drawString(10,500, 'y500')
    pdf.drawString(10,600, 'y600')
    pdf.drawString(10,700, 'y700')
    pdf.drawString(10,800, 'y800') 
# drawMyRuler(pdf)

# for font in pdf.getAvailableFonts():
#     print(font)
pdfmetrics.registerFont(
    TTFont('Times-New-Roman-Bold','times-new-roman-bold.ttf')
)
pdf.setFont('Times-New-Roman-Bold',22.5)
# title
pdf.drawImage('logo.png', 25, 730,width=0.77*inch, height=0.86*inch ,mask='auto')
pdf.drawCentredString(320,770,'PRIYADARSHINI ENGINEERING COLLEGE')
pdfmetrics.registerFont(
    TTFont('Times-New-Roman','times-new-roman.ttf')
)
pdf.setFont('Times-New-Roman',12)
pdf.drawCentredString(320,757,'''(Approved by AICTE, New Delhi & Permanently Affiliated to Anna University, Chennai)''')
pdf.drawCentredString(320,744,'''Chettiyappanur Village & Post, Vaniyambadi – 635 751, Tirupattur Dt.''')

pdf.setFont('Times-New-Roman',10)
pdf.drawCentredString(320,728,'''Web: www.priyadarshini.net.in | E-Mail: principal@priyadarshini.net.in''')
pdf.drawCentredString(320,717,'''Phone: 04174 - 227591 / 228477 / 228972''')
pdf.setFont('Times-New-Roman-Bold',14)
pdf.drawCentredString(320,698,'''TRANSFER CERTIFICATE''')
pdf.line(235,697,409,697)

pdf.setFont('Times-New-Roman',12)
pdf.drawString(25,665,'Sl. No. '+'4253')
pdf.drawString(440,665,'Admission No.:'+'01432')

# form line-space -25 units
pdf.drawString(24,640,'''1. Name of the Student (in Block Letters)''')
pdf.drawString(300,642,'''      Sudharsan T''')
pdf.drawString(300,640,''': …………………………………………………………..''')
pdf.drawString(24,615,'''2. Name of the Parent or Guardian''')
pdf.drawString(300,617,'''      Thiyagarajan''')
pdf.drawString(300,615,''': …………………………………………………………..''')
pdf.drawString(24,590,'''3. Nationality, Religion and Caste''')
pdf.drawString(300,592,'''      Hindhu''')
pdf.drawString(300,590,''': …………………………………………………………..''')
pdf.drawString(24,565,'''4. Community : Whether he/she belongs to''')
pdf.drawString(24,550,'''   Adi Dravida(Scheduled Caste or ''')
pdf.drawString(24,535,'''   Scheduled Tribe). Backward Class / ''')
pdf.drawString(24,520,'''   Most BackwardClass / Denotified Tribes''')
pdf.drawString(300,522,'''      No''')
pdf.drawString(300,520,''': …………………………………………………………..''')

pdf.drawString(24,495,'''5. Sex''')
pdf.drawString(300,495,''': …………………………………………………………..''')

pdf.drawString(24,470,'''6. Date of Birth as entered in the admission
Register ''')
pdf.drawString(24,455,'''   in figures and words''')
pdf.drawString(300,455,''': …………………………………………………………..''')

pdf.drawString(24,430,'''7. Personal marks of Identification''')
pdf.drawString(300,430,''': …………………………………………………………..''')

pdf.drawString(24,405,'''8. Date of admission and course in which''')
pdf.drawString(24,390,'''   Admitted (the year to be entered in words)''')
pdf.drawString(300,390,''': …………………………………………………………..''')

pdf.drawString(24,365,'''9. a.) Class in which the Student was studying at''')
pdf.drawString(24,350,'''   the time of leaving(in words)''')
pdf.drawString(300,350,''': …………………………………………………………..''')
pdf.drawString(24,333,'''   b.)  Course offered''')
pdf.drawString(300,333,''': …………………………………………………………..''')
pdf.drawString(24,315,'''   c.)  Medium of Study''')
pdf.drawString(300,315,''': …………………………………………………………..''')

pdf.drawString(24,295,'''10. Whether qualified for Promotion''')
pdf.drawString(300,295,''': …………………………………………………………..''')

pdf.drawString(24,270,'''11. Whether the student has paid all the fees to the''')
pdf.drawString(24,255,'''    College''')
pdf.drawString(300,255,''': …………………………………………………………..''')

pdf.drawString(24,230,'''12. Whether the Student was in receipt of any''')
pdf.drawString(24,215,'''    Scholarship (Nature of the scholarship to be''')
pdf.drawString(24,200,'''    Specified) or Educational Concessions''')
pdf.drawString(300,200,''': …………………………………………………………..''')

pdf.drawString(24,175,'''13. Date on which the Student actually left the''')
pdf.drawString(24,150,'''    College''')
pdf.drawString(300,150,''': …………………………………………………………..''')

pdf.drawString(24,125,'''14. The Student’s Conduct and Character''')
pdf.drawString(300,125,''': …………………………………………………………..''')

pdf.drawString(24,100,'''15. Date on which for Transfer Certificate was ''')
pdf.drawString(24,85,'''    made on behalf the Student by the parent or''')
pdf.drawString(24,70,'''    guardian''')
pdf.drawString(300,70,''': …………………………………………………………..''')





pdf.setFont('Times-New-Roman-Bold',12)
pdf.drawString(25,50,'''Place : Vaniyambadi''')
pdf.drawString(25,30,'''Date : 5/3/2021''')
pdf.drawString(440,30,'''Signature of the Principal''')
pdf.save()
