import pandas as pd
import random

# 1)

List1 = [7, 11, 13, 17]
Series1 = pd.Series(List1)
print(Series1)

# 2)

onehundreds = pd.Series([100, 100, 100, 100, 100])
print(onehundreds)

# 3)

randomseries = pd.Series([random.randint(0, 100) for i in range(20)])
print(randomseries)

# 4)

temperatures = pd.Series(
    [98.6, 98.9, 100.2, 97.9], index=["Julie", "Charlie", "Sam", "Andrea"]
)
print(temperatures)

# 5)

dictionary1 = {"Julie": 98.6, "Charlie": 98.9, "Sam": 100.2, "Andrea": 97.9}
temperatureseries = pd.Series(dictionary1)
print(temperatureseries)