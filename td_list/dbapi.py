from base.dbapi import AbstractBaseDbIO
from td_list.models import TicketActivity


class TicketActivityDbio(AbstractBaseDbIO):

    @property
    def model(self):
        return TicketActivity
