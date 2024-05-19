# TUAZON, FRANCESCA MARIE A. (BCS24)

'''
Create a program that reads a text file and counts the frequency of each word in the file.
'''

file = open('poem.txt', 'r')

# initialize dictionary to store word counts
word_counts = {}

for line in file:
    words = line.split()        # split each line into words
    for word in words:
        temp = word.lower()     # convert to lowercase to remove case sensitivity; temp is current word being viewed

        temp = ''.join(char for char in temp if char.isalnum()) # remove punctuation

        # increment word count in the dictionary
        if temp in word_counts:
            word_counts[temp] += 1
        else:
            word_counts[temp] = 1

# close the file
file.close()

print("Word Frequencies: ")
print("--------------------------------------")
for word, count in word_counts.items():
    print(f"{word}: {count}")

        

