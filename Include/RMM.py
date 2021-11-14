word_list = '../wordlist.txt'
test_file2 = '../all_without_punctuation.txt'
test_file3 = '../text_out/text_out_RMM.txt'

def get_dic(test_file):
    with open(test_file,'r',encoding='utf-8',) as f:
        try:
            file_content = f.read().split()
        finally:
            f.close()
    chars = list(set(file_content))
    return chars

dic = get_dic(word_list)
def readfile(test_file2):
    max_length = 5

    h = open(test_file3,'w',encoding='utf-8',)
    with open(test_file2,'r',encoding='utf-8',) as f:
        lines = f.readlines()

    for line in lines:
        my_stack = []
        len_hang = len(line)
        while len_hang>0 :
            tryWord = line[-max_length:]
            while tryWord not in dic:
                if len(tryWord)==1:
                    break
                tryWord=tryWord[1:]
            my_stack.append(tryWord)
            line = line[0:len(line)-len(tryWord)]
            len_hang = len(line)

        while len(my_stack):
            t = my_stack.pop()
            if t == '\n' :
                h.write('\n')
            else:
                h.write(t + "  ")

    h.close()
if __name__ == "__main__":
    readfile(test_file2)