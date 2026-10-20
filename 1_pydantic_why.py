from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Annotated

class Patient(BaseModel):
    name:Annotated[str, Field(max_length=50,title="Name of the patient",description="Give the name of the patient in less that 50 chars",examples=["Pranav","Gauri"])]
    age:int = Field(gt=0,lt=120)                
        #Age must be greater than 0 and less tha 120
    email:EmailStr
    linkedin_url:AnyUrl
    weight: Annotated[float, Field(gt=0,strict=True)]                  
        #weight must be greater that 0
    married:Annotated[bool,Field(default=None,description="Patient is married or not")]
        #married is optional now
    allergies: Annotated[List[str], Field(default=None,max_length=5)] 
        #list not write becouse we need list of strings not only list, and maximum only 5 allergies
    contact_details:Dict[str,str]               #same for Dict need dict of str type


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


patient_info = {"name":"Pranav", "age":26, "email":"pranav@gmail.com","linkedin_url":"http://linkedin.com","weight":79.5,"married":False, "allergies":["Dust","Pollen"], "contact_details":{"email":"pranav@example.com","phone":"9359647575"}}

patient1 = Patient(**patient_info)  #unpacking the dictionary to create an object of Patient class

insert_patient_data(patient1)       #passing the object to the function
update_patient_data(patient1)       #passing the object to the function
