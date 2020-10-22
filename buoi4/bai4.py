from functools import reduce

def increase(x):
    return x + 1

def double(x):
    return x*2

def square(x):
    return x**2

def compose1(*func):
    return lambda x: reduce(lambda x, function: function(x), func[::-1],x)

func1 = compose1(increase, double,increase, double)
print(func1(2))

def compose2(*func):
    def inner(x):
        if len(func) == 1:
            return func[0](x)
        return func[0](compose2(*func[1:])(x))
    return inner
func1 = compose2(increase, double,increase, double)
print(func1(2))

def compose3(*func):
    if len(func) == 1:
        return lambda x: func[0](x)
    return lambda x: func[0](compose3(*func[1:])(x))
func1 = compose3(increase, double,increase, double)
print(func1(2))