from datetime import date

class Talaba:
    # classs nomi
    def __init__(self,firts_name,last_name,birth_day,):
        self.first_name = firts_name
        self.last_name = last_name
        self.birth_Day = birth_day

    def tanishtir(self):
        print(f"{self.last_name} {self.first_name} {self.birth_Day} - yilda tug'ilgan ")

    def get_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_full_name(self):
        return f"(self.last_name) (self.first_name)"

    def set_age(self):
        # date.today().year hozirgi vohtdagi yilni oladi
        return date.today().year - self.birth_Day

talaba = Talaba("gayrat","Sohibov",2002)

print(talaba.set_age())

class User:

    def __init__(self, username,email,password):
        self.username = username
        self.xato_email = email
        self.password = password


    def tekshiruv(self):
        if '@' in self.xato_email:
            print("email_to'gri kiritildi")
            self.email = self.xato_email
        else :
            print("xato email ")

userr = User("javohir","javohirikromov", "javohir31")


userr.tekshiruv()
userr.xato_email = "javohirikromov003@gmail.com"
print (userr.xato_email)
userr.tekshiruv()