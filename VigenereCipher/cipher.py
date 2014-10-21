#### Name: Grace Hadiyanto
#### E-mail: ifoundparis@gmail.com
#### CPSC 223P
#### Assignment 2

# A list of the alphabet letters in lowercase
alphabet = [chr(x) for x in range(97, 123)]

# A set containing common special characters; used for formatting output
special_characters = { "'", '“', '”', ',', '.', '!', '\n', '\t', '?', '"', ':' }

# A dictionary that maps each alphabet to its index in the alphabet
alpha_to_num = dict([(alphabet[x], x) for x in range(0, 26)])

# A dictionary that maps each number to its letter in the alphabet
num_to_alpha = dict([(x, alphabet[x]) for x in range(0, 26)])

# Returns a list of the indices of the letter by their places in the alphabet
def alphaIndex(keyword):
    l = []
    for c in keyword:
        l.append(alpha_to_num.get(c.casefold()))
    return l

# Adds the index of the code letter to a list after its shift by the key value
def encodeLetter(l, i, key, counter):
    i = (i + key[counter]) % 26
    l.append(i)

# Adds the index of the original letter to a list after it is shifted back by
# the key value
def decodeLetter(l, i, key, counter):
    i = (i - key[counter]) % 26
    l.append(i)

# Takes the list of unshifted values and key values to return a new list with
# shifted values
def encodeList(unshifted, key_values):
    l = []
    counter = 0
    for i in unshifted:
        if i is None:
            l.append(None)
            continue
        if counter + 1 <= len(key_values):
            encodeLetter(l, i, key_values, counter)
            counter += 1
        else:
            counter = 0
            encodeLetter(l, i, key_values, counter)
            counter += 1
    return l

# Takes the list of shifted values and key values to return a new list with
# its original values
def decodeList(shifted, key_values):
    l = []
    counter = 0
    for i in shifted:
        if i is None:
            l.append(None)
            continue
        if counter + 1 <= len(key_values):
            decodeLetter(l, i, key_values, counter)
            counter += 1
        else:
            counter = 0
            decodeLetter(l, i, key_values, counter)
            counter += 1
    return l

# Takes in a list of ciphered/unciphered text and its coded one returning a
# list of the coded characters with matching cases
def transcribe(origin, code):
    l = []
    for i, v in enumerate(code):
        if v is None:
            l.append(None)
            continue
        else:
            if origin[i].isupper():
                l.append((num_to_alpha.get(v).upper()))
            else:
                l.append(num_to_alpha.get(v))
    return l

# Takes the relevant elements in list l and adds them all onto one string
def listToString(l):
    s = ''
    for i in l:
        if i is None:
            s += ' '
        else:
            s += str(i)
    return s

# Looks for special characters in the original string to put in the new string
def formatString(original_string, new_string):
    for i, v in enumerate(original_string):
        if v in special_characters:
            new_string = new_string[:i] + v + new_string[i + 1:]
    return new_string

# Takes in a file name and depending on the action, will create a new file name
# for the output
def outFileName(file_name, action):
    dot_index = file_name.find('.')
    if action == 'cipher':
        newfile_name = file_name[:dot_index] + '-cipher.txt'
    if action == 'decipher':
        newfile_name = file_name[:dot_index] + '-clear.txt'
    return newfile_name
