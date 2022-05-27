# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    
    file = open(filename, "r")
    file_content = file.read()
    file.close()
    
    return f"Below is the content of {filename}\n\n{file_content}\n"



def count_words():
    text = read_file_content("story.txt")
    text_list = text.split()
    unique_words = set(text_list)

    words_dict = {}
    
    
    for word in unique_words:
        word_count = 0
        for each_word in text_list:
            
            if word == each_word:
                word_count += 1
        
        words_dict[word] = word_count

    return words_dict


print(read_file_content("story.txt"))
print(count_words())
