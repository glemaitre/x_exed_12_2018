pipe = make_pipeline(preprocessor, RandomForestRegressor())
gridsearch = GridSearchCV(
    pipe,
    param_grid={'randomforestregressor__n_estimators': [5, 10, 100]},
    cv=10, iid=False
)
res = -cross_val_score(
    gridsearch, with_age, with_age['Age'], n_jobs=1, cv=10,
    scoring='neg_mean_absolute_error'
)
sns.distplot(res)
sns.distplot(with_age.Age)
print(f'{res.mean()} +/- {res.std()}')


