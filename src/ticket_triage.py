# Shoaib Mohammed 
# recieve ticket input from user
# categorize it into a category based on buzzwords, use .lower to account for caps
# if unable to categorize -> send it to general issues

def categorize_ticket(ticket):
    ticket_lowercase = ticket.lower() # initializing variable that converts ticket input into lowercase
    
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
    return category

print("Cloud Ticket Triage\n")

print("What issue are you having today?")
ticket = input()



print("Ticket Received: ")
print(ticket, "\n")


category = categorize_ticket(ticket)
print("Ticket Category:", category)




# Categories: 

# General
# Accessing Account
# Hardware Issues
# Application Issues
# Network Issues

