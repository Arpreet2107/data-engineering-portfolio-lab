# File: bank_package/account.py
"""
Package: bank_package
Module: account.py
"""

class Account:
    def __init__(self):
        # Public member (accessible everywhere)
        self.name = ""
        
        # Protected member (accessible in package and subclasses)
        self._email = ""
        
        # Private member (accessible only within class)
        self.__password = ""
    
    # Public setter method for private password
    def set_password(self, password):
        self.__password = password
    
    # Public getter method for private password
    def get_password(self):
        return self.__password
    
    # Protected method (intended for internal use)
    def _validate_email(self):
        if "@" in self._email:
            return True
        return False
    
    # Private method (internal use only)
    def __encrypt_password(self):
        return "*" * len(self.__password)
    
    # Public method to display account info
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self._email}")
        print(f"Password (encrypted): {self.__encrypt_password()}")

# Subclass demonstrating protected access
class PremiumAccount(Account):
    def upgrade_account(self):
        # Can access protected member from parent
        if self._validate_email():
            print(f"Upgrading account for {self.name} with email {self._email}")
        else:
            print("Invalid email format")
        
        # Cannot access private member directly
        # print(self.__password)  # This would fail

# Main execution (similar to Java's main method)
def main():
    # Create account object
    a1 = Account()
    
    # Setting public member
    a1.name = "Apna College"
    
    # Setting protected member (accessible but not recommended directly)
    a1._email = "hello@apnacollege.com"
    
    # Setting private member via setter method
    a1.set_password("abcd")
    
    # Display account information
    a1.display_info()
    
    # Access through getter
    print(f"\nRetrieved password: {a1.get_password()}")
    
    # Demonstrate PremiumAccount
    print("\n--- Premium Account Demo ---")
    premium = PremiumAccount()
    premium.name = "VIP User"
    premium._email = "vip@example.com"
    premium.set_password("vip123")
    premium.upgrade_account()

# Entry point
if __name__ == "__main__":
    main()