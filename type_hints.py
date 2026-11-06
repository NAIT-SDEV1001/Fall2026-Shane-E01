#Type hints describe what a function expects for parameters and what it returns
#They are documentation, and NOT enforced
#str, int, float, bool,list[str|int|float],dict[str,str]


#name parameter is expecting a string and the function is expected to return a string
def greeting(name: str)-> str:
    return f'Hello {name}!'

def shout(name: str)->None:
    print(f'Hello {name}!')

def shoutShane(name: str)->str | None :
    if name == 'Shane':
        return f'Hello {name}!'
    else:
        return None


print(greeting('Shane'))