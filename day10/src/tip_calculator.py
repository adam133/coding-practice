from decimal import Decimal

from pydantic import BaseModel, computed_field, condecimal, conint

type BillAmount = condecimal(gt=0, le=1000000, decimal_places=2)
type TipPercentage = conint(gt=-1, le=100)
type NumberOfPeople = conint(gt=0, le=100)


class TipCalculator(BaseModel):
    bill_amount: BillAmount
    tip_percentage: TipPercentage
    number_of_people: NumberOfPeople

    @computed_field
    @property
    def calculate_tip(self) -> condecimal(gt=0, le=1000000, decimal_places=2):
        return self.bill_amount * (self.tip_percentage / Decimal(100))

    @computed_field
    @property
    def calculate_total(self) -> condecimal(gt=0, le=1000000, decimal_places=2):
        return self.bill_amount + self.calculate_tip

    @computed_field
    @property
    def calculate_total_per_person(
        self,
    ) -> BillAmount:
        return round(self.calculate_total / self.number_of_people, 2)
