import time

user = {"username": "jose", "access_level": "guest"}

def get_admin_password():
    return "1234"

'''    
def secure_function(func):
    if user["access_level"] == "admin":
        return func

get_admin_password = secure_function(get_admin_password) #because user isn't admin, so this function returns none (error)

print(get_admin_password())
'''

def make_secure(func):
    def secure_function(): #decorator
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}"
    
    return secure_function

get_admin_password = make_secure(get_admin_password) #because user isn't admin, so this function returns none (error)

user = {"username": "jose", "access_level": "admin"}
print(get_admin_password())

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs) #To accept any types of arguemnts
        end = time.time()

        print(f"Function: {func.__name__} executed time: {end - start: .4f} sec")
        return result
    return wrapper

def slow_function():
    time.sleep(2) # wait 2 sec
    print("End")

slow_function = timer(slow_function)
slow_function()