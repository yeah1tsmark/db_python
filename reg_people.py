from main import People

try:
    p_name = input("Enter your name \n")
    p_phone_no = input("Enter your Phone no \n")
    p_email = input("Enter your email \n")
    p_country = input("Enter your country \n")
    p_gender = input("Enter your gender \n")
    p_religion= input("Enter your religion \n")
    p_password = input("Enter your password \n")

    People.create(person_name=p_name, person_number=p_phone_no, person_email=p_email, person_country=p_country,
                  person_gender=p_gender, person_religion=p_religion, person_password=p_password)
    print("Person Registered Successfully")
except:
    print("Failed to register Person use a different email")
    