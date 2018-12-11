without_age = data[data.Age.isnull()]
with_age = data[~data.Age.isnull()]
