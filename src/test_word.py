from docx import Document
from docx.shared import Inches
document = Document()

document.add_heading('簡単なWordドキュメントのタイトルasdasdsads', 0)
document.add_paragraph('簡単なWordドキュメントのテキスト')

document.save('sample.docx')

document.add_picture('wsl.jpg', width=Inches(1.25))

document.save('sample.docx')
num = 0
for p in document.paragraphs:
    num += len(p.text)

print('文字数:',num)