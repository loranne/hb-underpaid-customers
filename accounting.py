def gets_payment_discrepancies(orderfile):
    """Takes in text file containing order data, returns list of customers who
    underpaid, along with how much they paid, and how much they should have paid"""

    # open the relevant file, save as a variable
    order_data = open(orderfile)

    # read the file line by line
    for line in order_data:
         # split on | character
        order = line.rstrip().split("|")
        
        # unpack to assign variables to each item in list
        customer_num, customer_name, melons_purchased, amount_paid = order
        # probably a neater way to do this, but need amount paid to be a float
        amount_paid = float(amount_paid)
        melons_purchased = float(melons_purchased)

        # split off first name
        customer_first_name = customer_name.split()[0]
        # print(customer_first_name)

        # calculates how much customer owed 
        amount_owed = melons_purchased * 1.00

        # if cust payment not equal to cust owed, print details
        if amount_owed != float(amount_paid):
            print(f"{customer_first_name} paid ${amount_paid:.2f}", f"expected ${amount_owed:.2f}")
    
    # returns order
    #return order
    pass

    order_data.close()

gets_payment_discrepancies("customer-orders.txt")