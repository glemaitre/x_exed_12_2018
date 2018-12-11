pipe = make_pipeline(preprocessor, LinearRegression())
res = -cross_val_score(
    pipe, with_age, with_age['Age'], n_jobs=1, cv=100,
    scoring='neg_mean_absolute_error'
)
sns.distplot(res)
sns.distplot(with_age.Age)
print(f'{res.mean()} +/- {res.std()}')
