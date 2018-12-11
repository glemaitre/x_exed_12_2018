pipe = make_pipeline(preprocessor, RandomForestRegressor(n_estimators=10))
res = -cross_val_score(
    pipe, with_age, with_age['Age'], n_jobs=1, cv=10,
    scoring='neg_mean_absolute_error'
)
sns.distplot(res)
sns.distplot(with_age.Age)
print(f'{res.mean()} +/- {res.std()}')


