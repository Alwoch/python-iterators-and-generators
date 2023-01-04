my_list=[1,2,3,4]
list_iterable=iter(my_list)

print(type(list_iterable)) #<class list_iterator>

my_string='sally'
string_iterable=iter(my_string)

print(type(string_iterable)) #<class str_iterator>

my_dict={"name":"sally","age":20}
dict_iterable=iter(my_dict)

print(type(dict_iterable)) #<class 'dict_keyiterator'>

#iterate over elements of my_list using next()
print(next(list_iterable)) 
print(next(list_iterable))
print(next(list_iterable))
print(next(list_iterable))
print(next(list_iterable))#generates only one item after the other and causes a stop iteration exception when the items are exhausted

class EvenNumbers:
    def __init__(self, max:int):
        self.max = max
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num >= self.max:
            raise StopIteration
        self.num += 2
        return self.num

my_even_numbers=EvenNumbers(5)
print(my_even_numbers.__iter__())
print(my_even_numbers.__next__())
print(my_even_numbers.__next__())
print(my_even_numbers.__next__())#raises a stopIteration
