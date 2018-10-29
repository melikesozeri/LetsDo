import pandas as pd
data = [
        ['D1', 'Sunny','Hot', 'High', 'Weak', 'No'],
        ['D2', 'Sunny','Hot', 'High', 'Strong', 'No'],
        ['D3', 'Overcast','Hot', 'High', 'Weak', 'Yes']
        ]
df = pd.DataFrame(data, columns=['day', 'outlook', 'temp', 'humidity', 'windy', 'play'])
print(df)
#df.info()
print(df.shape)
print(df.size)
print(df.describe())
