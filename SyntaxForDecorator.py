import functools

user = {"username": "jose", "access_level": "admin"}

#1
'''
def make_secure(func):
    def secure_function(): #decorator
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}"
    
    return secure_function
'''

#2
def make_secure(func):
    @functools.wraps(func)
    def secure_function(): #decorator
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}"
    
    return secure_function


@make_secure #Instead assigning directly, "at" sytnax can be used. 
def get_admin_password():
    return "1234"

print(get_admin_password.__name__) #but the name of this function is actually secure_function, so modify the code as #2

#get_admin_password = make_secure(get_admin_password)

print(get_admin_password())