def two_fer(name='you'):
    # what I just did is I defined a function with argument that unless specified defaults to the string 'you'
    if type(name) is not str:
            raise Exception('Name is not a string!')
            # what I just did is prepare for the possibility that a non-string parameter is passed on to the function in which case we end up at an exception
    string_to_return = ('One for %s, one for me.') % name
    print(string_to_return)
    return(string_to_return)
