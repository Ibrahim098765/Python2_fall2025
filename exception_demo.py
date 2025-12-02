# test different errors in python
def main():
    """ main fundtion"""
    error_list = [
        test_zero_division,
        test_type_error,
        test_index_error,
        test_name_error,
        test_value_error
    ]
    i = 0
    while i < len(error_list):
        test_function = error_list[i]
        try:
            test_function()
        except Exception as ex:
            print(f'Capture an error:{type(ex).__name__}')
            print(f'The error details: {ex}')
        # if there is no error, run th code inside else
        else:
            print('No error occurred')
        # with error or without error, this block of code will run
        finally:
            print('-'* 30)
        i +=1
        




def test_zero_division():
    """ capture zerodivision error"""
    print('----- Tessting ZeroDivisionError ------')
    result = 20 / 0 
def test_type_error():
    """ capyure type error"""
    print('-------- Testing TypeError ----')
    ' greetings' + 5
def test_index_error():
    """ capture the index error"""
    print('-----Testing IndexError ------')
    lst = [1,2,3]
    lst[5]
def test_name_error():
    """ capture the name error"""
    print('-------Testing NameError -----')
    print(undefined_variable)
def test_value_error():
    """ capture the value error"""
    print('-----Test ValueError-----')
    int('not a number')

main()