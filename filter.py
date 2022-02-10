'''
Remove words with lenght other than 5
'''
from openpyxl import load_workbook

WORDS = 'polish.xlsx'
OUTPUT_FILE = 'filtered_words.txt'
DICTIONARY = 'word_list.txt'
WORD_LENGTH = 5

data = []
'''
# Load data from excel

workbook = load_workbook(filename=WORDS)
sheet = workbook.active

for idx, row in enumerate(sheet['A']):
    word = row.value
    try:
        if len(word) == WORD_LENGTH:
            data.append(word)
    except:
        print(word, type(word))

workbook.close()

with open(OUTPUT_FILE, mode='w', encoding='utf-8') as output:
    for word in data:
        output.write(str(word + '\n'))
'''

# Remove strange words

words = set()
filtered_and_correct = list()

with open(DICTIONARY, mode='r', encoding='utf-8') as dictionary:
    for w in dictionary.readlines():
        word = w.rstrip()
        if len(word) == WORD_LENGTH:
            words.add(word)
    
with open(OUTPUT_FILE, mode='r', encoding='utf-8') as filtered:
    for w in filtered.readlines():
        if w.rstrip() in words:
            filtered_and_correct.append(w.rstrip())

with open(OUTPUT_FILE, mode='w', encoding='utf-8') as filtered:
    for w in filtered_and_correct:
        filtered.write(str(w + '\n'))