from passlib.context import CryptContext


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Hashing():
    @classmethod
    def Hash(cls, string:str):
        return pwd_context.hash(string)


    @classmethod
    def Verify(cls, plainString:str, hashedString:str):
        print(plainString, hashedString)
        return pwd_context.verify(plainString, hashedString)


