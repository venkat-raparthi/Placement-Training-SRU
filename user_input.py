from Authentication import Authentication

class user_input():
    def password(self):
        while self.attempts>0:
                user_input=input("Enter the password:")

                if user_input==self.password:
                    print("welcome!")
                    break
                else:
                    self.attempts-=1
                    if self.attempts>0:
                        print(f"wrong password! you have {self.attempts} attempts left.")
                    else:
                        print("Account Blocked.")
                        break