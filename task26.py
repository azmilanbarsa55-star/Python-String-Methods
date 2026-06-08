user = input("git hub username: ")
result = user.replace('-', ' ').isalpha()
print(result)