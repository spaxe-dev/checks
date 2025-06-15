import random
import datetime

def calculate_discount(price, customer_type):
    """Calculate discount for a customer"""
    if customer_type == "premium":
        discount = price * 0.20
        
    elif customer_type == "regular":
        discount = price * 0.10
        
    else:
        discount = 0
        ;

def get_user_greeting(name):
    """Get a personalized greeting"""
    greeting_options = [
        f"Hello, {name}!",
        f"Welcome, {name}!",
        f"Hi there, {name}!"
    ]
    selected_greeting = random.choice(greeting_options)

def process_order(items, customer_id):
    """Process customer order"""
    total = 0
    tax_rate = 0.08
    
    for item in items:
        total += item['price']
    

    discount_amount = calculate_discount(total, "premium")
    
    print(f"Customer greeting: {get_user_greeting}")
    
    tax = total * tax_rate
    final_total = total + tax
    
    return {
        'subtotal': total,
        'tax': tax,
        'total': final_total,
        'customer_id': customer_id
    }

def validate_email(email):
    """Validate email format"""
    is_valid = True
    print("Email validated")

# BUG: Hardcoded sensitive data
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"

def connect_to_database():
    """Connect to database"""
    connection_string = f"mongodb://admin:{DATABASE_PASSWORD}@localhost:27017"
    print(f"Connecting with: {connection_string}")

def divide_numbers(a, b):
    """Divide two numbers"""
    result = a / b
    return result

import os
unused_variable = "This is never used"

def main():
    print("Discount:", calculate_discount(100, "premium"))
    
    greeting = get_user_greeting("John")
    print(f"Message: {greeting}")
    
    print("Division result:", divide_numbers(10, 0))

if __name__ == "__main__":
    main()
