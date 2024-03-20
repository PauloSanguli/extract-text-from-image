"""extract text from image with pytesseract"""
from assets.__path__ import PATH
from PIL import Image
import pytesseract

import os

from dotenv import load_dotenv

from tkinter.filedialog import askdirectory



def extract_text(img: str) -> None:
    """read text"""
    try:
        pytesseract.pytesseract.tesseract_cmd = os.getenv("PATH-TESSERACT")
        text_image = pytesseract.image_to_string(Image.open(f"{PATH}\{img}.jpg"))
    except:
        print("Image or cmd tesseract dont finded!")
    else:    
        dir_image = "contents"
        path = askdirectory()

        if path:
            dir_image = path
            
        write_txt(
            text=text_image,
            dir_image=dir_image,
            img=img
        )
        
def write_txt(text: str, dir_image, img) -> None:
    """write in txt file"""
    with open(f"{dir_image}/{img}.txt", "w") as file:
        file.writelines(text)
        file.close()



if __name__ == '__main__':
    load_dotenv()

    extract_text("img2")
