import os
import streamlit as st
from PIL import Image
import tesserocr
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

def load_image(image_file):
    img = Image.open(image_file)
    return img

st.title("Image to text Application")
image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
if image_file is not None:
    file_details = {"filename":image_file.name, "filetype":image_file.type,
                  "filesize":image_file.size}
    st.write(file_details)
    img=load_image(image_file)
    st.image(img,width=250)
    classifier = tesserocr.image_to_text(img)
    new_title = '<p style="font-family:sans-serif; color:Green; font-size: 32px;">Image Information: {classifier}</p>'.format(classifier=classifier)
    st.markdown(new_title, unsafe_allow_html=True)