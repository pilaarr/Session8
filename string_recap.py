text = "I like cats"

print(text)
print(text[0], text[7])
  # text[7] = 'r' I cannot change the string
print(text[7:])
# text = text[:7] + "sneaky r" + text[8:] + ". How about you?"
#
# print("I produced this result:", text)
print(f"the result of 2+3={2+3}")  # string with code inside
print(f"I produced this result differently: {text[:7]}sneaky r{text[8:]}")