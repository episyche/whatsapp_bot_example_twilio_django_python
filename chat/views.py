from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from django.conf import settings
# Create your views here.
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

# get userinput and reply 
class SendMessage(APIView):
    def post(self, request):
        try:
            data = request.data
            data_dict = data.dict()
            print('-----data_dict ' , data_dict)
            msg = data_dict['Body']
            resp = MessagingResponse()
            if (msg == 'Hi'):
                resp.message('''I am chatbot assisted designed to show the blogs of our compnay 
                             \n\nTo know more about Stripe payment gateway integration - https://episyche.com/blog/how-to-integrate-stripe-payment-gateway-in-django-and-react-for-the-subscription-use-case 
                             \n\nTo read all our blogs please visit https://episyche.com/blog''')
            else:
                resp.message('Your Msg is -- {}'.format(msg))

            return HttpResponse(resp ,  content_type='application/xml')
        except Exception as err:
            print('er----- ',err , '\n\n')
            return HttpResponse(err)