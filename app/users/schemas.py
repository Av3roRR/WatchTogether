from pydantic import BaseModel, EmailStr, SecretStr, Field

class SRegistration(BaseModel):
    nickname: str 
    email: EmailStr = Field(examples=["new@gmail.com"])
    password: SecretStr = Field(
        json_schema_extra={
            "title": "Password",
            "description": "Password of the user",
            "examples": ["123456"]
        }
    )
    title: str | None
    name: str | None
    surname: str | None
    age: int | None