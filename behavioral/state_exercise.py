from abc import ABC, abstractmethod


class TicketState(ABC):

    @abstractmethod
    def assign(self, ticket):
        pass

    @abstractmethod
    def resolve(self, ticket):
        pass

    @abstractmethod
    def close(self, ticket):
        pass


class NewState(TicketState):
    def assign(self, ticket):
        ticket.state = AssignedState()

    def resolve(self, ticket):
        pass

    def close(self, ticket):
        ticket.state = ClosedState()


class AssignedState(TicketState):
    def assign(self, ticket):
        pass

    def resolve(self, ticket):
        ticket.state = ResolvedState()

    def close(self, ticket):
        ticket.state = ClosedState()


class ResolvedState(TicketState):
    def assign(self, ticket):
        pass

    def resolve(self, ticket):
        pass

    def close(self, ticket):
        ticket.state = ClosedState()


class ClosedState(TicketState):
    def assign(self, ticket):
        pass

    def resolve(self, ticket):
        pass

    def close(self, ticket):
        pass


class Ticket:
    def __init__(self):
        self.state = NewState()

    def assign(self):
        self.state.assign(self)

    def resolve(self):
        self.state.resolve(self)

    def close(self):
        self.state.close(self)


# Step 4: Test the behavior of the ticket and its state transitions
def main():
    ticket = Ticket()

    # Test the initial state and transitions
    ticket.assign()
    ticket.resolve()
    ticket.close()

    # Test invalid transitions
    ticket.assign()
    ticket.resolve()


if __name__ == "__main__":
    main()
