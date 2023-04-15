#! /usr/bin/python3

'''uitwerking huiswerkopdracht'''

def is_palindroom(input_string, resultaat):
    '''
    Naam: is_palindroom
    Doel: bepaalt of een input_string een palindroom is
    precondities: resultaat is bij eerste aanroep True
    postcondities: -
    Input: input_string input_string
                boolean  resultaat
    output: True if input_string is een palindroom, else False
    '''


    #grenswaarde
    if len(input_string) <= 1:
        resultaat = True
    else:
        if resultaat:
            #ga naar grenswaarde
            einde = input_string[0]
            laatste = input_string[len(input_string)- 1]
            if einde == laatste:
                #recursieve aanroep
                input_string = input_string[1:-1]
                resultaat = is_palindroom(input_string, resultaat)
            else:
                resultaat = False
    return resultaat


def is_palindroom2(input_string, resultaat, begin, einde):
    '''Alternatief:
    Input:
            input_string input_string
            int begin
            int einde
            boolean resultaat
    pre:
            bij eerste aanroep wijst begin naar eerste karakter van input_string
            bij eerste aanroep wijst einde naar laatste karakter van input_string
            resultaat is bij eerste aanroep True
    '''
    if resultaat and (begin >= einde or begin == einde):
        resultaat = True
    else:
        if resultaat:
            #N.B. wijkt af van de pseudocode: dit heet voortschrijdend inzicht
            #pseudocode is alleen een hulpmiddel, geen doel (behalve misschien op het tentamen)
            #het dient er voor om je op weg te helpen
            if input_string[begin] == input_string[einde]:
                begin = begin + 1
                einde = einde - 1
                resultaat = is_palindroom2(input_string, resultaat, begin, einde)
            else:
                resultaat = False
    return resultaat


TESTSTRING = ['lepel', 'konijn', 'anna', 'aap']
for test in TESTSTRING:
    print(is_palindroom(test, True))

for test in TESTSTRING:
    print(is_palindroom2(test, True, 0, len(test) - 1))
