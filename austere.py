num_words = input()
word = input()

n = int(num_words.split()[0])
k = int(num_words.split()[1])

freq_map = {}
count = 0


for char in word:
    if char in freq_map.keys():
        freq_map[char] = freq_map[char] + 1
    else:
        freq_map[char] = 1

    # desc = {k : v for k, v in sorted(freq_map.values())}
    # sorted(freq_map.items)
    desc = dict(sorted(freq_map.items(), key=lambda item: item[1], reverse=True))
    


    
    # for i in range(n):
        # stencils.append(list(desc.keys())[i])
    # print(stencils)


letters = list(desc.keys())

if ' ' in letters:
    letters.remove(' ')
# print(letters)

stencils = letters[0:k]
# print(stencils)

result = []

for char in word:
    # if space
        # print space
    if char == ' ':
        # print(char)
        result.append(char)
    elif char in stencils:
        # print(char)
        result.append(char)
    else:
        # print(stencils[0])
        result.append(stencils[0])


x = ''.join(result)
# x = str(result)
print(x)

    # else if char in stencils
        # print char
    # else - if not in stencils
        # print a letter from stencils


# for char in word:
#     if char in freq_map.keys():
#         freq_map.values += 1
#     else:
#         freq_map.put(char, 1)
    # word[char] = word.get(char, 0) + 1
# print(desc)