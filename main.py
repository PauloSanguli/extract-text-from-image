"""extract text from image with pytesseract"""
from assets.__path__ import PATH
from PIL import Image
import pytesseract

import os

from dotenv import load_dotenv



def extract_text(img: str) -> None:
    """read text"""
    try:
        pytesseract.pytesseract.tesseract_cmd = os.getenv("PATH-TESSERACT")
        text_image = pytesseract.image_to_string(Image.open(f"{PATH}\{img}.jpg"))
    except:
        print("Image or cmd tesseract dont finded!")
    else:    
        with open(f"contents/{img}.txt", "w") as file:
            file.writelines(text_image)
            file.close()


if __name__ == '__main__':
    load_dotenv()

    extract_text("img1")
