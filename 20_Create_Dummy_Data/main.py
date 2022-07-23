import pandas as pd
from faker import Faker

fake = Faker()

print(fake.name())
print(fake.address())
print(fake.text())

print("#" * 100)

fake = Faker()
data = [fake.profile() for i in range(100)]
data = pd.DataFrame(data)
print(data.head())
print(data.shape)
