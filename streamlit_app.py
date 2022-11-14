import streamlit as st
import cv2
import pandas as pd
""" ## There is title
    # There is subtitle
"""
img = cv2.imread("C:/Users/ADMIN/Desktop/cat.jpeg",cv2.COLOR_BGR2RGB)
st.image(img)