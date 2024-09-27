from faker import Faker
import random
from .models import *
fake= Faker()

def seed_db(n=10)-> None:
    try:
            for i in range(0 , n):
                [1, 2, 3, 4]
                department_objs= department.objects.all()
                random_index= random.randint(0, len(department_objs)-1)
                student_id=(f" STU-0{random.randint(100, 999)}")
                department=department_objs[random_index]
                student_name= fake.name()
                student_age= random.randint(20 , 30)
                student_contact= f" +91{random.randint(10000000000,999999999999)}"
                student_email= fake.email()
                student_address= fake.address()

                student_id_objs=StudentID.objects.create(student_id=student_id)
                
                student_objs= Student.objects.create(
                    department=department,
                    student_id=student_id_objs,
                    student_name=student_name, 
                    student_age =student_age,
                    student_contact=student_contact,
                    student_email=student_email,
                    student_address= student_address,)
    except Exception as e:
            print(e)