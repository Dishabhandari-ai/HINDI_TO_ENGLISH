import pytesseract
from PIL import Image


class HindiOCR:

    def __init__(self):

        
        pytesseract.pytesseract.tesseract_cmd = (
            r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        )

        print("Hindi OCR Initialized Successfully!")

    def recognize(self, image_path):

       
        image = Image.open(image_path)

        
        # OEM 3 -> Best available engine
        # PSM 8 -> Treat image as a single word
        custom_config = r'--oem 3 --psm 8'

        text = pytesseract.image_to_string(
            image,
            lang="hin",
            config=custom_config
        )

      
        text = text.strip()

        return text


if __name__ == "__main__":

    ocr = HindiOCR()

    result = ocr.recognize("outputs/processed_sample2.png")

    print("Recognized Text:", result)