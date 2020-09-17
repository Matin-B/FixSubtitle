from sys import argv


def fix_word(word):
    word = word.replace('ي', 'ی')
    word = word.replace('ك', 'ک')
    return word


file_name = argv[1]
file_content = open(file_name, 'r', encoding='cp1256').readlines()
final_text = ''
for line in file_content:
    final_text += fix_word(line)
export_file = open(argv[1], 'w')
export_file.writelines(final_text)
