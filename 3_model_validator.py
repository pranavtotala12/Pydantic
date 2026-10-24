from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name:str
    age:int            
    email:EmailStr
    weight: float             
    married:bool
    allergies: List[str]
    contact_details:Dict[str,str]          

    @model_validator(mode= "after")
    def validate_emergency_contact(cls, model):
        if model.age >60 and "emergency" not in model.contact_details:
            raise ValueError("Patients older than 60 must have emergency contact")
        return model



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


patient_info = {"name":"Pranav", "age":61, "email":"pranav@gmail.com","linkedin_url":"http://linkedin.com","weight":79.5,"married":False, "allergies":["Dust","Pollen"], "contact_details":{"email":"pranav@example.com","phone":"9359647575","emergency":"88997766"}}

patient1 = Patient(**patient_info)  #unpacking the dictionary to create an object of Patient class

insert_patient_data(patient1)       #passing the object to the function
update_patient_data(patient1)       #passing the object to the function
