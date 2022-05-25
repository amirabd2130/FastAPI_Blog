from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hashing():
    def Hash(string:str):
        return pwd_context.hash(string)
        
    def Verify(plainString:str, hashedString:str):
        return pwd_context.verify(plainString, hashedString)


