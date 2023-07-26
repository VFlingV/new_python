"""
В большой текстовой строке подсчитать количество встречаемых 
слов и вернуть 10 самых частых. Не учитывать знаки препинания и
 регистр символов. За основу возьмите любую статью из википедии или
   из документации 
к языку.(Может помочь метод translate из модуля string)
"""



import string

def count_words(text):
    text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = text.split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_words[:10]


text = "Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. \
An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks \
rather than curly brackets or keywords), and a syntax which \
allows programmers to express concepts in fewer lines of code than might be used in languages such as C++ or Java. The language provides constructs intended \
to enable writing clear programs on both a small and large scale."

most_common_words = count_words(text)
for word, count in most_common_words:
    print(word, count)

