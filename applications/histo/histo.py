# Your code here

ignore_list = ['"', ':', ';', ',', '.','-','+','=','/', '\\', 
                '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
ignore_str = ''.join(ignore_list)

with open('robin.txt') as f:
	# set as a string 
	my_list = f.read().replace('\n', '')

def word_count(words: str) -> dict:
    no_punct_words = words.translate(
        str.maketrans('','',ignore_str)).lower().split()
    # print(no_punct_words)
    return dict((word, no_punct_words.count(word)) for word in no_punct_words)
    # return (reduce( lambda return_dict, 
    #     count: return_dict.update([(count, return_dict.get(count,0)+1)]) 
    #     or return_dict, no_punct_words, {}) )


x = word_count(my_list)
# read more here: 
# https://stackoverflow.com/questions/9919342/sorting-a-dictionary-by-value-then-key
# 
y = sorted(x.items(), key = lambda x: (-x[1],x[0]), reverse=True)
print(y)
