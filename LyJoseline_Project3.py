article = open("article.txt", "r")
uniq = set()
for line in article:
    line = line.rstrip('''punctation goes here''')
    for word in line:
        if word not in uniq:
            uniq.add(word)