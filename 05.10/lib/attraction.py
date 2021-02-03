if __name__ == "__main__":
    Attraction

class Attraction:

    def attraction(self):
        exit = False
        self._balance = int(input("Enter grn "))
        self._moods = 0
        while not exit:
            choice = int(input("1. Батут\n2. Трамплін\n3. Басейн\n4. Настроения\n5. Баланс\n0. exit\n:>>> "))
            if choice == 1:
               if self._balance >= 100:
                  a = 100
                  self._balance = self._balance - a
                  self._moods = self._moods + 20
                  print("Батут")
                  print("Moods " + "+" + str(self._moods))
               elif self._balance <= 100:
                  print("Не достатньо грошей")
                  exit = True
                  print("Баланс " + str(self._balance) + " grn")
                  self._moods = self._moods - 20
                  print("Moods " + "-" + str(self._moods))
            elif choice == 2:
                if self._balance >= 50:
                   self._balance = self._balance - 50
                   self._moods = self._moods + 15
                   print("Трамплін")
                   print("Moods " + "+" + str(self._moods))
                elif self._balance <= 50:
                   print("Не достатньо грошей")
                   exit = True
                   print("Баланс " + str(self._balance) + " grn")
                   self._moods = self._moods - 15
                   print("Moods " + "-" + str(self._moods))
            elif choice == 3:
                if self._balance >= 200:
                   self._balance = self._balance - 200
                   self._moods = self._moods + 50
                   print("Басейн")
                   print("Moods " + "+" + str(self._moods))
                elif self._balance <= 200:
                   print("Не достатньо грошей")
                   exit = True
                   print("Баланс " + str(self._balance) + " grn")
                   self._moods = self._moods - 50
                   print("Moods " + "-" + str(self._moods))
            elif choice == 4:
                print("Настроения " + str(self._moods))
            elif choice == 5:
                print("Баланс " + str(self._balance) + " grn")
            elif choice == 0:
                exit = True
            else:
                print("Use --help for reading manual")

#2 task

# if __name__ == "__main__":
#     Bank

# class Bank:

#     def bank(self):
#         exit = False
#         self._balance = int(input("\nEnter your balance : "))
#         while not exit:
#             choice = int(input("\n1. Поточний баланс\n2. Зняти гроші\n0. exit\n:>>> "))
#             if choice == 1:
#                print("balance : " + str(self._balance) + " grn")
#             elif choice == 2:
#                 price = int(input("Сумма зняття : "))
#                 if price >= self._balance:
#                    print("Неможливо знятти бо сумма зняття > за баланс ")
#                 else:
#                     # self._balance - price
#                     self._balance = self._balance - price
#                     print("balance : " + str(self._balance) + " grn")