import functools 


user = {"username": "Jose", "access-level": "guest"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function(panel):
        if user["access-level"] == "admin":
            return func(panel)
        else:
            return f"No admin permissions for {user['username']}."
    
    return secure_function
 
@make_secure            # this does same job as get_admin_password = make_secure(get_admin_password)
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"


print(get_password("billing"))