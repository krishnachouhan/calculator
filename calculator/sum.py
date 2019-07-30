# Sum Module

def sum(a, b, verbose=0):
    '''
    Writing this Sample doc. This is useful as when you type __doc(sum)__, this text is printed.
    hence its a good practice to use this.
    Here, 
        - parameters are to be explained.
        - return values are to be explained.
        - finally, dependencies are to explained
    '''
    try:
        return a+b
    except:
        if verbose==1:
            print("a+b Couldn't be done simply, Trying other alternaives.")
        temp=None
        try:
            if verbose==2:
                print("""Second level of Verbose here we are explaining the simply preformed operations.
                a+b Couldn't be done simply, Trying other alternaives, as this mmight be a list.""")
            if type(a[0])==type(''):
                temp=''
            if type(a[0])==type(0):
                temp=0
            for i in a:
                if type(i)==type(0):
                    temp = temp + i
                elif type(i)==type(''):
                    temp = str(temp)+i
        except:
            if verbose==1:
                print("""Possible Unsupported operation, please check the variable-type.""")
            return a+b