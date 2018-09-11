""" CP1404 Prac 05 """

text = "this is a collection of nice words this is a fun thing it is"
words = text.split(" ")
words_to_count = {}
word_length = 0
for word in words:
    if word in words_to_count:
        words_to_count[word] += 1
    else:
        words_to_count[word] = 1
    if len(word) > word_length:
        word_length = len(word)
# print("longest word is", str(word_length))
for word in sorted(words_to_count):
    print("{:{}} : {}".format(word, word_length, words_to_count[word]))
