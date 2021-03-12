def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    result = {}
    my_phrase = phrase.lower()
    for letter in my_phrase:
        if letter in 'aeiou' and letter in result:
            result[letter]+=1
        elif letter in 'aeiou':
            result[letter] = 1
    return result


