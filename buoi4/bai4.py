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

idx = 0
def compose2(*func):
    func = func[::-1]
    def inner(x):
        global idx
        if idx == len(func):
            return x
        else:
            x = func[idx](x)
            idx += 1
            return inner(x)
    return inner
func1 = compose2(increase, double,double, square)
print(func1(3))