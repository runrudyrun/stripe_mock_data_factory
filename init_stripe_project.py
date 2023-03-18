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

for c in factory.customers:
    billing_details = {
        "name": c.name,
        "email": c.email,
        "phone": c.phone,
    }
    payment_method = factory.create_payment_method(billing_details)
    payment_method.attach(c.id)
    payment_method.set_default_payment_method(c.id)

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