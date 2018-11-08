leftHandChars = set(['q','w','e','r','t','a','s','d','f','g','z','x','c','v','b'])
rightHandChars = set(['y','u','i','o','p','h','j','k','l','n','m'])

def other(group):
    if group == leftHandChars:
        return rightHandChars
    return leftHandChars

def alternates(word):
    currentGroup = None
    if word[0] in leftHandChars:
        currentGroup = leftHandChars
    else:
        currentGroup = rightHandChars
    for c in word:
        if c not in currentGroup:
            return False
        currentGroup = other(currentGroup)
    return True

with open('words.txt','r') as f:
    for word in f:
        word = word.rstrip()
        if len(word) == 4 or len(word) == 3:
            if alternates(word):
                print word
