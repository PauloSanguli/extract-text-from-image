"""extract text from image with pytesseract"""
from assets.__path__ import PATH
from PIL import Image
import pytesseract

import os

from dotenv import load_dotenv

from tkinter.filedialog import askdirectory




class ProcessImage:
    @staticmethod
    def extract_text(img: str) -> None:
        """read text"""
        try:
            pytesseract.pytesseract.tesseract_cmd = os.getenv("PATH-TESSERACT")
            print(f"[INFO]: EXTRATING TEXT FROM IMAGE NAME '{img}'...")
            text_image = pytesseract.image_to_string(Image.open(f"{PATH}\{img}.jpg"))
        except:
            print("Image or cmd tesseract dont finded!")
        else:    
            ProcessImage.write_txt(
                text=text_image,
                dir_image="contents",
                img=img
            )
            
    @staticmethod
    def write_txt(text: str, dir_image, img) -> None:
        """write in txt file"""
        with open(f"{dir_image}/{img}.txt", "w") as file:
            file.writelines(text)
            file.close()
        print("[INFO]: TEXT EXTRACTED WITH SUCESS AND SAVED!")
        print(f"[INFO]: TEXT EXTRACTED SAVED IN '{dir_image.upper()}'")



if __name__ == '__main__':
    load_dotenv()

    ProcessImage.extract_text(img="img3")
