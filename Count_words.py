# 1. Define the function and have it take a string argument.
def sentence_analyzer(sentence):

#2. Iterate through the string and count the occurrences of each character.
    solution = {}
    for char in sentence: 
        if char != " ": #loại bỏ khoẳng trắng
            if char in solution:
                solution[char]+= 1
            else:
                solution[char] = 1
    return solution
#3. Output each character as a key in the output dictionary, with the frequency as the
# value.
print(sentence_analyzer("Pythonn"))
print(sentence_analyzer("Nguyen Cong Duy"))
print(sentence_analyzer("Count number of occurrence of words in a given text"))