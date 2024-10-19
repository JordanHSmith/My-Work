'''
Jordan Smith
11/11/21
CS 152B
This file creates a word association game
To run the file type "python3 wordmap.py" in the terminal
'''

def main():
    '''
    (None) -> (None)
    Prints out various words and user's responses to these prompts
    '''
    print("Say whatever word comes to mind when prompted.")
    words = ["cat ", "goat ", "thumb ","cheese ","happy ","computer ","loser ","bagels ","long ","kayak "]
    mapping = {}
    for item in words:
        response = input(item)
        mapping[item] = response
    for key in mapping.keys():
        print(key, mapping.get(key))

if __name__=='__main__':
    main()