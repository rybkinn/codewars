import codewars_test as test
"""Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
Leave punctuation marks untouched."""


def pig_it(text):
    # words = text.split()
    # for index, word in enumerate(words):
    #     if word.isalpha():
    #         symbol = words[index][:1]
    #         words[index] = words[index][1:] + f'{symbol}ay'
    #     else:
    #         continue
    # return ' '.join(words)
    return ' '.join([f'{word[1:]}{word[:1]}ay' if word.isalpha() else word for word in text.split()])

test.assert_equals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
test.assert_equals(pig_it('This is my string'),'hisTay siay ymay tringsay')
test.assert_equals(pig_it('O tempora o mores !'),'Oay emporatay oay oresmay !')
