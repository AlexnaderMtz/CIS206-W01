"""
CIS206 W01 3/12/2024
Alexander Martinez Leyva
Assignment 9
"""

import re

# Problem 1: Check for set of characters
def containsOnlySpecificCharacters(s):
    return bool(re.match(r'^[a-zA-Z0-9]+$', s))


# Problem 2: Match - followed by zero
def matchFollowedByZeroOrMoreBs(s):
    return bool(re.match(r'^ab*$', s))


# Problem 3: Match - followed by one
def matchFollowedByOneorMoreBs(s):
    return bool(re.match(r'^ab+$', s))


# Problem 4: Find sequences of lowercase - underscore
def findSequencesofLowercaseLettersJoinedbyUnderscore(s):
    return re.findall(r'\b[a-z]+_[a-z]+\b', s)


# Problem 5: Match a word at the beginning
def matchWordatBeginningofString(s):
    return bool(re.match(r'^\w+', s))


# Problem 6: Match a word containing z
def matchWordContainingZ(s):
    return bool(re.search(r'\b\w*z\w*\b', s))


# Problem 7: Remove leading zeros from IP address
def removeLeadingZerosFromipAddress(ip):
    return re.sub(r'\b0+(\d+)', r'\1', ip)


# Problem 8: Search for literal stringS
def searchForLiteralStrings(s, words):
    return [word for word in words if re.search(word, s)]


# Problem 9: Search for a literal string and its location
def searchforLiteralStringandLocation(s, word):
    match = re.search(word, s)
    if match:
        return match.start()
    return -1


# Problem 10: Replace whitespaces with underscore
def replaceWhitespaceWithUnderscoreandViceVersa(s):
    return re.sub(r'\s', '_', s), re.sub(r'_', ' ', s)


# Problem 11: Extract year, month, and date from a URL
def extractYearMonthDateFromUrl(url):
    return re.findall(r'/(\d{4})/(\d{2})/(\d{2})/', url)


# Problem 12: Find all words starting with a or e
"""SAME PROBLEM AS 14"""
def findWordsStartingWithaore(s):
    return re.findall(r'\b[a|e]\w*\b', s)


# Problem 13: Replace space, comma, or dot with a colon
def replaceSpaceCommadotWithColon(s):
    return re.sub(r'[ ,.]', ':', s)


# Problem 14: Find all words starting with a or e
"""SAME PROBLEM AS 12"""
def findWordsStartingWithaore2(s):
    return re.findall(r'\b[a|e]\w*\b', s)


# Problem 15: Remove multiple spaces from a string
def removeMultipleSpaces(s):
    return re.sub(r'\s+', ' ', s)


# Test the functions
def main():
    # Test strings
    testStrings = [
        "ABCDEFabcdef123450",
        "*&%@#!}{",
        "ab", "abc", "a", "ab", "abb",
        "aab_cbbbc", "aab_Abbbc", "Aaab_abbbc",
        "The quick brown fox jumps over the lazy dog.",
        " The quick brown fox jumps over the lazy dog.",
        "216.08.094.196",
        "The quick brown fox jumps over the lazy dog.",
        'The quick brown fox jumps over the lazy dog.',
        "Regular Expressions", "Code_Examples",
        "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/",
        "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly.",
        "Python Exercises, PHP exercises.",
        "Python      Exercises"
    ]

    # Call each function with test strings
    functions = [
        containsOnlySpecificCharacters,
        matchFollowedByZeroOrMoreBs,
        matchFollowedByOneorMoreBs,
        findSequencesofLowercaseLettersJoinedbyUnderscore,
        matchWordatBeginningofString,
        matchWordContainingZ,
        removeLeadingZerosFromipAddress,
        searchForLiteralStrings,
        searchforLiteralStringandLocation,
        replaceWhitespaceWithUnderscoreandViceVersa,
        extractYearMonthDateFromUrl,
        findWordsStartingWithaore,
        replaceSpaceCommadotWithColon,
        findWordsStartingWithaore2,
        removeMultipleSpaces
    ]

    for i, (testString, func) in enumerate(zip(testStrings, functions), start=1):
        if i == 8:  # for Problem 8
            result = func(testString, ['fox', 'dog', 'horse'])
        elif i == 9:  # for Problem 9
            result = func(testString, 'fox')
        else:
            result = func(testString)
        print(f"Problem {i} Result:", result)
        print()

if __name__ == "__main__":
    main()

