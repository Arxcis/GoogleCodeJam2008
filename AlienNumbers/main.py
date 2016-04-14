#!/usr/bin/env python
# -*- coding: utf-8

""" Tittel   : Alien numerical language converter.
                  En oppgave gitt på Google CodeJam 2008.
    Author   : Jonas
    Opprettet: 14.04.2016
     Session : 15:00 - 17:10
     Session : 21:40 -                       
     ---------------------------------------------------"""

import math

def convert_to_decimal(number, source):
    """ For this problem, I have chosen decimal as an intermediate
         language. 
        """
    base_source = len(source) 
    counter = 0
    decimal_sum = 0

    for digit in number[-1::-1]:

        decimal_sum += source.index(digit) * (base_source ** counter)
    
        counter += 1
        """ 
        source.index(digit) finds the value of given digit based on
                             the value of the index in the language-spec.

                        Example: in Hex, 'A' has the value 10, and it also is 
                                  placed at index 10 in a list from smallest 
                                   to highest. 

        base_source**counter -> Base of source_language: 
                         Decides the positional value. 
                          in Hex the rightmost digit has positional value
                           16 ** 0 and then 
                           16 ** 1, and then 
                           16 ** 2 etc.                           """

    return decimal_sum


def convert_to_target(decimal, target_language):
    base_target = int(len(target_language))
    pool = decimal

    exponent = 50
    slot_counter = 0
    new_number = ''

    while exponent >= 0:
       
        if pool - (base_target**exponent) >= 0:
            factor = math.floor((pool) / (base_target**exponent))
            pool -= factor*(base_target**exponent)

            new_number += target_language[int(factor)]
        elif pool != decimal:
            new_number += target_language[0]
        else: 
            pass
        exponent -= 1

    return new_number

def alien_number_translator(source_number, source_language, target_language):
    # Source-number is converted to decimal.
    decimal = convert_to_decimal(source_number, source_language)
    #Decimal is convert to target-number
    new_number = convert_to_target(decimal, target_language)
    # Target-number is returned
    return new_number


def main():
    with open('large-input.txt', 'r') as f:
        f2 = open('large-decimal.txt', 'a')

        count_max = int(f.readline())
        counter = 1
        while counter < (count_max + 1):

            line = (f.readline()).replace("\n", "")
            listline = line.split(" ")

            source_number, source_language, target_language = listline
            target_number = alien_number_translator(source_number, source_language, 
                                                ['0','1','2','3','4','5','6','7','8','9'])

            f2.write("Case #%s: %s" % (counter, target_number) + "\n")

            print(line)
            print(target_number)
            counter += 1

        f2.close()


if __name__ == "__main__":
    main()
    #print(alien_number_translator('alll', ['l','a','r','s'], ['0','1','2','3','4','5','6','7','8','9']))





# HEx: tall2*(16^1), tall1*(16^0)
# Foo: tall2*(3^1),  tall1*(3^0)
# Bin: tall2*(2^1),  tall1*(2^0)

# Lars: tall3*(4^2), tall2*(4^1), tall1*(4^0)
#          a            l            l 
#          1            0            0 
#          16           0            0 

#                       s            s
#                       12           3


"""
language_specs = {
    'Decimal'   : ['0','1','2','3','4','5','6','7','8','9'],

    'Hex'       : ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'],
    'Foo'       : ['o', 'F', '8'],
    'Binary'    : ['0', '1'],
    'CodeJamsk' : ['O','!','C','D','E','?'],
    'CodeJamsk2': ['A','?','J','M','!','.'],

    'Romersk'   : ['I', 'II', 'III', 'IV'] # FML
} """