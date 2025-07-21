'''
基础版，可转换成pdf，图片比例有问题
'''
# from weasyprint import HTML
# import os
# os.environ['PATH'] += ';C:\msys64\mingw64\\bin\\'  # 将路径替换为您的 GTK+ 安装路径
#
# # 读取HTML文件
# html_file = "E:\JLSF2023-9-13-1\JLSF2023-9-13-1-6\Reports\\ReportPage_167.html"
#
# # 输出PDF文件
# pdf_file = "output.pdf"
#
# # 将HTML文件转换为PDF
# HTML(filename=html_file).write_pdf(pdf_file)
'''
增加功能，图片正常
'''
# from weasyprint import HTML, CSS
# import os
#
# # 添加GTK+路径
# os.environ['PATH'] += ';C:\\msys64\\mingw64\\\\bin\\\\'  # 请将路径替换为您的 GTK+ 安装路径
#
# # 读取HTML文件
# html_file = "E:\\JLSF2023-9-13-1\\JLSF2023-9-13-1-6\\Reports\\\\ReportPage_167.html"
#
# # 输出PDF文件
# pdf_file = "3.pdf"
#
# # 设置缩放比例
# scale = 0.9  # 设置缩放比例为1.5
#
# # 添加页眉
# header_html = '<h1 style="text-align: center;">西安海关缉私局</h1>'
#
# # 将HTML文件转换为PDF，并设置缩放比例和页眉
# HTML(filename=html_file).write_pdf(pdf_file, stylesheets=[CSS(string='@page { size: A4; margin: 1cm; }'),
#                                                            CSS(string='@page { @top-center { content: element(header); } }'),
#                                                            CSS(string='.header { position: running(header); }')],
#                                    zoom=scale, presentational_hints=[(header_html, '.header')])
#
# print("PDF文件生成成功！")
'''
添加页眉和页脚
'''
# from weasyprint import HTML, CSS
#
# # 读取HTML文件
# html_file = "E:\\JLSF2023-9-13-1\\JLSF2023-9-13-1-6\\Reports\\ReportPage_167.html"
#
# # 输出PDF文件
# pdf_file = "2.pdf"
#
# # 定义页眉和页脚样式
# header_html = '<h1 style="text-align: center;">My Header</h1>'
# footer_html = '<h2 class="page" style="text-align: center; color: black;"></h2>'
#
# # 将HTML文件转换为PDF，并自动添加页眉和页脚
# pdf = HTML(html_file).write_pdf(pdf_file, stylesheets=[
#     CSS(string='@page { size: A4; margin: 1cm; }'),
#     CSS(string='.page { counter-increment: page; } .page:after { content: counter(page); }'),
#     CSS(string=header_html),
#     CSS(string=footer_html)
# ])
#
# print("PDF文件生成成功！")
# import fitz  # PyMuPDF
#
# def add_page_numbers_and_header(pdf_input, pdf_output, header_text="Header"):
#     doc = fitz.open(pdf_input)
#
#     for page_number in range(len(doc)):
#         page = doc.load_page(page_number)
#         page_width = page.rect.width
#         page_height = page.rect.height
#         rotation = page.rotation  # 获取页面的旋转角度
#
#         # 添加页眉
#         page.insert_text((50, 10), header_text, fontsize=10, fontname="helv", color=(0, 0, 0), rotate=0)
#
#         # 计算文本框的中心位置
#         text_width = fitz.get_text_length("Page {}".format(page_number + 1), fontsize=8)
#         text_height = 20  # 文本框高度
#         x = (page_width - text_width) / 2
#         y = page_height - 30  # 距离底部的间距
#
#         # 如果页面被镜像并翻转了180度，将页码左右翻转，并旋转180度
#         if rotation == 180:
#             # 计算文本框的左上角位置
#             text_box = fitz.Rect(x + text_width, y, x, y + text_height)
#             text = "Page {}".format(len(doc) - page_number)
#             page.insert_textbox(text_box, text, fontsize=8, color=(0, 0, 0), align=1, rotate=180, fontname="helv", reset_rotation=False)
#         else:
#             # 计算文本框的中心位置
#             text_box = fitz.Rect(x, y, x + text_width, y + text_height)
#             text = "Page {}".format(page_number + 1)
#             page.insert_textbox(text_box, text, fontsize=8, color=(0, 0, 0), align=1, rotate=0, fontname="helv")
#
#     # 保存修改后的PDF
#     doc.save(pdf_output)
#     doc.close()
#
#     print("页码和页眉已添加到PDF文件中！")
#
# # 调用函数并传入参数
# pdf_input = "2.pdf"
# pdf_output = "output_with_page_numbers_and_header.pdf"
# header_text = "Confidential"  # 你想要添加的页眉文本
# add_page_numbers_and_header(pdf_input, pdf_output, header_text)
#coding=utf-8
'''
pdf文件添加页码，在底部成功添加
'''
# from PyPDF2 import PdfReader, PdfWriter
# import io
# from reportlab.pdfgen import canvas
#
# def add_page_numbers(input_pdf, output_pdf):
#     with open(input_pdf, 'rb') as pdf_in:
#         pdf_reader = PdfReader(pdf_in)
#         pdf_out = PdfWriter()
#
#         for page_num in range(len(pdf_reader.pages)):
#             page = pdf_reader.pages[page_num]
#             packet = io.BytesIO()
#             can = canvas.Canvas(packet)
#             can.drawString(10, 10, f"Page {page_num + 1}")  # 设置页码文本和位置
#             can.save()
#
#             packet.seek(0)
#             watermark_pdf = PdfReader(packet)
#             watermark_page = watermark_pdf.pages[0]
#
#             page.merge_page(watermark_page)
#             pdf_out.add_page(page)
#
#         with open(output_pdf, 'wb') as pdf_output:
#             pdf_out.write(pdf_output)
#
# # 设置输入和输出的文件名
# input_pdf = '3.pdf'
# output_pdf = 'output.pdf'
#
# # 调用添加页码函数
# add_page_numbers(input_pdf, output_pdf)

'''
添加页脚，页码改右边,单个文件
'''
# from PyPDF2 import PdfReader, PdfWriter
# import io
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch
# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.pdfbase import pdfmetrics
#
# def add_page_numbers(input_pdf, output_pdf,footstr):
#     with open(input_pdf, 'rb') as pdf_in:
#         pdf_reader = PdfReader(pdf_in)
#         pdf_out = PdfWriter()
#
#         for page_num in range(len(pdf_reader.pages)):
#             page = pdf_reader.pages[page_num]
#             packet = io.BytesIO()
#             can = canvas.Canvas(packet)
#             pdfmetrics.registerFont(TTFont('Microsoft YaHei', 'C:\Windows\Fonts\\msyh.ttc'))  # 注册SimSun字体
#             can.setFont("Microsoft YaHei", 8)  # 设置字体为SimSun，字号为12
#             # footstr = "江隆司法鉴定/XAHG缉私局/具体人名/案件编号"
#             # 添加页码在底部右侧
#             page_width = page.mediabox[2]
#             can.drawString(page_width - 50, 10, f"Page {page_num + 1}")  # 设置页码文本
#             # can.setFont("SimSun", 12)  # 设置字体为宋体，字号为12
#
#             # 添加页脚在底部左侧
#             can.drawString(50, 10, footstr.encode('utf-8'))  # 设置页脚文本
#
#             can.save()
#
#             packet.seek(0)
#             watermark_pdf = PdfReader(packet)
#             watermark_page = watermark_pdf.pages[0]
#
#             page.merge_page(watermark_page)
#             pdf_out.add_page(page)
#
#         with open(output_pdf, 'wb') as pdf_output:
#             pdf_out.write(pdf_output)
#
# # 设置输入和输出的文件名
# input_pdf = "刘\蜜丝cici-let's dietww(4205)--957_1.pdf"
# output_pdf = '刘\蜜丝cici-let\'s dietww(4205)--957_1(1).pdf'
# footstr = "江隆司法鉴定/XAHG缉私局/刘纯月/JLSF2024-3-4-2-18"
# # 调用添加页码函数
# add_page_numbers(input_pdf, output_pdf,footstr)

'''
批量转换
'''
from PyPDF2 import PdfReader, PdfWriter
import pandas as pd
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import filecmp
from weasyprint import HTML, CSS
import os
def html_to_pdf(html_file, pdf_file,footstr,savefile):
    # 添加GTK+路径
    os.environ['PATH'] += ';C:\\msys64\\mingw64\\\\bin\\\\'  # 请将路径替换为您的 GTK+ 安装路径

    # 设置缩放比例
    scale = 0.7  # 设置缩放比例为1.5

    # 控制图片样式，设定固定宽度和高度
    img_style = """
        img {
            max-width: 250px;  /* 设置图片最大宽度 */
            max-height: 200px; /* 设置图片最大高度 */
        }
    """

    # # 将HTML文件转换为PDF，并设置缩放比例、页眉和图片样式
    # HTML(filename=html_file).write_pdf(pdf_file, stylesheets=[
    #     CSS(string='@page { size: A4; margin: 1cm; }'),
    #     CSS(string='@page { @top-center { content: element(header); } }'),
    #     CSS(string='.header { position: running(header); }'),
    #     CSS(string=img_style)  # 添加图片样式
    # ], zoom=scale)
    try:
        # 将HTML文件转换为PDF，处理可能出现的图像问题
        HTML(filename=html_file).write_pdf(pdf_file, stylesheets=[
            CSS(string='@page { size: A4; margin: 1cm; }'),
            CSS(string='@page { @top-center { content: element(header); } }'),
            CSS(string='.header { position: running(header); }'),
            CSS(string=img_style)  # 添加图片样式
        ], zoom=scale)

        if not filecmp.cmp(html_file, pdf_file.replace('.html', '.pdf')):
            print(f"警告：HTML和PDF文件不一致，可能是因为图像问题。")
    except (OSError, IOError) as e:
        print(f"图像处理错误：{str(e)}，跳过当前图像。")
        # 输出PDF文件名，但跳过异常
        # output_pdf=pdf_file.split('.')[0]+'.pdf'
        # output_pdf_folder=output_pdf.replace(savefile,savefile+'/页码')
        # print(output_pdf)
        pass   # 跳过当前的输出PDF操作

    # output_pdf=save_file+'/(1)'+pdf_file
    output_pdf=pdf_file.split('.')[0]+'.pdf'
    output_pdf_folder=output_pdf.replace(savefile,savefile+'/页码')
    print(output_pdf)
    add_page_numbers(pdf_file,output_pdf_folder,footstr)
    print("PDF文件生成成功！")

def add_page_numbers(input_pdf, output_pdf, footstr):
    with open(input_pdf, 'rb') as pdf_in:
        pdf_reader = PdfReader(pdf_in)
        pdf_out = PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            packet = io.BytesIO()
            can = canvas.Canvas(packet)
            pdfmetrics.registerFont(TTFont('Microsoft YaHei', 'C:\Windows\Fonts\\msyh.ttc'))
            can.setFont("Microsoft YaHei", 8)

            page_width = page.mediabox[2]
            can.drawString(page_width - 50, 10, f"Page {page_num + 1}")
            can.drawString(50, 10, footstr.encode('utf-8'))

            can.save()

            packet.seek(0)
            watermark_pdf = PdfReader(packet)
            watermark_page = watermark_pdf.pages[0]

            page.merge_page(watermark_page)
            pdf_out.add_page(page)

        with open(output_pdf, 'wb') as pdf_output:
            pdf_out.write(pdf_output)


def get_files_with_keyword(folder_path, keyword):
    files_list = []
    for file_name in os.listdir(folder_path):
        if keyword in file_name:
            files_list.append(os.path.join(folder_path, file_name))

    return files_list


import re



def extract_string(file_name):
    pattern = r'(ReportPage_\d+)_?\d*\.html'
    match = re.match(pattern, file_name)
    if match:
        return match.group(1)
    else:
        return None

# 读取 xlsx 文件
data = pd.read_excel('张清鸿9月10.xlsx')    #替换嫌疑人有群聊名称的表格，群聊名称有.的使用空格替换
footstr1 = "江隆/XAHG缉私局/JLSF2024-11-12-1-1/ReportPage_996_20" #文档路径替换嫌疑人名字
folder_path = "C:\\Users\PC\Desktop\JLSF2024-11-12-1-1张临-手机\JLSF2024-11-12-1-1\JLSF2024-11-12-1-1\默认线索1_20241115103659\Reports"  #html保存的文件夹
save_file = "张清鸿9月10" #PDF保存的文件夹，需要新建文件夹，还需在下级新建（页码）文件夹。

for index, row in data.iterrows():
    link = row['link']  # 从 link 列获取输入文件名 #全都修改为link
    nick_name = row['群聊名称']  # 从群聊昵称列获取输出文件名  #需修改每个表格的名称
    keyword = link.split('.')[0]
    files = get_files_with_keyword(folder_path, keyword)
    if len(files) > 1:
        print("文件夹中包含多个文件符合条件：")
        for file in files:
            print(file)
            num=file.split('\\')[-1]
            footstr=footstr1+num.split('.')[0]
            num1=num.split('.')[0].replace('ReportPage_','-')
            new_name = f"{save_file}/{nick_name}-" + num1 + ".pdf"
            html_to_pdf(file, new_name,footstr,save_file)

    else:
        print("文件夹中没有或只有一个文件符合条件。")
        footstr=footstr1+link.split('.')[0]
        output_pdf = f"{save_file}/{nick_name}-{link.split('.')[0].replace('ReportPage_','-')}.pdf"
        # output_pdf=output_pdf.replace(' ','-')
        input_pdf=f'{folder_path}\\{link}'
        # add_page_numbers(input_pdf, output_pdf, footstr)
        html_to_pdf(input_pdf,output_pdf,footstr,save_file)


















