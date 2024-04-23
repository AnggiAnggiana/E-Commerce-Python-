#Install midtransclient(https://github.com/Midtrans/midtrans-python-client) PIP package
#pip install midtransclient
# INTEGRATE WITH "MIDTRANS" (PAYMENT GATEWAY)
#SAMPLE REQUEST START HERE
import random
import requests
from django.http import JsonResponse
from midtransclient import Snap
from decouple import config
from stores.models import Smartphone, Foods

# MIDTRANS (PAYMENT GATEWAY) CONFIGURATION
MIDTRANS_CLIENT_KEY = config('MIDTRANS_CLIENT_KEY')
MIDTRANS_SERVER_KEY = config('MIDTRANS_SERVER_KEY')
MIDTRANS_API_BASE_URL = config('MIDTRANS_API_BASE_URL')
MIDTRANS_IS_PRODUCTION = config('MIDTRANS_IS_PRODUCTION')


def create_transaction(request):
    # Decode data from request.body
    data = request.json
    
    # Data sent from model (Smartphone & Foods)
    smartphone_data = Smartphone.objects.first() #Change method to get data
    foods_data = Foods.objects.first() #Change method to get data
    
    # Generate random order_id
    order_id = random.randint(1000, 9999)
    
    # Decide gross_amount value based on the selected product (Smartphone or Foods)
    if request.data['product_type'] == 'smartphone':
        gross_amount = smartphone_data.price
    elif request.data['product_type'] == 'foods':
        gross_amount = foods_data.food_price
    else:
        # Default value if there is no product selected
        gross_amount = 0

    # Create Snap API instance
    snap = Snap(
        # Set to true if you want Production Environment (accept real transaction).
        is_production= config('MIDTRANS_IS_PRODUCTION'),
        server_key= config('MIDTRANS_SERVER_KEY'),
        client_key= config('MIDTRANS_CLIENT_KEY'),
    )
    
    # Build API parameter
    param = {
        "transaction_details" : {
            "order_id": order_id,
            "gross_amount": gross_amount
        },
        "credit_card" : {
            "secure" : True
        },
        "item_details" : [
            {
                "id": smartphone_data.id,
                "name": smartphone_data.name,
                "quantity": data['quantity'],
                "price": smartphone_data.price,
            },
            {
                "id": foods_data.id,
                "name": foods_data.food_name,
                "quantity": data['quantity'],
                "price": foods_data.food_price,
            },
        ],
        "customer_details" : {
            "first_name": data['name'],
            "phone": data['phone'],
            "note": data['note'],
        }
    }
    
    # print(param)

    transaction = snap.create_transaction(param)

    transaction_token = transaction['token']
    
    return JsonResponse({'transaction_token': transaction_token})