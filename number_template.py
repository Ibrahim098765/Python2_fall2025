# operator overloading for numbers

class Number():
    """ Number class to demonstrate operator oberloading """
    def __init__(self, value):
        """ initializer """
        self.value = value


    def __add__(self, other):
        """ add tow objects"""
        if isinstance(other,Number):
            return Number(self.value + other.value)
        raise TypeError('Incompatiable objects')
    def __gt__(self, other):
        """ compare tow objects to see whether one has a greater vlaue"""
        if isinstance(other, Number):
            return (self.value > other.value)
        
    def __eq__(self, other):
        """ compare whether tow objects has the same vlaue" """
        if isinstance(other, Number):
            return self.value == other.value
        
    def __str__(self):
        """ dissplay number objects"""
        return f'Value = {self.value}'
# teset class
if __name__ == '__main__':
    try:
        pass
        # create number objects
        num1 = Number(10)
        num2 = Number(20)

       

        # add two number objects
        num3 = num1 + num2

        # display results
        print(f'{num1.value} + {num2.value} + {num3.value}')
        

        # compare two number objects and display results
        # test for equality (=)
        print(f'{num1} == {num2}: {num1 == num2}')

        
        # test for greater than  (>)
        print(f'{num1} is greater than {num2}: {num1 > num2}')

        # test for number object with non-number object
        print(num1 + 100)
       

    except TypeError as te:
        print(te)
    except Exception as ex:
        print(ex)
