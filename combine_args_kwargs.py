# *args must be before **kwargs

def order_summary(*items,**options):
    print("Items ordered: ")
    #Loop through the items (tuple)
    for item in items:
        print(f"- {item}")

    print("Options: ")
    #loop through the options(dictionary)
    for key, value in options.items():        
        print(f"{key}: {value}")

order_summary("burger", "pasta","fries","gravy",takeout = True, bag = False, utensils = False)


    