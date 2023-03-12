import stripe
from dotenv import load_dotenv

load_dotenv()

import os

api_key = os.environ.get('STRIPE_API_KEY')

stripe.api_key = api_key

class Customer():
    # 
    def __init__(
        self,
        name: str,
        email: str,
        phone: str,
        line1: str,
        line2: str,
        city: str,
        state: str,
        postal_code: str,
        country: str,
        ) -> None:
        self.name=name
        self.email=email
        self.phone=phone
        self.address={
            "line1": line1,
            "line2": line2,
            "city": city,
            "state": state,
            "postal_code": postal_code,
            "country": country
        }
    
    def __repr__(self):
        customer = {
            "name": f"{self.name}",
            "email": f"{self.email}",
            "phone": f"{self.phone}",
            "address": f"{self.address['line1']} {self.address['line2']}",
            "city": self.address['city'],
            "state": self.address['state'],
            "country": self.address['country'],
            "postal_code": self.address['postal_code']
        }
        return f"Customer({customer})"
    
    def create(self):
        customer = stripe.Customer.create(
            name=self.name,
            email=self.email,
            phone=self.phone,
            address=self.address
            )
        return customer


class Charge:
    def __init__(self, amount, currency, payment_method):
        self.amount = amount
        self.currency = currency
        self.payment_method = payment_method
        
    def create(self):
        charge = stripe.Charge.create(
            amount=self.amount,
            currency=self.currency,
            payment_method=self.payment_method
        )
        
        # Получаем данные из ответа и сохраняем их в объекте Charge
        self.id = charge.id
        self.status = charge.status
        
        return self
    
    def __repr__(self):
        charge = {
            'id': self.id,
            'amount': self.amount,
            'currency': self.currency,
            'status': self.status,
            'payment_method': self.payment_method
        }

        return f'Charge({charge})'
            

class Product:
    def __init__(self, name, active=True, description=None, metadata=None):
        self.name = name
        self.active = active
        self.description = description
        self.metadata = metadata
        self.id = None
        
    def create(self):
        product = stripe.Product.create(
            name=self.name,
            active=self.active,
            description=self.description,
            metadata=self.metadata
        )
        
        # Получаем данные из ответа и сохраняем их в объекте Product
        self.id = product.id
        
        return self
    
    def __repr__(self):
        product = {
            'id': self.id,
            'name': self.name,
            'active': self.active,
            'description': self.description,
            'metadata': self.metadata
        }

        return f'Product({product})'

class Subscription:
    def __init__(self, customer, items, cancel_at_period_end=None, currency=None, default_payment_method=None, description=None, metadata=None, payment_behavior=None):
        self.customer = customer
        self.items = items
        self.cancel_at_period_end = cancel_at_period_end
        self.currency = currency
        self.default_payment_method = default_payment_method
        self.description = description
        self.metadata = metadata
        self.payment_behavior = payment_behavior
        self.id = None
        
    def create(self):
        subscription = stripe.Subscription.create(
            customer=self.customer,
            items=self.items,
            cancel_at_period_end=self.cancel_at_period_end,
            currency=self.currency,
            default_payment_method=self.default_payment_method,
            description=self.description,
            metadata=self.metadata,
            payment_behavior=self.payment_behavior
        )
        
        # Получаем данные из ответа и сохраняем их в объекте Subscription
        self.id = subscription.id
        
        return self
    
    def __repr__(self):
        subscription = {
            'id': self.id,
            'customer': self.customer,
            'items': self.items,
            'cancel_at_period_end': self.cancel_at_period_end,
            'currency': self.currency,
            'default_payment_method': self.default_payment_method,
            'description': self.description,
            'metadata': self.metadata,
            'payment_behavior': self.payment_behavior
        }
        
        return f'Subscription({subscription})'    


class Plan():
    def __init__(self, amount, currency, interval, product, active=None, metadata=None, nickname=None):
        self.amount = amount
        self.currency = currency
        self.interval = interval
        self.product = product
        self.active = active
        self.metadata = metadata
        self.nickname = nickname
        self.id = None
        
    def create(self):
        plan = stripe.Plan.create(
            amount=self.amount,
            currency=self.currency,
            interval=self.interval,
            product=self.product,
            active=self.active,
            metadata=self.metadata,
            nickname=self.nickname
        )
        
        # Получаем данные из ответа и сохраняем их в объекте Plan
        self.id = plan.id
        
        return self
    
    def __repr__(self):
        plan = {
            'id': self.id,
            'amount': self.amount,
            'currency': self.currency,
            'interval': self.interval,
            'product': self.product,
            'active': self.active,
            'metadata': self.metadata,
            'nickname': self.nickname
        }

        return f'Plan({plan})'

class Price:
    def __init__(self, currency, product, unit_amount, active=True, metadata=None, nickname=None, recurring=None):
        self.currency = currency
        self.product = product
        self.unit_amount = unit_amount
        self.active = active
        self.metadata = metadata
        self.nickname = nickname
        self.recurring = recurring
        self.id = None
    
    def create(self):
        price = stripe.Price.create(
            currency=self.currency,
            product=self.product,
            unit_amount=self.unit_amount,
            active=self.active,
            metadata=self.metadata,
            nickname=self.nickname,
            recurring=self.recurring
        )
        
        self.id = price.id
        
        return self
        
    
    def __repr__(self) -> str:
        price = {
            'currency': self.currency,
            'product': self.product,
            'unit_amount': self.unit_amount,
            'active': self.active,
            'metadata': self.metadata,
            'nickname': self.nickname,
            'recurring': self.recurring   
        }

        return f'Price({price})'