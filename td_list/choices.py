from base.choices import Choices


class TicketStatus(Choices):
    STATUS_NOT_SET = 0
    INPROGRESS = 1
    COMPLETED = 2
    PENDING = 3
