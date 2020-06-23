def convert(number):

    # initialize flags such that we start with no factors
    factor3 = False
    factor5 = False
    factor7 = False

    # initialize the output as type string
    string_output = ''

    # evaluate the moduli for each division, checking for zeroes
    if (number%3 == 0):
        factor3 = True
    if (number%5 == 0):
        factor5 = True
    if (number%7 == 0):
        factor7 = True

    if factor3 or factor5 or factor7 is True:
        if factor3 is True:
            string_output = string_output + 'Pling'

        if factor5 is True:
            string_output = string_output + 'Plang'

        if factor7 is True:
            string_output = string_output + 'Plong'
    else:
        string_output = string_output + str(number)

    return(string_output)
