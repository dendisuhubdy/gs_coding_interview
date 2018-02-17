def reverseSentence(sentence):
    words = sentence.split()
    results = []
    for word in words:
        results.append(word[::-1])
    results = ' '.join(results)
    print(results)

if __name__=="__main__":
    reverseSentence('Hello world')
