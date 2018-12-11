preprocessor = make_column_transformer(
    (['Sex'], OneHotEncoder()),
    (['Pclass'], OrdinalEncoder()),
    (['Fare'], StandardScaler())
)
preprocessor.fit(with_age)
preprocessor.transform(with_age)
