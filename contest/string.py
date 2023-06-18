def string(dict ,query):
    result =[]
    freq_dict = {}
    for word in dict:
        sorted_word = ''.join(sorted(word))
        freq_dict[sorted_word] = freq_dict.get(sorted_word, 0 ) +1
    for q in query:
        sorted_q = ''.join(sorted(q))
        count = freq_dict.get(sorted_q,0)
        result.append(count)
    return result


dictionary = ["listen", "silent", "enlist", "inlets", "listen"]
query = ["silent", "inlets", "foo"]

result = string(dictionary, query)
print(result)
