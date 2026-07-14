import torch

from PIL import Image

from transformers import (
    TrOCRProcessor,
    VisionEncoderDecoderModel
)


class HindiOCR:

    def __init__(self):

        print("Loading TrOCR model...")

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model_name = "paudelanil/trocr-devanagari-2"
        self.processor = TrOCRProcessor.from_pretrained(self.model_name)
        self.model = VisionEncoderDecoderModel.from_pretrained(self.model_name).to(self.device)
        self.model.eval()
        print(f"Using device: {self.device}")
        print("Model Loaded Successfully!")

    def recognize(self, image_path):

        print(f"\nReading image: {image_path}")

        image = Image.open(image_path).convert("RGB")

        pixel_values = self.processor(
            image,
            return_tensors="pt"
        ).pixel_values

        print("Tensor Shape:", pixel_values.shape)

        pixel_values = pixel_values.to(self.device)

if __name__ == "__main__":

    ocr = HindiOCR()

    ocr.recognize("outputs/processed_sample1.png")   