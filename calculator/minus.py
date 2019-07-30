# Sum Module

def minus(a, b, verbose=0):
    '''
    Writing this Sample doc. This is useful as when you type __doc(minus)__, this text is printed.
    hence its a good practice to use this.
    Here, 
        - parameters are to be explained.
        - return values are to be explained.
        - finally, dependencies are to explained
    '''
    try:
        return a-b
    except:
        if verbose==1:
            print("""Possible Unsupported operation, please check the variable-type.""")
        return a-b