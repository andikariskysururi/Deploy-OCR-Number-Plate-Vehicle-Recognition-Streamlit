import streamlit as st
from PIL import Image
import pandas as pd
from ultralytics import YOLO
import io

#Load Model
classifier = YOLO(r"C:\Users\dika\OneDrive\Documents\OCR Deploy\best_v5l.pt")

def upload_image():
    image_uploaded = st.file_uploader("Upload Your Image")
    if image_uploaded is not None:
        # Membaca data dari objek file uploader sebagai BytesIO
        image_bytes = io.BytesIO(image_uploaded.getvalue())
        # Membuka gambar dengan PIL
        try:
            image = Image.open(image_bytes)
            st.image(image)
            return image
        except Exception as e:
            st.error(f"Error: {e}")
    return None

def convert(i):
  if i == '0':
    return 'A'
  elif i == '1':
    return 'B'
  elif i == '2':
    return 'C'
  elif i == '3':
    return 'D'
  elif i == '4':
    return 'E'
  elif i == '5':
    return 'F'
  elif i == '6':
    return 'G'
  elif i == '7':
    return 'H'
  elif i == '8':
    return 'I'
  elif i == '9':
    return 'J'
  elif i == '10':
    return 'K'
  elif i == '11':
    return 'L'
  elif i == '12':
    return 'M'
  elif i == '13':
    return 'N'
  elif i == '14':
    return 'O'
  elif i == '15':
    return 'P'
  elif i == '16':
    return 'Q'
  elif i == '17':
    return 'R'
  elif i == '18':
    return 'S'
  elif i == '19':
    return 'T'
  elif i == '20':
    return 'U'
  elif i == '21':
    return 'V'
  elif i == '22':
    return 'W'
  elif i == '23':
    return 'X'
  elif i == '24':
    return 'Y'
  elif i == '25':
    return 'Z'
  elif i == '26':
    return '0'
  elif i == '27':
    return '1'
  elif i == '28':
    return '2'
  elif i == '29':
    return '3'
  elif i == '30':
    return '4'
  elif i == '31':
    return '5'
  elif i == '32':
    return '6'
  elif i == '33':
    return '7'
  elif i == '34':
    return '8'
  elif i == '35':
    return '9'
  else:
    return " "

def BikinPlat(x):
  tmp=''
  c= 0
  for i in x:
    if c < 8:
      tmp = tmp + convert(i)
    else:
      tmp = tmp
    c = c+1

  return tmp

def convert_res(pred):
    for i in pred:
        kelas = pd.DataFrame(i.boxes.cls.cpu().numpy()).astype(int)
        kelas = kelas.rename(columns={0:'kelas'})
        titik = pd.DataFrame(i.boxes.xywhn.cpu().numpy())
        titik = titik.rename(columns={0:'x', 1:'y', 2:'w', 3:'h'})
        titik= titik.join(kelas).sort_values('x', ascending=True)
    plat = titik['kelas'].astype(str).tolist()
    return BikinPlat(plat)

def predict_ocr(image_uploaded):
    result = convert_res(classifier.predict(image_uploaded))
    return result
        
def main():
    st.title("OCR_Project")
    st.write("This project will help you to identify every alphanumeric digit in number plate vehicle")
    image = upload_image()
    result = ""
    if st.button("Predict"):
        result = predict_ocr(image)
    st.success("The Plate Number Digit is : {}".format(result))
    print(result)
    


if __name__ == "__main__":
    main()
    
