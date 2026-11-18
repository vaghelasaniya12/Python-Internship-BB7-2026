def build_invoice(customer_name, *args, **kwargs):
    print("Customer Name:", customer_name)
    total = sum(args)
    print("Total Amount:", total)
    print("Additional Details")
    for key, value in kwargs.items():
        print(key + ":", value)
        
build_invoice("Sanii", 500, 200, 300, discount=50, tax=20 )