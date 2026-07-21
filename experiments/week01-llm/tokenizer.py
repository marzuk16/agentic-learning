# import tiktoken
# open ai tokenizer encoding
# encoding = tiktoken.get_encoding("cl100k_base") # auto choose model specific encoding
# encoding = tiktoken.encoding_for_model("gpt-4o") # model specific encoding

# Text to token
# text = "Hello, World!"
# tokens = encoding.encode(text)


# Token to text
# tokens = [9906, 11, 4435, 0]
# text = encoding.decode(tokens)


# accurate token count for `Qween3-8B` model
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "Qwen/Qwen3-8B"
)

tokens = tokenizer.encode("Hello World")
text = tokenizer.decode(tokens)

print(tokens)
print(len(tokens))

print(text)

# Print each token and its decoded string
for token in tokens:
    print(token, tokenizer.decode([token]))