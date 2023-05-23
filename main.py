from JobsGeParser import jobs_ge_pars
from JobsGeDatabase import JobDatabse
from jobs import Jobs

database = JobDatabse("job_data")
print("What do you want to do?")
print('1.Get information from website ')
print('2.See jobs and salaries ')
print('3.Create a vacancy ')
print('4.press 4 to quit')
user = int(input('Choose by inserting corresponding number '))
print()

while user != 4:

    if user == 1:
        user = int(input("how many? "))
        jobs_ge_pars(user)
        print('information has successfuly added to the database')
        print()
    elif user == 2:
        al = database.jobs_salaries()
        for i in al:
            if i[1] is None:
                print(f'{i[0]} -- No information')
            else:
                print(f'{i[0]} -- {i[1]}')
        print()
    elif user == 3:
        name = input('name - ')  # def __init__(self, name, desc, company, p_date, d_date, salary, email):
        description = input('descriiption - ')
        company = input("company - ")
        publish_d = input('publish date - ')
        deadline = input('deadline date - ')
        salary = input('salary - ')
        email = input('email - ')
        new_job = Jobs(name, description, company, publish_d, deadline, salary, email)
        database.add_job(new_job)
    elif user == 4:
        break

    print()
    print("What do you want to do?")
    print('1.Get information from website ')
    print('2.See jobs and salaries ')
    print('3.Create a vacancy ')
    print('4.press 4 to quit')
    user = int(input('Choose by inserting corresponding number '))
    print()
