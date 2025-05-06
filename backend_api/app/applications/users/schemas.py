from pydantic import BaseModel, EmailStr, Field, ValidationInfo, model_validator


class BaseFields(BaseModel):
    email: EmailStr = Field(description="User email", examples=["timov31@ukr.net"])
    name: str = Field(description="User name", examples=["Richie"])


class PasswordField(BaseModel):
    password: str = Field(min_length=8)

    @model_validator(mode="before")
    def validate_passwords(cls, values: dict, info: ValidationInfo):
        password = (values.get("password") or "").strip()
        if not password:
            raise ValueError("Password is required")

        if len(password) < 8:
            raise ValueError("Too short password!")

        if " " in password:
            raise ValueError("No spaces in password!")

        return values


class RegisterUserFields(BaseFields, PasswordField):
    pass
