import requests


# the simplest way to work with a file!
fp = open("text.txt")  # store the file into a variable
print(fp.read())
fp.close()

fp = open("text.txt")

# files are iterable!
for line in fp:
    # print(line, end="") so it does not add an extra line after line
    # print(line[:-1]) same thing
    print(line.rstrip())  # these are three ways to get rid of the enter after line

r = requests.get("https://www.gutenberg.org/cache/epub/345/pg345.txt")
# print(r.text)
# print(r.content) this one is not decoded
fp = open("dracula.txt", "wb")  # wb is open for writing (decodes the content)
fp.write(r.content)
fp.close()