class Ticket:
   counter = 1
   open_tickets = 0
   closed_tickets = 0
   def __init__(self, staff_id, creator_name, contact_email, description):
       self.ticket_number = Ticket.counter + 2000
       Ticket.counter += 1
       self.staff_id = staff_id
       self.creator_name = creator_name
       self.contact_email = contact_email
       self.description = description
       self.response = "Not Yet Provided"
       self.status = "Open Ticket"
       Ticket.open_tickets += 1
   def submit_ticket(self):
       pass
   def respond_to_ticket(self, response):
       self.response = response
       if "Password Change" in self.description:
           new_password = self.staff_id[:2] + self.creator_name[:3]
           self.response += " New Password: " + new_password
           self.close_ticket()
       elif response != "Not Yet Provided":
           self.close_ticket()
   def resolve_password_change(self):
       new_password = self.staff_id[:2] + self.creator_name[:3]
       self.response = "Password Changed. New Password: " + new_password
       self.close_ticket()
   def close_ticket(self):
       self.status = "Closed Ticket"
       Ticket.open_tickets -= 1
       Ticket.closed_tickets += 1
   def reopen_ticket(self):
       self.status = "Reopened"
       Ticket.open_tickets += 1
       Ticket.closed_tickets -= 1
   @classmethod
   def ticket_stats(cls):
       return f"Tickets Created: {cls.counter - 1}, Tickets Resolved: {cls.closed_tickets}, Tickets To Solve: {cls.open_tickets}"
   def display_ticket(self):
       print(f"Ticket Number: {self.ticket_number}")
       print(f"Ticket Creator: {self.creator_name}")
       print(f"Staff ID: {self.staff_id}")
       print(f"Email Address: {self.contact_email}")
       print(f"Description: {self.description}")
       print(f"Response: {self.response}")
       print(f"Ticket Status: {self.status}\n")
class TicketManager:
   tickets = []
   @classmethod
   def submit_ticket(cls, ticket):
       cls.tickets.append(ticket)
   @classmethod
   def display_all_tickets(cls):
       for ticket in cls.tickets:
           ticket.display_ticket()
# Main method
if __name__ == "__main__":
   # Creating tickets
   ticket1 = Ticket("42069", "Leighton Sutcliffe", "LeightonSutcliffe@gmail.com", "Password Change request")
   ticket2 = Ticket("42420", "Alan Bigdog", "Alan Bigdog@gmail.com", "Printer not working")
   ticket3 = Ticket("69696", "Kelly McNabb", "KellyMcNabb@gmail.com", "Software installation issue")
   ticket4 = Ticket("72400", "Rob Dog", "RobDog@gmail.com", "Network connectivity problem")
   # Adding tickets to TicketManager
   TicketManager.submit_ticket(ticket1)
   TicketManager.submit_ticket(ticket2)
   TicketManager.submit_ticket(ticket3)
   TicketManager.submit_ticket(ticket4)
   # Displaying ticket statistics
   print("Displaying Ticket Statistics")
   print(Ticket.ticket_stats())
   # Responding to tickets
   ticket1.respond_to_ticket("Resolved")
   ticket2.respond_to_ticket("Working on it")
   # Displaying all tickets
   print("\nPrinting Tickets:")
   TicketManager.display_all_tickets()
   # Displaying updated ticket statistics
   print("\nDisplaying Ticket Statistics")
   print(Ticket.ticket_stats())
   # Reopening tickets
   ticket1.reopen_ticket()
   # Displaying updated ticket information and statistics
   print("\nPrinting Tickets:")
   TicketManager.display_all_tickets()
   print("\nDisplaying Ticket Statistics")
   print(Ticket.ticket_stats())