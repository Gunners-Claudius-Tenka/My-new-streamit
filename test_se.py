#先写一下这个计划吧
#1.摄像头 2.读取文件(dcm) 3.生成docx文件(不确定能不能行) 4.图像增强 5.考虑一下布局美观
import streamlit as st
from docx import Document
from docx.shared import Inches
from PIL import Image
import io
import tempfile
import os

st.markdown("<h1 style='font-family: 宋体; font-size: 24px; text-align: center;'>这是一个关于streamlit和opencv的练习网站</h1>", unsafe_allow_html=True)
picture = st.camera_input("Take a picture")
if picture:
    # 将图像数据转换为PIL图像
    image = Image.open(picture)
    # 创建一个临时文件
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    # 保存图像到临时文件
    image.save(temp_file.name, format='PNG')
    # 创建Word文档
    doc = Document()
    doc.add_picture(temp_file.name, width=Inches(4))  # 设置图片宽度

    # 保存Word文档到临时文件
    temp_doc_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
    doc.save(temp_doc_file.name)

    # 下载按钮
    st.download_button(
        label="Download Word Document",
        data=open(temp_doc_file.name, 'rb').read(),
        file_name='picture.docx',
        mime='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )

    # 删除临时文件
    os.remove(temp_file.name)
    os.remove(temp_doc_file.name)