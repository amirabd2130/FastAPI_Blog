from fastapi import status, HTTPException


CREDENTIALS_EXCEPTION = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = 'Could not validate credentials',
        headers = {'WWW-Authenticate': 'Bearer'},)

USER_EXISTS_EXCEPTION = HTTPException(
        status_code = status.HTTP_409_CONFLICT,
        detail = 'The provided username already exists')

NOT_FOUND_EXCEPTION = HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = f'The record with provided id deos not exist or has been deleted')