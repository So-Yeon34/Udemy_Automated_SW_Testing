import functools

user = {"username": "jose", "access_level": "admin"}
user = {"username": "jose", "access_level": "guest"}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function():
            if user["access_level"] == "admin":
                return func()
            else:
                return f"No {access_level} permissions for {user['username']}"
        
        return secure_function
    
    return decorator

@make_secure("admin")
def get_admin_password():
    return "1234"

@make_secure("guest")
def get_dashboard_password():
    return "user: user_password"

print(get_admin_password())
print(get_dashboard_password())