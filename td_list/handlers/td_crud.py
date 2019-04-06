from td_list.dbapi import TicketActivityDbio
from td_list.models import TicketActivity


class TicketAct:
    def create_issue(self, data):
        tkt_data = {
            'title': data.get('title'),
            'description': data.get('description'),
            'status': data.get('status'),
        }
        return TicketActivityDbio().create_obj(tkt_data)

    def get_all_tickets(self):
        objs = TicketActivity.objects.all().exclude(is_delete=True)
        if not objs:
            return {
                'message': 'No tickets are available'
            }
        return objs

    def modify(self, ticket_uuid, data):
        obj = TicketActivityDbio().get_object(
            {
                'uuid': ticket_uuid
            }
        )
        tkt_data = {
            'title': data.get('title', obj.title),
            'description': data.get('description', obj.description),
            'status': data.get('status', obj.status),
        }
        return TicketActivityDbio().update_obj(obj, tkt_data)

    def delete_ticket(self, ticket_uuid):
        obj = TicketActivityDbio().get_object(
            {
                'uuid': ticket_uuid
            }
        )
        TicketActivityDbio().update_obj(obj, {'is_delete': True})

    def retreive_single_ticket(self, ticket_uuid):
        return TicketActivityDbio().get_object(
            {
                'uuid': ticket_uuid
            }
        )

    def get_all_todo(self, tkt_id=None):
        if tkt_id:
            objs = TicketActivity.objects.filter(uuid=tkt_id)
        else:
            objs = TicketActivity.objects.all()
        to_do = []
        for obj in objs:
            data = {
                'tkt_uuid': obj.uuid,
                'title': obj.title,
                'description': obj.description,
                'status': obj.status,
                'is_delete': obj.is_delete,
                'created_at': obj.created_at,
                'modified_at': obj.modified_at
            }
            to_do.append(data)
        return to_do
