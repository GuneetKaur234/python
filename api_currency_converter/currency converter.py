import currencyapicom

client_name = currencyapicom.Client('cur_live_HhCaEDLXKaJ5BzoJpNtiXgcFj2y302gbtkptCW7r')
result_name = client_name.currencies()

dict_currency_name = result_name['data']

amount = float(input("Enter the amount in Rupees = "))
print("You want to convert Rupee to? available option are = ")

list_currency = []
for x in dict_currency_name:
    list_currency.append(f"{x} : {dict_currency_name[x]['name']}")

list_symbol = []
for x in dict_currency_name:
    list_symbol.append(f"{x} : {dict_currency_name[x]['symbol_native']}")

for x in range(1,len(list_currency)+1):
    print(f"{x}: {list_currency[x-1]}")

client_value = currencyapicom.Client('cur_live_HhCaEDLXKaJ5BzoJpNtiXgcFj2y302gbtkptCW7r')
result_value = client_value.latest()

currency = int(input("Enter valid serial number = "))

data_list = list_currency[currency-1]
data_string = str(data_list).split(" :")

dict_currency_value = result_value['data'][data_string[0]]['value']

converted_amount = amount * float(dict_currency_value) / 82.79
formated = "{:.2f}".format(converted_amount)

print(f"Total amount after conversion is {list_symbol[currency-1][-1]}{formated}")
