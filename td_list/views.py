from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from td_list.constants import TD_LIST, TD_NOTKT, TD_POST, TD_VIEW
from td_list.handlers.td_crud import TicketAct


class TicketActivityView(APIView):

    def get(self, request):
        objs = TicketAct().get_all_tickets()
        if 'message' in objs:
            return render(request, TD_NOTKT)
        return render(request, TD_LIST, {'tkt_info': objs})


class TicketHtmlView(APIView):
    def get(self, request):
        return render(request, TD_POST)

    def post(self, request):
        data = request.data
        tkt_obj = TicketAct().create_issue(data)
        messages.success(request, 'The Ticket has been Created')
        return render(request, TD_POST, {'tkt_info': tkt_obj})


class ModifyTicketView(APIView):

    def get(self, request, ticket_uuid):
        obj = TicketAct().retreive_single_ticket(ticket_uuid)
        return render(request, TD_VIEW, {'info': obj})

    def post(self, request, ticket_uuid):
        data = request.data
        if data.get('_method') == 'PUT':
            return self.put(request, ticket_uuid)
        return self.delete(request, ticket_uuid)

    def put(self, request, ticket_uuid):
        data = request.data
        obj = TicketAct().modify(ticket_uuid, data)
        messages.success(request, 'The Ticket has been Updated')
        return render(request, TD_VIEW, {'info': obj})

    def delete(self, request, ticket_uuid):
        TicketAct().delete_ticket(ticket_uuid)
        arg_num = reverse('get_tickets')
        messages.success(request, 'The Ticket has been Deleted')
        return HttpResponseRedirect(arg_num)


class AllToDoView(APIView):
    def get(self, request):
        tkt_id = request.query_params.get('ticket_id')
        response = TicketAct().get_all_todo(tkt_id)
        return Response(response, status=status.HTTP_200_OK)
