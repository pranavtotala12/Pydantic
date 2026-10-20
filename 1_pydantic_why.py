from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):
    name:str
    age:int
    weight:float
    married:bool
    allergies:List[str]             #list not write becouse we need list of strings not only list
    contact_details:Dict[str,str]   #same for Dict need dict of str type




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

patient_info = {"name":"Pranav", "age":26, "weight":79.5, "married":False, "allergies":["Dust","Pollen"], "contact_details":{"email":"pranav@example.com","phone":"93596475**"}}

patient1 = Patient(**patient_info)  #unpacking the dictionary to create an object of Patient class

insert_patient_data(patient1)  #passing the object to the function
update_patient_data(patient1)  #passing the object to the function