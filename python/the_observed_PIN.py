import codewars_test as test
from itertools import product
""" ┌───┬───┬───┐
    │ 1 │ 2 │ 3 │
    ├───┼───┼───┤
    │ 4 │ 5 │ 6 │
    ├───┼───┼───┤
    │ 7 │ 8 │ 9 │
    └───┼───┼───┘
        │ 0 │
        └───┘
He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could 
actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. 
instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 
6 or 8.

He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, 
they never finally lock the system or sound the alarm. That's why we can try out all possible (*) 
variations.

* possible in sense of: the observed PIN itself and all variations considering the adjacent digits

Can you help us to find all those variations? It would be nice to have a function, that returns 
an array (or a list in Java/Kotlin and C#) of all variations for an observed PIN with a length 
of 1 to 8 digits. We could name the function getPINs (get_pins in python, GetPINs in C#). 
But please note that all PINs, the observed one and also the results, must be strings, because of 
potentially leading '0's. We already prepared some test cases for you."""


def get_pins(observed):
    horizontal_table = (('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'))
    vertical_table = (('1', '4', '7'), ('2', '5', '8', '0'), ('3', '6', '9'))
    pin_number_associate = {}

    for index_pin_symbol, one_pin_symbol in enumerate(tuple(observed)):
        pin_number_associate_key = f'{index_pin_symbol + 1} symbol => {one_pin_symbol}'
        pin_number_associate[pin_number_associate_key] = [one_pin_symbol]
        for type_table in (horizontal_table, vertical_table):
            for type_line in type_table:
                if one_pin_symbol in type_line:
                    pin_number_index = type_line.index(one_pin_symbol)
                    try:
                        if pin_number_index == 0:
                            pin_number_associate[pin_number_associate_key].append(
                                type_line[pin_number_index + 1])
                        elif pin_number_index == (len(type_line) - 1):
                            pin_number_associate[pin_number_associate_key].append(
                                type_line[pin_number_index - 1])
                        else:
                            pin_number_associate[pin_number_associate_key].append(
                                type_line[pin_number_index + 1])
                            pin_number_associate[pin_number_associate_key].append(
                                type_line[pin_number_index - 1])
                    except IndexError:
                        continue
                    break    

    result = []
    for list_single_values in product(*pin_number_associate.values()):
        result.append(''.join(list_single_values))
    
    return result


@test.describe("example tests")
def sample_tests():
    @test.it("Tests")
    def it_1():
        expectations = [('8', ['5','7','8','9','0']),
         ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]), 
         ('369', ["339","366","399","658","636","258","268","669","668","266","369","398","256",
         "296","259","368","638","396","238","356","659","639","666","359","336","299","338","696",
         "269","358","656","698","699","298","236","239"])]

        for tup in expectations:
            test.assert_equals(sorted(get_pins(tup[0])), sorted(tup[1]), 'PIN: ' + tup[0])

