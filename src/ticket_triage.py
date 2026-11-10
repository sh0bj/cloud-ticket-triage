# Shoaib Mohammed 
# recieve ticket input from user
# categorize it into a category based on buzzwords, use tolower to account for caps
# if unable to categorize -> print error message



print("Cloud Ticket Triage\n")

print("What issue are you having today?")
ticket = input()
ticket_lowercase = ticket.lower() # initializing variable that converts ticket input into lowercase


print("Ticket Received: ")
print(ticket, "\n")



if "password" in ticket_lowercase: # if statement checking for keywords to categorize the ticket  
    category = "Accessing Account"
elif "mouse" in ticket_lowercase or "keyboard" in ticket_lowercase:
    category = "Hardware Issues"
elif "update" in ticket_lowercase:
    category = "Application Issues"
elif "internet" in ticket_lowercase:
    category = "Network Issues"
else:
    category = "General Issues"

print("Ticket Category:", category)




# Categories: 

# General
# Accessing Account
# Hardware Issues
# Application Issues
# Network Issues

