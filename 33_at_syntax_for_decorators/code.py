import functools 


user = {"username": "Jose", "access-level": "guest"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access-level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."
    
    return secure_function
 
@make_secure            # this does same job as get_admin_password = make_secure(get_admin_password)
def get_admin_password():
    return "1234"


print(get_admin_password())