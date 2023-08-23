#Private Variable in Closure:

#Using a closure to create a "private" #variable within a function
def secret_keeper(secret):
    def get_secret():
        return secret 
    return get_secret 
reveal =secret_keeper("Hidden message")
print(reveal())
