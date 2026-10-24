from pydantic import BaseModel, EmailStr, AnyUrl, Field, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name:str
    age:int            
    email:EmailStr
    weight: float  #kg
    height: float  #mtr       
    married:bool
    allergies: List[str]
    contact_details:Dict[str,str]        

    @computed_field()
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi


def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.bmi)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("inside insert_patient_data")

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.bmi)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("inside update_patient_data")


patient_info = {"name":"Pranav", "age":26, "email":"pranav@gmail.com","linkedin_url":"http://linkedin.com","weight":79.5,"height":1.75,"married":False, "allergies":["Dust","Pollen"], "contact_details":{"email":"pranav@example.com","phone":"9359647575"}}

patient1 = Patient(**patient_info)  #unpacking the dictionary to create an object of Patient class

insert_patient_data(patient1)       #passing the object to the function
update_patient_data(patient1)       #passing the object to the function
