# Your code here
ignore_str = '":;,.-+=/\\|[]{}()*^&'

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

wc_dict = word_count(my_list)

# need longest key length for padding reasons
longest_key = max(len(x) for x in wc_dict)

# have to sort keys alphabetically which is done with key =, and values by descending which is done with sorted()
# read more here: 
# https://stackoverflow.com/questions/9919342/sorting-a-dictionary-by-value-then-key
# 
sorted_tuple = sorted(wc_dict.items(), key = lambda wc_dict: (-wc_dict[1],wc_dict[0]), reverse=False)

for k, v in sorted_tuple:
	print("{0: <17} ".format(k), v * "#")
