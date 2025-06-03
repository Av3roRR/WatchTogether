from app.users.schemas import SRegistration
from app.exceptions import (IncorrectPasswordException, IncorrectNameException,
                            LongNicknameException, IncorrectSurnameException,
                            IncorrectAgeException)

def check_registration_info(schema: SRegistration):
    pw = schema.password
    if len(pw) < 6 or len(pw) > 32:
        raise IncorrectPasswordException
    
    if len(schema.nickname) > 20:
        raise LongNicknameException
    
    if schema.name is not None and not schema.name.isalpha():
        raise IncorrectNameException
    
    if schema.surname is not None and not schema.surname.isalpha():
        raise IncorrectSurnameException
    
    age = schema.age
    if age is not None and (not isinstance(age, int) 
                                 or (isinstance(age, int) and (age < 12 or age > 120))):
        raise IncorrectAgeException