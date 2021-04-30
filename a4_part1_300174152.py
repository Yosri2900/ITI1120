# Full name: Yosri Ketata
# Student number: 300174152
# Course: ITI 1120
# Assignment Number: 4
##############################################################################

def is_valid_file_name():
    '''()->str or None'''
    file_name = None
    try:
        file_name = input("Enter the name of the file: ").strip()
        f = open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name = None
    return file_name


def get_file_name():
    file_name = None
    while file_name == None:
        file_name = is_valid_file_name()
    return file_name


def clean_word(word):
    """(str)->str
    Returns a new string which is lowercase version of the given word
    with special characters and digits removed

    The returned word should not have any of the following characters:
    ! . ? : , ' " - _ \ ( ) [ ] { } % 0 1 2 3 4 5 6 7 8 9 tab character and new-line character

    clean_word("co-operate.")
    'cooperate'
    clean_word("Anti-viral drug remdesivir has little to no effect on Covid patients' chances of survival, a study from the World Health Organization (WHO) has found.")
    'antiviral drug remdesivir has little to no effect on covid patients chances of survival a study from the world health organization who has found'
    clean_word("1982")
    ''
    clean_word("born_y1982_m08\n")
    'bornym'

    """
    # YOUR CODE GOES HERE
    only_letters = ""
    for char in word:
        if char.isalpha() or char == " ":
            only_letters += char.lower()

    return (only_letters)


def test_letters(w1, w2):
    """(str,str)->bool
    Given two strings w1 and w2 representing two words,
    the function returns True if w1 and w2 have exactlly the same letters,
    and False otherwise

    >>> test_letters("listen", "enlist")
    True
    >>> test_letters("eekn", "knee")
    True
    >>> test_letters("teen", "need")
    False
    """

    # YOUR CODE GOES HERE
    w1 = list(w1)
    w2 = list(w2)
    w1.sort()
    w2.sort()
    return w1 == w2


def create_clean_sorted_nodupicates_list(s):
    '''(str)->list of str
    Given a string s representing a text, the function returns the list of words with the following properties:
    - each word in the list is cleaned-up (no special characters nor numbers)
    - there are no duplicated words in the list, and
    - the list is sorted lexicographicaly (you can use python's .sort() list method or sorted() function.)

    This function must call clean_word function.

    You may find it helpful to first call s.split() to get a list version of s split on white space.
    
    create_clean_sorted_nodupicates_list(',''able "acre bale beyond" binary boat brainy care cat cater crate lawn\nlist race react cat sheet silt slit trace boat cat crate.\n')
    ['able', 'acre', 'bale', 'beyond', 'binary', 'boat', 'brainy', 'care', 'cat', 'cater', 'crate', 'lawn', 'list', 'race', 'react', 'sheet', 'silt', 'slit', 'trace']

    create_clean_sorted_nodupiates_list('Across Europe, infection rates are rising, with Russia reporting a record 14,321 daily cases on Wednesday and a further 239 deaths.')
    ['', 'a', 'across', 'and', 'are', 'cases', 'daily', 'deaths', 'europe', 'further', 'infection', 'on', 'rates', 'record', 'reporting', 'rising', 'russia', 'wednesday', 'with']
    '''

    # YOUR CODE GOES HERE
    words = s.split()
    no_duplicates_list = []
    for w in words:
        w = clean_word(w)
        if w not in no_duplicates_list:
            no_duplicates_list.append(w)
    no_duplicates_list.sort()
    return list(no_duplicates_list)


def word_anagrams(word, wordbook):
    '''(str, list of str) -> list of str
    - a string (representing a word)
    - wordbook is a list of words (with no words duplicated)

    This function should call test_letters function.

    The function returs a (lexicographicaly sorted) list of anagrams of the given word in wordbook
    >>> word_anagrams("listen", wordbook)
    ['enlist', 'silent', 'tinsel']
    >>> word_anagrams("race", wordbook)
    ['acre', 'care']
    >>> word_anagrams("care", wordbook)
    ['acre', 'race']
    >>> word_anagrams("year", wordbook)
    []
    >>> word_anagrams("ear", wordbook)
    ['are', 'era']
    '''

    # YOUR CODE GOES HERE
    list_of_anagrams = []
    for w in wordbook:
        is_anagram = test_letters(w, word)
        if (is_anagram == True) and not (w == word):
            list_of_anagrams.append(w)
    list_of_anagrams.sort()
    return (list_of_anagrams)


def count_anagrams(l, wordbook):
    '''(list of str, list of str) -> list of int

    - l is a list of words (with no words duplicated)
    - wordbook is another list of words (with no words duplicated)

    The function returns a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.
    
    Whenever a word in l is the same as a word in wordbook, that is not counted.

    >>> count_anagrams(["listen","care", "item", "year", "race", "ear"], wordbook)
    [3, 2, 3, 0, 2, 2]

    The above means that "listen" has 3 anagrams in wordbook, that "care" has 2 anagrams in wordbook ...
    Note that wordbook has "care", "race" and "acre" which are all anagrams of each other.
    When we count anagrams of "care" we count "race" and "acre" but not "care" itself.
    '''

    # YOUR CODE GOES HERE
    out = []
    for w in l:
        anagrams = word_anagrams(w, wordbook)
        count = len(anagrams)
        out.append(count)
    return out


def k_anagram(l, anagcount, k):
    '''(list of str, list of int, int) -> list of str

    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a  (lexicographicaly sorted) list of all the words
    in l that have exactlly k anagrams (in wordbook as recorded in anagcount)

    k_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2], 2)
    ['care', 'ear', 'race']
    '''

    # YOUR CODE GOES HERE
    i = 0
    final = []
    while i < len(anagcount):

        if k == anagcount[i]:
            final.append(l[i])

        i += 1

    final.sort()

    ufinal = []
    for word in final:
        if word not in ufinal:
            ufinal.append(word)

    return ufinal


def max_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with maximum number of anagrams (in wordbook as recorded in anagcount)
    
    >>> max_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2])
    ['item', 'listen']
    '''

    # YOUR CODE GOES HERE

    return k_anagram(l, anagcount, max(anagcount))


def zero_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with no anagrams
    (in wordbook as recorded in anagcount)
    
    >>> zero_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2])
    ['year']
    '''

    # YOUR CODE GOES HERE
    return k_anagram(l, anagcount, 0)


##############################
# main
##############################
wordbook = open("english_wordbook.txt").read().lower().split()
list(set(wordbook)).sort()

print("Would you like to:")
print("1. Analize anagrams in a text -- given in a file")
print("2. Get small help for Scrabble game")
print("Enter any character other than 1 or 2 to exit: ")
choice = input()

if choice == '1':
    file_name = get_file_name()
    rawtx = open(file_name).read()
    l = create_clean_sorted_nodupicates_list(rawtx)

    anagcount = count_anagrams(l, wordbook)

    maxa = max_anagram(l, anagcount)
    print("\nOf all the words in your file, the following words have the most anagrams:\n", maxa)
    print("\nHere are their anagrams: ")

    for w in maxa:
        print("Anagrams of", w, "are:", (word_anagrams(w, wordbook)))
    print("\nHere are the words from your file that have no anagrams: \n", zero_anagram(l, anagcount))

    print("\nSay you are interested if there is a word in your file that has exactly k anagrams")
    k = int(input("Enter an integer for k: "))
    print("Here is a word (words) in your you file with exactly", k, "anagrams: ")
    print(k_anagram(l, anagcount, k))

    # when asking for k from the user you may assume that they will enter non-negative integer
elif choice == '2':
    a = input("Enter the letters that you have, one after another with no space: ")
    while a != a.strip() or a.find(' ') != -1:
        print("Error: you entered space(s)")
        a = input("Enter the letters that you have, one after another with no space: ")

    a = clean_word(a)
    print("Would you like help forming a word with")
    builtin_choice = input("1. all these letters\n2. all but one of these letters?\n")
    while not (builtin_choice == '1' or builtin_choice == '2'):
        print("You must chose 1 or 2. Please try again.")
        builtin_choice = input("\n1. all these letters\n2. all but one of these letters?\n")

    if builtin_choice == '1':
        c = word_anagrams(a, wordbook)
        if a in wordbook:
            c = c + a
        if c:
            print("Here are the words that are comprised of exactly these letters:")
            print(c)
        else:
            print("There is no word comprised of exactly these letters.")


    elif builtin_choice == '2':
        print("The letters you gave us are:", a, "\nLet's see what we can get if we ommit one of these letters.")
        i = 0
        while i < len(a):
            b = a[:i] + a[i + 1:]
            print("Without the letter in position", i + 1, "we have letters", b)
            if word_anagrams(b, wordbook):
                print("Here are the words that are comprised of letters:", b)
                print(word_anagrams(b, wordbook))
            else:
                print("There is no word comprised of letters:", b)
            i += 1
else:
    print("Good bye")
