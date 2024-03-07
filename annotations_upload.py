import numpy as np
import pandas as pd
from statsmodels.stats.inter_rater import fleiss_kappa

from krippendorff_alpha import *
import statsmodels
def convert_to_int_emotion(word):
    if word == "Angažovanost":
        return 1
    elif word == "Frustracija":
        return 2
    elif word == "Nezainteresovanost":
        return 3
    elif word == "Umor":
        return 4
    elif word == "Zbunjenost":
        return 5
    return 6

def convert_to_int_aspect(word):
    if word == "Tutor":
        return 1
    elif word == "Lekcija":
        return 2
    elif word == "Instrukcioni materijali":
        return 3
    elif word == "Zadaci":
        return 4
    elif word == "Projekat":
        return 5
    return 6

df = pd.read_excel('data/Anotiranje_3_KGG.xlsx')
print(df.T)
array_emotion = np.array([df.T.to_numpy()[1], df.T.to_numpy()[4], df.T.to_numpy()[7], df.T.to_numpy()[10], df.T.to_numpy()[13]])
array_aspect = np.array([df.T.to_numpy()[2], df.T.to_numpy()[5], df.T.to_numpy()[8], df.T.to_numpy()[11], df.T.to_numpy()[14]])
# array = [convert_to_int(x) for x in np.nditer(array)]

for idx, x in np.ndenumerate(array_emotion):
    number = convert_to_int_emotion(x)
    array_emotion[idx] = number

for idx, x in np.ndenumerate(array_aspect):
    number = convert_to_int_aspect(x)
    array_aspect[idx] = number

print("nominal metric: %.3f" % krippendorff_alpha(array_emotion, nominal_metric))
print("interval metric: %.3f" % krippendorff_alpha(array_emotion, interval_metric))
print("nominal metric: %.3f" % krippendorff_alpha(array_aspect, nominal_metric))
print("interval metric: %.3f" % krippendorff_alpha(array_aspect, interval_metric))
# print("fleiss kapa: %.3f" % fleiss_kappa(array_emotion, method='fleiss'))
# print("fleiss kapa: %.3f" % fleiss_kappa(array_aspect, method='fleiss'))