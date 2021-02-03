# num = [1,2,3,4,5,6,[4, False]]
# print(num)
# print("type =>", type(num))

# num[2] = "white"
# print(num)
# print("======")
# print(num[6][1])
# print(num[-1])
# print("******")

# for item in num:
#     print(item)

# print("Lenght", len(num))
# new_item = int(input("Enter number append ===>>>"))
# num.append(new_item)
# print(num)

# num.pop(6)
# print(num)
# print("------Incert------")
# ins = input("Enter value ")
# ins_index = int(input("Enter index ===>>>"))
# num.insert(ins_index, ins)
# print(num)
# num = num.reverse()

# num = [1,2,3,4,5,6,7,8,9,0]

# print("type =>", type(num))
# for item in num1
#     print(item)

#-------------------------Tuple--------------

# currency = (2,3,4,5,6,7,7)


# print("type =>", type(currency))
# print(currency)
# for item in currency:
#     print(item)

# print("By index =>>",currency[0])

# import requests

# URL = "https://api.covid19api.com/summary"
# covid = requests.get(URL)
# covid = covid.json();

# for item in covid["Countries"]:

#     print(item['NewConfirmed'])

# for item in covid["Global"]:
#     print(item["TotalConfirmed"])

# for item in covid["Global"]:

#     print(str(item['NewConfirmed']))

# for i in covid["Global"]:
#     print(i["TotalRecovered"])
# for i in covid["Global"]:
#     print(int(i['NewConfirmed']))


#v2.0

import requests

URL = "https://api.covid19api.com/summary"
covid = requests.get(URL)
covid = covid.json();

# for i in covid["Countries"]:
    # a = covid["Global"]
    # print(a["NewConfirmed"])
    # print("New " + str(a["NewConfirmed"]))
    # print(str(i) + str(covid["Countries"]["NewConfirmed"]))
    # print(int(i["NewConfirmed"]).sort())
    # i["NewConfirmed"].sorted()
    # print(i["NewConfirmed"].sorted())
    # sorted(str(i["NewConfirmed"]))
    # print(sorted(str(i["NewConfirmed"])))
    # sor = str(i["NewConfirmed"])
    # sorted(sor, reverse=True)
    # print(sorted(sor, reverse=True))

#

    # print(i["CountryCode"]["AF"])

#Tutorial



# print(newconfirmed)

#search country
# exit = False
# searchcountry = "Albania2"
# lol = 0

# def get_contry_index(country):
#     for index,item in enumerate(covid["Countries"]):
#         if item["Country"] == country:
#             return index

# countryid = get_contry_index(searchcountry)


# for i in covid["Countries"]:
#     if searchcountry == i["Country"]:
#         lol = True

# if lol == True:
#     newconfirmed = covid["Countries"][countryid]["NewConfirmed"]
#     totalconfirmed = covid["Countries"][countryid]["TotalConfirmed"]
#     newdeaths = covid["Countries"][countryid]["NewDeaths"]
#     totaldeaths = covid["Countries"][countryid]["TotalDeaths"]
#     newrecovered = covid["Countries"][countryid]["NewRecovered"]
#     totalrecovered = covid["Countries"][countryid]["TotalRecovered"]
#     date = covid["Countries"][countryid]["Date"]

#     covid_msg = f'New confimed cases in {searchcountry}: {newconfirmed}.\nThe total cases are: {totalconfirmed}.\nNew Deaths: {newdeaths}.\nTotal Deaths:{totaldeaths}.\nNew recovered: {newrecovered}.\nTotal Recoved: {totalrecovered}.\nDate: {date}'

#     print(covid_msg)
# else:
#     print("Please enter correct country")



exit = False
while not exit:
    choice = int(input("1.Covid info\n0.Exit\n==>>: "))
    if choice == 1:
        from lib.covid import Covid
        cov = Covid()
        cov.covid()
    if choice == 0:
        exit = True