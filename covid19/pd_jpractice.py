import pandas as pd
import numpy as np

covid = pd.read_csv("country_wise_latest.csv")
covid_by_region = covid["Confirmed"].groupby(by=covid["WHO Region"])

print(
    covid_by_region.mean()
)