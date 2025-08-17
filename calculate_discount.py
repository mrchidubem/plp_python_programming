#  Magical Discount Calculator 🌟
# This script sprinkles some discount magic on your shopping!

#  Function to calculate the final price after discount
def calculate_discount(price, discount_percent):
    # 🧙 Check if the discount is worthy (20% or more)
    if discount_percent >= 20:
        #  Apply the discount formula: price - (price * discount_percent / 100)
        final_price = price * (1 - discount_percent / 100)
        return final_price
    else:
        #  No discount? Keep the original price!
        return price

#  Main program to interact with the user
def main():
    #  Ask the user for the original price
    price = float(input("Enter the original price of the item: $"))
    
    #  Get the discount percentage
    discount_percent = float(input("Enter the discount percentage: "))
    
    #  Calculate the final price using our magical function
    final_price = calculate_discount(price, discount_percent)
    
    #  Display the result with flair
    if discount_percent >= 20:
        print(f"🎊 Hooray! After a {discount_percent}% discount, the final price is ${final_price:.2f}!")
    else:
        print(f" No discount applied. The final price remains ${final_price:.2f}.")

#  Run the program when the script is executed
if __name__ == "__main__":
    main()