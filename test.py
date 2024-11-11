import streamlit as st
import pydicom
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math

st.header('这是一个测试dcm的文件')
# 使得matplotlib可以显示出中文
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
matplotlib.rcParams['font.size'] = 10

# 创建一个文件上传控件
uploaded_file = st.file_uploader("选择一个DICOM文件", type=['dcm'])
if uploaded_file is not None:
    ds = pydicom.dcmread(uploaded_file)
    info = ds
    I = ds.pixel_array
    # 创建一个Figure对象
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    # 在Figure对象中显示图像
    ax[0].imshow(I, cmap='gray')
    ax[0].set_title('原图像')
    ax[0].axis('off')  # 不显示坐标轴

    hist = np.histogram(I.flatten(), bins=256, range=(0, 255))
    # 灰度调整
    # 平均线性灰度变换
    w, h = I.shape
    t = math.sqrt((w + h) / 2)
    m = np.argmax(hist[0] >= t) + 1
    n = len(hist[0]) - np.argmax(np.flip(hist[0] >= t)) - 1

    I_eq = ((I - m) * 255 / (n - m))
    I_eq = np.clip(I_eq, 0, 255).astype(np.uint8)
    # 显示灰度变换后的图像
    ax[1].imshow(I_eq, cmap='gray', interpolation='nearest')
    ax[1].set_title('灰度变换后DICOM图片')
    ax[1].axis('off')  # 不显示坐标轴
    # 将Figure对象传递给st.pyplot()
    st.pyplot(fig)