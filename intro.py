introduction = input("please specify your details: ")
wordcount = 1
charactercount = 0

for character in introduction:
    charactercount += 1
    # print(charactercount)
    if character == " ":
        wordcount += 1
        # print(wordcount)

print(charactercount)
print("word count is: ", wordcount)