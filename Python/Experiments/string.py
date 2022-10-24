print("Enter the lines: ")
lines = ''' 
         '''
while not lines.endswith("."):
    lines = str(input())
    
print("The length of the string is:", len(lines))
rep_word = input("Enter the word to be replaced: ")
new_word = input("Enter the new word: ")
lines = lines.replace(rep_word, new_word)
print("The new string is:", lines)
