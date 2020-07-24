'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    
    # Set a base case for recursion to stop (if the word is down to 1 or 0 letters)
    if len(word) == 1 or len(word) == 0:
            return 0

    # Set the counting variable
    count = 0

    # Check if the word has 't' followed by 'h' in the first two positions
    if word[0] == 't' and word[1] == 'h':
        # If it does, increase the word count by 1
        count += 1

    # Recursively run through the input word and check the first two positions
    # If the first two positions don't have 't' followed by 'h',
    # Take the first letter off and check again
    return count + count_th(word[1:])
