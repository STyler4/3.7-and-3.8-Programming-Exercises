sandwich = {
    "Bread": {
        "Wholemeal": 1.00,
        "White": 0.80,
        "Cheesy White": 1.20,
        "Gluten Free": 1.40,
    },
    "Meat": {
        "Chicken": 2.69,
        "Beef": 3.00,
        "Salami": 4.00,
        "Vegan Slice": 3.30
    },
    "Garnish": {
        "Onion": 1.69,
        "Tomato": 1.00,
        "Lettuce": 2.00,
        "Cheese": 2.50
    }
}


# allows program to be run again on command
def main():
    def sandwich_selection(category):
        # counter for while loop
        counter = 0
        # Prints each category separately
        print(f"\navailable {category} options: ")

        # loops through option and its correspondant price for each category separately
        for choice, price in sandwich[category].items():
            print(f"{choice}: ${price}")

        # loops until all three components have been successfully picked
        while counter < 3:
            choice = input(f"Select your {category}: ").strip()
            if choice in sandwich[category]:
                counter += 1
                return choice
            # if choice not in the category loops again
            else:
                print("Invalid choice. Please try again.")
# User choices for each category
bread_choice = sandwich_selection("Bread")
meat_choice = sandwich_selection("Meat")
garnish_choice = sandwich_selection("Garnish")
