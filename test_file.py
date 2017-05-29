with open('hindi/21_utf8.txt.norm') as f:
    print f
    words = [word for line in f for word in line.split()]

    print words[:10]
