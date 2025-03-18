class SupportTicket:
    def __init__(self, ticket_id, customer_name, issue):
        self.ticket_id = ticket_id
        self.customer_name = customer_name
        self.issue = issue
        self.status = "Açık"  # "Çözüldü" durumu da olabilir

    def close_ticket(self):
        self.status = "Çözüldü"

    def __str__(self):
        return f"#{self.ticket_id} - {self.customer_name}: {self.issue} [{self.status}]"

class CustomerSupportModule:
    def __init__(self):
        self.tickets = []

    def create_ticket(self, ticket_id, customer_name, issue):
        self.tickets.append(SupportTicket(ticket_id, customer_name, issue))

    def list_tickets(self):
        for ticket in self.tickets:
            print(ticket)

    def resolve_ticket(self, ticket_id):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                ticket.close_ticket()
                print(f"Ticket #{ticket_id} çözüldü.")
                return
        print("Ticket bulunamadı.")

