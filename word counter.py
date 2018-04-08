"""
CREATED BY UMAR SOHAIL
MORE UPDATE COMING ON, HOLD ON TO YOUR SEATS :)4
"""


user_sentence = str(input("Plaese enter your sentense or paragraph: ")).lower()
user_word = str(input("please enter the word that you want to count: ")).lower()


sentence_split = user_sentence.split(' ')


def space_remover(li):
    while '' in li:
        li.remove('')
    return li

cleaned_sent = space_remover(sentence_split)

def word_counter(word, lis):
    total = 0
    for i in lis:
        if word == i:
            total += 1
        else:
            pass
    return total

print (word_counter(user_word, cleaned_sent))
