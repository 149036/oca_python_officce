from docx import Document
from docx.shared import Inches
document = Document()

document.add_heading('簡単なWordドキュメントのタイトルasdasdsads', 0)
document.add_paragraph('簡単なWordドキュメントのテキスト')

document.save('sample.docx')

