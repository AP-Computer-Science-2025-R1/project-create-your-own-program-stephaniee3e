def unit_converter():
    print ("Unit Converter")
    print("1. length(m to ft, ft to m)")
    print("2. weight (kg to lb, lb to kg)")
    print ("3. temperature (C to F, F to C)")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        sub_choice = input("Enter 'm to ft' or 'ft to m': ")
        if sub_choice == 'm to ft':
            meters = float(input("Enter length in meters: "))
            feet = meters * 3.28084
            print(f"{meters} meters is equal to {feet} feet.")
        elif sub_choice == 'ft to m':
            feet = float(input("Enter length in feet: "))
            meters = feet / 3.28084
            print(f"{feet} feet is equal to {meters} meters.")
        else:
            print("Invalid choice for length conversion.")
    elif choice == '2':
        sub_choice = input("Enter 'kg to lb' or 'lb to kg': ")
        if sub_choice == 'kg to lb':
            kg = float(input("Enter weight in kg: "))
            lb = kg * 2.20462
            print (f"{kg} kg is equal to {lb} lb.")
        elif sub_choice == 'lb to kg':
            lb = float(input("Enter weight in lb: "))
            kg = lb / 2.20462
            print(f"{lb} lb is equal to {kg} kg.")
        else:
            print("Invalid choice for weight conversion.")
    elif choice == '3':
        sub_choice = input("Enter 'C' to 'F' or 'F to 'C': ")
        if sub_choice == 'C to F':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit.")
        elif sub_choice == 'F to C':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius.")
        else:
            print("Invalid choice for temperature conversion.")
    
unit_converter()