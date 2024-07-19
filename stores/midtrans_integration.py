#Install midtransclient(https://github.com/Midtrans/midtrans-python-client) PIP package
#pip install midtransclient
# INTEGRATE WITH "MIDTRANS" (PAYMENT GATEWAY)
#SAMPLE REQUEST START HERE
import random
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from midtransclient import Snap
from decouple import config
from stores.models import Profile, Customers, Smartphone, Foods, Shopping_Cart
import midtransclient

# MIDTRANS (PAYMENT GATEWAY) CONFIGURATION
MIDTRANS_CLIENT_KEY = config('MIDTRANS_CLIENT_KEY')
MIDTRANS_SERVER_KEY = config('MIDTRANS_SERVER_KEY')
MIDTRANS_API_BASE_URL = config('MIDTRANS_API_BASE_URL')
MIDTRANS_IS_PRODUCTION = config('MIDTRANS_IS_PRODUCTION')


@csrf_exempt
def create_midtrans_transaction(request):
    if request.method == 'POST':
        user = request.user
        profile_instance = Profile.objects.get(user=user)
        customer = Customers.objects.get(owner_id=profile_instance)
        owner = Shopping_Cart.objects.filter(user=customer).first()
        
        # first_name = user.first_name
        # last_name = user.last_name
        first_name = customer.first_name
        last_name = customer.last_name
        # address = f"{user.street}, {user.district}, {user.city}, {user.province}, {user.country} ({user.postal_code})"
        address = f"{customer.street}, {customer.district}, {customer.city}, {customer.province}, {customer.country} ({customer.postal_code})"
        # phone_number = user.phone_number
        phone_number = customer.phone_number
        gross_amount = request.POST.get('totalCost')

        # Create Snap API instance
        snap = midtransclient.Snap(
            # Set to true if you want Production Environment (accept real transaction).
            # is_production=False,
            is_production=MIDTRANS_IS_PRODUCTION,
            # server_key='YOUR_SERVER_KEY'
            server_key= MIDTRANS_SERVER_KEY
        )
        
        # Build API parameter
        param = {
            "transaction_details": {
                "order_id": f"order-{random.randint(1000, 9999)}",
                "gross_amount": int(gross_amount.replace('Rp.', '').replace('.', ''))
            },
            "credit_card":{
                "secure" : True
            },
            "customer_details":{
                "first_name": first_name,
                "last_name": last_name,
                "email": address,
                "phone": phone_number
            }
        }

        transaction = snap.create_transaction(param)

        transaction_token = transaction['token']
        
        return JsonResponse({'token': transaction_token})