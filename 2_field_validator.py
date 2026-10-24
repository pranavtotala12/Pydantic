from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name:str
    age:int            
    email:EmailStr
    weight: float             
    married:bool
    allergies: List[str]
    contact_details:Dict[str,str]        

    @field_validator("email")
    @classmethod
    def email(cls, value):
        vaild_domains = ["hdfc.com","icici.com"] 

        domain_name = value.split("@")[-1]             # pranav@gmail.com -> gmail.com

        if domain_name not in vaild_domains:           #checking email is the part of vaild_domains
            raise ValueError("Not a vaild domain")
        
        return value

    @field_validator("name")
    @classmethod
    def name(cls, value):
        return value.upper()



def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("inside insert_patient_data")

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("inside update_patient_data")


patient_info = {"name":"Pranav", "age":26, "email":"pranav@hdfc.com","linkedin_url":"http://linkedin.com","weight":79.5,"married":False, "allergies":["Dust","Pollen"], "contact_details":{"email":"pranav@example.com","phone":"9359647575"}}

patient1 = Patient(**patient_info)  #unpacking the dictionary to create an object of Patient class

insert_patient_data(patient1)       #passing the object to the function
update_patient_data(patient1)       #passing the object to the function
