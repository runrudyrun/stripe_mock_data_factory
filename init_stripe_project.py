from faker import Faker
import stripe
from factories import StripeFactory
import os
import random

fake = Faker()

params = {
    'n_customers': 10,
    'n_products': 3,

}

# Инициализация stripe.api_key
stripe.api_key = os.environ.get('STRIPE_API_KEY')

# Создаю переменную объекта StripeFactory

factory = StripeFactory()

for i in range(params['n_customers']):
    factory.create_customer()
print(f'{params["n_customers"]} customers created')

for i in range(params['n_products']):
    factory.create_product()
print(f'{params["n_products"]} products created')

for product in factory.products:
    price = factory.create_price(product)
    factory.create_plan(product)
print('Plans created')

for customer in factory.customers:
    factory.create_subscription(customer, random.choice(factory.prices))
print('Subscriptions created')