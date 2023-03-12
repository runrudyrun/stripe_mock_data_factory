from faker import Faker
import random
from models import Customer, Charge, Product, Subscription, Plan, Price 

fake = Faker()

class StripeFactory:
    def __init__(self):
        self.customers = []
        self.charges = []
        self.plans = []
        self.subscriptions = []
        self.products = []
        self.prices = []
        
    
    def create_customer(self):
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()
        line1 = fake.street_address()
        line2 = fake.secondary_address()
        city = fake.city()
        state = fake.state()
        postal_code = fake.postalcode()
        country = fake.country()
        
        self.customers.append(
            Customer(
                name=name,
                email=email,
                phone=phone,
                line1=line1,
                line2=line2,
                city=city,
                state=state,
                postal_code=postal_code,
                country=country
            ).create()
        )
    

    def create_charge(self):
        amount = random.randint(10, 1000)
        currency = 'usd'
        payment_method = fake.credit_card_number()
        
        self.charges.append(
            Charge(
                amount=amount,
                currency=currency,
                payment_method=payment_method
            ).create()
        )
    

    def create_product(self):
        name = fake.catch_phrase()
        active = True
        description = fake.paragraph()
        metadata = {
            'category': fake.word(ext_word_list=['fruits','vegetables','other']),
            'subcategory': fake.word(ext_word_list=['1category','2category','3category'])
        }
        
        self.products.append(
            Product(
                name=name,
                active=active,
                description=description,
                metadata=metadata
            ).create()
        )
    

    def create_subscription(self, customer, price):
        items = [{
            'price': price.id
        }]
        cancel_at_period_end = False
        currency = 'usd'
        default_payment_method = fake.credit_card_number()
        description = fake.sentence()
        metadata = {
            'subscription_type': fake.word(ext_word_list=[
                'basic',
                'plus',
                'premium'
            ])
        }
        payment_behavior = random.choice(['default_incomplete', 'allow_incomplete', 'error_if_incomplete'])
        
        self.subscriptions.append(
            Subscription(
                customer=customer.id,
                items=items,
                cancel_at_period_end=cancel_at_period_end,
                currency=currency,
                default_payment_method=default_payment_method,
                description=description,
                metadata=metadata,
                payment_behavior=payment_behavior
            ).create()
        )
    

    def create_plan(self, product):
        amount = random.randint(10, 1000)
        currency = 'usd'
        interval = 'month'
        active = True
        metadata = {
            'plan_type': fake.word()
        }
        nickname = fake.word()
        
        self.plans.append(
                Plan(
                amount=amount,
                currency=currency,
                interval=interval,
                product=product.id,
                active=active,
                metadata=metadata,
                nickname=nickname
            )
        )
    

    def create_price(self, product):
           
        currency = 'usd'
        rel_product = product
        unit_amount = fake.random_int(min=1, max=1000000)
        active = fake.pybool()
        metadata = {"key": fake.word(), "value": fake.word()}
        nickname = fake.word()
        recurring = {"interval": fake.word()}

        self.prices.append(
            Price(
                currency=currency,
                product=rel_product,
                unit_amount=unit_amount,
                active=active,
                metadata=metadata,
                nickname=nickname,
                recurring=recurring
            )
        )