from factory.django import DjangoModelFactory as Factory
import factory
from customers.models import Customer
from policies.models import Policy


class CustomerFactory(Factory):
    first_name = factory.Faker('name')
    last_name = factory.Faker('name')
    dob = factory.Faker('date_this_year', before_today=True, after_today=False)

    class Meta:
        model = Customer


class PolicyFactory(Factory):
    type = Policy.PERSONAL_ACCIDENT_TYPE
    premium = factory.Faker('random_int', min=10, max=10000)
    cover = factory.Faker('random_int', min=10, max=10000)

    class Meta:
        model = Policy
