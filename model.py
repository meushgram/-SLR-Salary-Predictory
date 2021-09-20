import pandas as pd
import numpy as np
df = pd.read_csv('Salary_Data.csv')
import statsmodels.formula.api as smf
model = smf.ols("Salary~YearsExperience",data = df).fit()
print(model.summary())