text_file = open("twain.txt")
word_counts = {}

for line in text_file:
    line = line.replace("--", " ")
    words = line.split(" ")
    for word in words:
        word
        #strip all punctuation and lowercase word
        word = word.strip("\'\"\n\t-,./?!:;()*[]_").lower()

        # #if word not found, add it
        # if word not in word_counts:
        #     word_counts[word] = 1

        # # otherwise, word already in word_counts, so increment count
        # else:  
        #     word_counts[word] += 1

        #if word not found, add it
        if word_counts.get(word) == None:
            word_counts[word] = 1

        # otherwise, word already in word_counts, so increment count
        else:
            word_counts[word] += 1

for word, count in word_counts.items():
    print word, count