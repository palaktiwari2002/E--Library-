from sass import balance
def library( book_list):
    r = book_list.keys()
    u = list(r)
    print("Books Available At The Stores :",u)
    print("20% off on each book")
    user = input("Select Book :")
    payment_method = input("do you want to pay by card ? ")
    for y in book_list:
        if y == user and payment_method == "yes":
            m = book_list[y]-book_list[y]*20/100
            print("mrp:",book_list[y]) 
            print("discounted price", book_list[y]*20/100)
            print("pay amount :",m)
            print(f'''amount debited from your a/c: {m}
                      balance Avalable : {balance - m}''')
   
                              
            
library( {
    "afcat": 460,
    "navy": 540,
    "army": 500,
    "banking":700
})

    
