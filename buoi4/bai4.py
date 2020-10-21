from functools import reduce

def increase(x):
    return x + 1

def double(x):
    return x*2

def square(x):
    return x**2

def compose1(*func):
    func = func[::-1]
    def inner(x):
        return reduce(lambda x, function: function(x), func,x)
    return inner
func1 = compose1(increase, double, square)
print(func1(3))

def compose2(*func):
    def inner(x):
        if len(func) == 1:
            return inner(func[0](x))
        return inner(func[0](compose2(*func[:-1])(x)))
    return inner
func1 = compose2(increase, double,double, square)
print(func1(3))