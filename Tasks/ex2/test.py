def f(x):
    return x**2 / (x**2 + 1)
    
def filter_numbers(l):
    return sorted([x for x in l if type(x)==float or type(x)==int ])
    
def shorten(l,length):
    return [x[:length] for x in l]

def overlapping(list1,list2):
    return len([x for x in list1 if x in list2])

def number_of_letters(word):
    dict = {}
    for x in word:
        if x not in dict:
            dict[x] = 1
        else:
            dict[x] = dict[x]+1
    return dict

def minmax(f,begin,end):
   return (min([f(x) for x in range(begin,end+1)]),max([f(x) for x in range(begin,end+1)]))
    


print(filter_numbers([1.2, "sdas", 4, [12], 3.4, "12", -3, True, 5, 8.1]))
print(shorten(["plzen", "liberec", "ostrava", "praha", "brno"], 3))
print(overlapping([1,2,3], [4,5,6,7]))
print(overlapping([1,2,3,4], [3,4,5]))
print(number_of_letters("ababdacabbdabc"))
print(minmax(f, -5, 5))

