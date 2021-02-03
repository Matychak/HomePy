exit = False
while not exit:
    choice = int(input("1. attraction\n0. exit\n :>>>"))
    if choice == 1:
        from lib.attraction import Attraction
        att = Attraction()
        att.attraction()

    elif choice == 0:
        exit = True
        print("Bye")
    else:
        print("Error enter correct num")

# 2 task

# exit = False
# while not exit:
#     choice = int(input("\n1.Bank\n2.Exit\n===>>>:"))
#     if choice == 1:
#         input_system = int(input("\nEnter password : "))
#         if input_system == 1111:
#             print("\nOkey password is correct")
#             from lib.attraction import Bank
#             bnc = Bank()
#             bnc.bank()
#         elif input_system != 1111:
#             print("Password wrong, please enter true password")
#     if choice == 2:
#         exit = True
#         print("Bye")
