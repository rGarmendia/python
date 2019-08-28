def fahrenheit_converter(celsius):
    return celsius * 9/5 + 32

temperatures = [10, -20, 100]

for temperature in temperatures:
    print(fahrenheit_converter(temperature))