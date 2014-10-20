def myRange(n):
    returnList = [0]
    counter = 0
    while n != counter:
        counter += 1
        returnList.append(counter)
    return returnList

print myRange(5)


print xrange(100)

word = "test"
print len(word)