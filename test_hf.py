from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "microsoft/trocr-base-handwritten"
)

print("Tokenizer loaded successfully!")