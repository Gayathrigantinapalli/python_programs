

# class breakfast:
#     def cooking():
#         print("i am making breakfast")
# class lunch(breakfast):
#     def cooking():
#         print("i am making lunch")
# class dinner(lunch):
#     def cooking():
#         print("i am making dinner")
# a=breakfast
# b=lunch
# c=dinner
# a.cooking()
# b.cooking()
# c.cooking()




# class payment:
#     def pay(self,amount):
#         pass
# class netbanking(payment):
#     def pay(self,amount):
#         print(f"i am doing the payment {amount}through netbanking")
# class creditcard(payment):
#     def pay(self,amount):
#         print(f"i am doing the payment {amount}through creditcard")
# class debitcard(payment):
#     def pay(self,amount):
#         print(f"i am doing the payment{amount} through debitcar")
# class upi(payment):
#     def pay(self,amount):
#         print(f"i am doing the payment {amount}through upi")

# def transection(x,amount):
#  x.pay(amount)
# y=transection(debitcard(),2000)
# z=transection(upi(),100)
# a=transection(creditcard(),30000)
# b=transection(netbanking(),10)







# a=2
# b=3
# c=a+b
# if a>b:
#     print("value")
# else:
#     print("sorry")
# print(c)


# def simple_interest(principal, rate, time):
#     interest = (principal * rate * time) / 100
#     return interest

# p = float(input("Enter the Principal amount: "))
# r = float(input("Enter the Rate of Interest: "))
# t = float(input("Enter the Time (in years): "))

# si = simple_interest(p, r, t)
# print("The Simple Interest is:", si)





# def compound_interest(principal, rate, time, n):
#     """
#     principal : initial amount
#     rate      : annual interest rate (in %)
#     time      : time in years
#     n         : number of times interest is compounded per year
#     """
#     # Convert rate from percentage to decimal
#     rate = rate / 100
    
#     # Compound Interest formula: A = P * (1 + r/n)^(n*t)
#     amount = principal * (1 + rate / n) ** (n * time)
    
#     # Interest earned
#     interest = amount - principal
    
#     return amount, interest


# # Example usage
# p = 10000   # Principal
# r = 5       # Annual interest rate in %
# t = 10      # Time in years
# n = 12      # Compounded monthly

# final_amount, earned_interest = compound_interest(p, r, t, n)

# print(f"Final Amount after {t} years: {final_amount:.2f}")
# print(f"Compound Interest earned: {earned_interest:.2f}")



class gpay:
    def pay(self):
        print("paying amount using gpay")
class phpay:
    def pay(self):
        print("paying amount using phpay")
class paytm:
    def pay(self):
        print("paying amount using paytm")
def billing(x):
    x.pay()
billing(phpay())
billing(gpay())
billing(paytm())
