song = """"""

word_count = {}

for word in song.lower().split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

##programa pra saber quantas vezes uma palavra se repete em uma musica/texto