from Salsa_sales import SalsaSales

# UI for salsa sales program
def main():
    """ maim function """
    flavors = ['mild','medium','hot','zesty']
    salsa_objects = []

    for flavor in flavors:
        salsa_object = SalsaSales()
        update_sales(flavor, salsa_object)
        salsa_objects.append(salsa_object)
    display_report(salsa_objects)

def update_sales(flavor, salsa_object):
    """ update the jars sold and unit price for each flavcor """
    qty = int(input('enter total jars sold for : ' + flavor + ' flavor:' ))
    # validate the qty, make sure it is not negative
    price = float(input('enter unit price for ' + flavor + ' flavor:'))
    # validate the price, make sure it is not negative
    # set salsa object values
    salsa_object.set_jars_sold(qty)
    salsa_object.set_flavor(flavor)
    salsa_object.set_unit_price(price)

def display_report(salsa_list):
    """ display all salsa objects """
    # displsy heading 
    print(f'{"Flavors":10}{"Jars Sold":10s}{"Unit Price":12s}{"Total Price":12s}')

    for salsa in salsa_list:
        print(salsa)

main()

