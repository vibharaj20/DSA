def encode(self, strs) -> str:
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res    

def decode(self, str):
    res, i = [], 0
    while i < len(str):
        # Find the position of '#'
        j = i
        while str[j] != '#':
            j += 1
        # Get the length of the next word
        length = int(str[i:j])
        # Extract the word of the given length
        word = str[j + 1 : j + 1 + length]
        res.append(word)
        # Move i to the next segment in the string
        i = j + 1 + length
    return res
