from django.db import models

from base.fields import ChoicesField
from base.models import AbstractAuditModel
from td_list.choices import TicketStatus


class TicketActivity(AbstractAuditModel):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    status = ChoicesField(
                                default=TicketStatus.STATUS_NOT_SET,
                                choice_class=TicketStatus
                        )
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return '%s ' % (self.title)
