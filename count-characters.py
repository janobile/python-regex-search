'''
Write a function that returns the count of distinct case-insensitive alphabetic
characters and numeric digits occurring more than once in an input string. Example:
a. "abcde" => {}
b. "aabbcde" => { ‘a’: 2, ‘b’: 2 }
c. "aabBcde" => { ‘a’: 2, ‘b’: 2 }
d. "indivisibility" => { ‘i’: 6 }
e. "Indivisibilities" => { ‘i’: 6, ‘s’: 2 }
f. "aA11" => { ‘a’: 2, 1: 2 }
g. "ABBA" => { ‘a’: 2, ‘b’: 2 }
'''

def run():
    string = input('Input the word: ').lower()

    dict_string = {char:string.count(char) for char in set(string) if string.count(char)>1 }

    print(dict_string)



if __name__ == "__main__":
    run()

