from app.utils.auth import JWTAuthenticator

def get_jwt_authenticator():
    return JWTAuthenticator(secret_key="serverless")  # move to config
