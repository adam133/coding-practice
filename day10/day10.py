from src.tip_calculator import (BillAmount, NumberOfPeople, TipCalculator,
                                TipPercentage)


# a basic python tip calculator, with pydantic for type checking and validation
def main():
    print("Hello from day10!")

    bill_amount: BillAmount = input("Enter the bill amount: ")
    tip_percentage: TipPercentage = input("Enter the tip percentage: ")
    number_of_people: NumberOfPeople = input("Enter the number of people: ")

    tip_calculator = TipCalculator(bill_amount=bill_amount, tip_percentage=tip_percentage, number_of_people=number_of_people)
    print(f'Tip amount: {tip_calculator.calculate_tip}')
    print(f'Total amount: {tip_calculator.calculate_total}')
    print(f'Amount per person: {tip_calculator.calculate_amount_per_person}')


if __name__ == "__main__":
    main()
