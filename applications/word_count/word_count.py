from functools import reduce 
# import string

ignore_list = ['"', ':', ';', ',', '.','-','+','=','/', '\\', 
                '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
ignore_str = ''.join(ignore_list)
def word_count(words: str):
    # Your code here
    # print(words.lower().split())
    # return dict((word, words.count(word)) for word in words.lower().split())
    
    words = words.translate(str.maketrans('','',ignore_str))
    return (reduce( lambda d, c: d.update([(c, d.get(c,0)+1)]) or d, words.lower().split(), {}) )


if __name__ == "__main__":
    print(word_count('Hello, my cat.  And my cat doesn\'t say "hello" back.'))
    print(word_count("Hello hello hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count("Hello    hello"))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))