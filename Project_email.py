email = input("Enter your email address: ")
at = email.find("@")
username = email[0:at]
left = email[at+1:len(email)]
dot = left.find(".")
domain = left[0:dot]
print("The username is: " + username)
print("The domain is: " + domain)
