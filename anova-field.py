import os
import pandas as pd
import numpy as np
import seaborn as sns
import scipy
from matplotlib import pyplot
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
from statsmodels.formula.api import ols
# from statsmodels.stats.anova import AnovaRM
# from statsmodels.regression.mixed_linear_model import MixedLMResults

#%%
# Sig: first, last, phone, dob, sex (culture only), email (culture only), zip, ssn, address (scenario only), citizenship, website, relationship
# Not sig: race, password, username

# read in data
not_complete = pd.read_csv('data_notcomplete.csv')  # , usecols=['culture', 'scenario', 'interface', 'percent']
not_complete.columns

# perform 2-way ANOVA for each field given the culture and scenario
model = ols('first ~ culture + scenario + culture:scenario', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('last ~ culture + scenario + culture:scenario', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('phone ~ culture + scenario + culture:scenario', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('dob ~ culture + scenario + culture:scenario', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('sex ~ culture + scenario + culture:scenario', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('race ~ culture + scenario + culture:scenario', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('email ~ culture + scenario + culture:scenario', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('zip ~ culture + scenario + culture:scenario', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('ssn ~ culture + scenario + culture:scenario', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('address ~ culture + scenario + culture:scenario', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('citizenship ~ culture + scenario + culture:scenario', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('website ~ culture + scenario + culture:scenario', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('password ~ culture + scenario + culture:scenario', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('username ~ culture + scenario + culture:scenario', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('relationship ~ culture + scenario + culture:scenario', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)


#%% T-Test
kor = not_complete.query("culture == 'Korea'").copy()
usa = not_complete.query("culture == 'USA'").copy()

t1, p1 = scipy.stats.ttest_ind(kor[kor['scenario'] == 'Bank'].sex, usa[usa['scenario'] == 'Bank'].sex)
print(t1, p1)

kor.columns
#%% T-test
# Kor vs. USA for not completing the task
kor.head()
# kor['percent_notcomplete']
t1, p1 = scipy.stats.ttest_ind(kor['percent_notcomplete'], usa['percent_notcomplete'])
print(t1, p1)

t1, p1 = scipy.stats.ttest_ind(kor[kor['scenario'] == 'Bank'].percent_notcomplete, usa[usa['scenario'] == 'Bank'].percent_notcomplete)
print(t1, p1)

t1, p1 = scipy.stats.ttest_ind(kor[kor['scenario'] == 'Shop'].percent_notcomplete, usa[usa['scenario'] == 'Shop'].percent_notcomplete)
print(t1, p1)

#%%
bank = not_complete.query("scenario == 'Bank'").copy()
shop = not_complete.query("scenario == 'Shop'").copy()

usa_var = bank.loc[bank['culture'] == "USA"].ssn
kor_var = bank.loc[bank['culture'] == "Korea"].ssn


# perform 2-way ANOVA for each field given the culture and scenario
model = ols('first ~ culture + interface + culture:interface', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('last ~ culture + interface + culture:interface', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('phone ~ culture + interface + culture:interface', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('dob ~ culture + interface + culture:interface', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('sex ~ culture + interface + culture:interface', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('race ~ culture + interface + culture:interface', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('email ~ culture + interface + culture:interface', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('zipc ~ culture + interface + culture:interface', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('ssn ~ culture + interface + culture:interface', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('address ~ culture + interface + culture:interface', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('citizenship ~ culture + interface + culture:interface', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('website ~ culture + interface + culture:interface', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('password ~ culture + interface + culture:interface', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('username ~ culture + interface + culture:interface', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)

model = ols('relationship ~ culture + interface + culture:interface', data=not_complete).fit()
sm.stats.anova_lm(model, typ=2)
