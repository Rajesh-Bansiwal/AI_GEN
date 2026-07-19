from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name: str='rakul'
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10,default=5,description='A decimal value representing the cgpa of the student.')

new_student = {
    "name": "rajesh",
    'email':"raj@gmail.com",
'cgpa':5
}
# using field default values ,contrains,decriptiuon,regex
student = Student(**new_student)
# '32' denge y number hai toh pydentic isko type conversion kr dega
print(dict(student))
print(student.model_dump_json())
# print(student.name)