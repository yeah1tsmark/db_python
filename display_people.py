from main import People

my_people = People.select()
for ps in my_people:
    print(ps.person_name, ps.person_number, ps.person_email, ps.person_country, ps.person_gender, ps.person_religion,
          ps.person_password)
