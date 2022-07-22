ADMINS = ["FunkyMonkey#0890"]
def isAdmin(User):
    return User.name + "#" + User.discriminator in ADMINS
