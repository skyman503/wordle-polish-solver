'''
Remove words with lenght other than 5
'''

INPUT_FILE = 'word_list.txt'
OUTPUT_FILE = 'filtered_words.txt'

with open(INPUT_FILE, mode='r', encoding='utf-8') as input:
    data = [x.rstrip() for x in input.readlines() if len(x.rstrip()) == 5]
    
    with open(OUTPUT_FILE, mode='w', encoding='utf-8') as output:
        for word in data:
            output.write(str(word + '\n'))
