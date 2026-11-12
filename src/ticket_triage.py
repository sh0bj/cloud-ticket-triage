# Shoaib Mohammed 
# recieve ticket input from user
# categorize it into a category based on buzzwords, use .lower to account for caps
# if unable to categorize -> send it to general issues

def categorize_ticket(ticket):
    ticket_lowercase = ticket.lower() # initializing variable that converts ticket input into lowercase

    if "password" in ticket_lowercase or "account" in ticket_lowercase: # if statement checking for keywords to categorize the ticket  
        category = "Accessing Account"
    elif "mouse" in ticket_lowercase or "keyboard" in ticket_lowercase:
        category = "Hardware Issues"
    elif "update" in ticket_lowercase or "loading" in ticket_lowercase:
        category = "Application Issues"
    elif "internet" in ticket_lowercase or "wifi" in ticket_lowercase:
        category = "Network Issues"
    else:
        category = "General Issues"
    return category

sample_tickets= ["Unable to login to my account, forgot my password.",
                 "My keyboard/mouse stopped working this morning.",
                 "A specific application isn't loading or requires an update.",
                 "I am having trouble with my internet connection.",
                 "The Wifi speed is slower than usual.",
                 "I have been locked out of my account.",
                 "My keyboard stopped working after the latest computer update."]


print("Cloud Ticket Triage\n")

for ticket in sample_tickets:
    print(ticket)
    category = categorize_ticket(ticket)
    print("Ticket Category:", category)
    print()





