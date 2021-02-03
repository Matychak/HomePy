import requests

if __name__ == "__main__":
    Covid

class Covid:

    def covid(self):
        URL = "https://api.covid19api.com/summary"
        covid = requests.get(URL)
        covid = covid.json();
        exit = False
        while not exit:
            choice = int(input("\n1.Show COVID19 information\n2.Sort by new confirmed\n3.Show info for Country\n0.exit\n==>>: "))
            if choice == 1:
                for i in covid["Global"]:
                    print("\n" + i + " " + str(covid["Global"]["NewConfirmed"]))
            elif choice == 3:
                searchcountry = str(input("Enter country: "))
                expectations = 0
                def get_contry_index(country):
                    for index,item in enumerate(covid["Countries"]):
                        if item["Country"] == country:
                            return index

                countryid = get_contry_index(searchcountry)


                for i in covid["Countries"]:
                    if searchcountry == i["Country"]:
                        expectations = True


                if expectations == True:
                    newconfirmed = covid["Countries"][countryid]["NewConfirmed"]
                    totalconfirmed = covid["Countries"][countryid]["TotalConfirmed"]
                    newdeaths = covid["Countries"][countryid]["NewDeaths"]
                    totaldeaths = covid["Countries"][countryid]["TotalDeaths"]
                    newrecovered = covid["Countries"][countryid]["NewRecovered"]
                    totalrecovered = covid["Countries"][countryid]["TotalRecovered"]
                    date = covid["Countries"][countryid]["Date"]

                    covid_msg = f'New confimed cases in {searchcountry}: {newconfirmed}.\nThe total cases are: {totalconfirmed}.\nNew Deaths: {newdeaths}.\nTotal Deaths:{totaldeaths}.\nNew recovered: {newrecovered}.\nTotal Recoved: {totalrecovered}.\nDate: {date}'
                    print(covid_msg)
                else:
                    print("Please enter correct country")
                if choice == 0:
                    exit = True

            elif choice == 2:
                # covid_countries = covid["Countries"]
                # print(covid_countries)
                # sort_countries = sorted(covid_countries, key=lambda k: k['NewConfirmed'])
                # sort_countries.reverse()
                # print(sort_countries.reverse())
                # print(sort_countries.reverse())
                
                lol = covid["Countries"]
                # # sort = i["NewConfirmed"]
                lole = sort_countries = sorted(lol, key=lambda k: k["Slug"])
                # sort_countries.reverse()
                print(lole)
                # print(lol)
