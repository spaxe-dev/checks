import random
import datetime

def calculate_discount(price, customer_type):
    """Calculate discount for a customer"""
    if customer_type == "premium":
        discount = price * 0.20
        # BUG: Function doesn't return the discount!
    elif customer_type == "regular":
        discount = price * 0.10
        # BUG: Also doesn't return here!
    else:
        discount = 0
        # BUG: And doesn't return here either!

def get_user_greeting(name):
    """Get a personalized greeting"""
    greeting_options = [
        f"Hello, {name}!",
        f"Welcome, {name}!",
        f"Hi there, {name}!"
    ]
    selected_greeting = random.choice(greeting_options)
    # BUG: Creates the greeting but never returns it!

def process_order(items, customer_id):
    """Process customer order"""
    total = 0
    tax_rate = 0.08
    
    for item in items:
        total += item['price']
    
    # BUG: Unused variable
    discount_amount = calculate_discount(total, "premium")
    
    # BUG: Using the function incorrectly - not calling it
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
    # BUG: No actual validation logic!
    is_valid = True
    # BUG: Should return the validation result
    print("Email validated")

# BUG: Hardcoded sensitive data
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"

def connect_to_database():
    """Connect to database"""
    # BUG: Using hardcoded password
    connection_string = f"mongodb://admin:{DATABASE_PASSWORD}@localhost:27017"
    print(f"Connecting with: {connection_string}")

def divide_numbers(a, b):
    """Divide two numbers"""
    # BUG: No division by zero check!
    result = a / b
    return result

# BUG: Unused import and variable
import os
unused_variable = "This is never used"

def main():
    # BUG: Function called without parentheses
    print("Discount:", calculate_discount(100, "premium"))
    
    # BUG: Function returns None but we're trying to use the result
    greeting = get_user_greeting("John")
    print(f"Message: {greeting}")
    
    # BUG: Potential division by zero
    print("Division result:", divide_numbers(10, 0))

if __name__ == "__main__":
    main()
