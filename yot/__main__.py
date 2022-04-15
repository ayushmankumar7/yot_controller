import sys 
import requests 

words = ['word1', 'word2', 'word3']
def main():
    print("☠ You Own It Controller ☠")
    args = sys.argv[1:]
    print()
    if len(args) == 2:
        args1 = args[0]
        args2 = args[1]
        if args1 in words:
            r = requests.put(f'http://localhost:5000/api/{args1}', data = {'message': args2})
            print("♻ Refresh the Website to view your Results!")
        else:
            print("🟡 Please enter a Valid Word Identifier\nAvaiable words identifiers are: [word1, word2, word3]")
        
    else:
        print("🛑Please enter Args. \n Usage: yot [identifier] [message]")