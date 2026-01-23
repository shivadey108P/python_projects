from passlib.context import CryptContext

# Create bcrypt context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Plain text password
plain_password = "Hello1234"

# Hash the password
hashed_password = pwd_context.hash(plain_password)

print("Plain password:", plain_password)
print("Hashed password:", hashed_password)

# Verify password later
is_valid = pwd_context.verify(plain_password, hashed_password)
print("Password valid?", is_valid)
