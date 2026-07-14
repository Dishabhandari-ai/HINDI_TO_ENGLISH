from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class HindiTranslator:

    def __init__(self):

        print("Loading Translation Model...")

        self.model_name = "Helsinki-NLP/opus-mt-hi-en"

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            self.model_name
        )

        print("Translation Model Loaded Successfully!")

    def translate(self, hindi_text):

        inputs = self.tokenizer(
            hindi_text,
            return_tensors="pt"
        )

        outputs = self.model.generate(
            **inputs,
            max_length=100
        )

        english = self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        return english


if __name__ == "__main__":

    translator = HindiTranslator()

    hindi = input("Enter Hindi text: ")

    english = translator.translate(hindi)

    print("\nEnglish Translation:")
    print(english)