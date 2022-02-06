import numpy as np
import pandas as pd
data = pd.DataFrame()
data['Gender'] = ['m','m','m','m','f','f','f','f','m','m','m','m','f','f','f','f']
data['Height'] = [1.7,1.75,1.8,1.72,1.65,1.6,1.55,1.7,1.55,1.7,1.7,1.75,1.65,1.6,1.45,1.57]
data['Weight'] = [60,65,70,62,50,55,45,52,65,71,59,62,45,43,56,52]
data['Footsize'] = [8,7,8,8,7,6,5,6,7,8,9,7,6,5,6,7]
print(data)
pe = pd.DataFrame()
pe['Gender'] = ['m','f','m','f','f','f','m','m']
pe['Height']=[1.7,1.5,1.62,1.45,1.54,1.66,1.82,1.7]
pe['Weight']=[60,45, 70,55,53,52,80,75]
pe['Footsize']=[7,6,8,6,6,6,8,7]
print(pe)
nm = data['Gender'][data['Gender']=='m'].count()
nf = data['Gender'][data['Gender']=='f'].count()
tot = data['Gender'].count()
pm = nm/tot
pf = nf/tot
print(f"No of Males : {nm}\n No of Females : {nf} \n Total no : {tot} \n P(Male) : {pm} \n P(Female) : {pf}")
means = data.groupby('Gender').mean()
var = data.groupby('Gender').var()
print(f'Means:\n {means}\n Variance :\n {var}')
mhm = means['Height'][means.index == 'm'].values[0]
mwm = means['Weight'][means.index == 'm'].values[0]
mfm = means['Footsize'][means.index == 'm'].values[0]
mhv = var['Height'][var.index == 'm'].values[0]
mwv = var['Weight'][var.index == 'm'].values[0]
mfv = var['Footsize'][var.index == 'm'].values[0]
print("Male:")
print(f"Height mean : {mhm} \nHeight variance : {mhv} \nWeight mean : {mwm} \nWeight variance : {mwv} \nFootsize mean : {mfm} \nFootsize variance : {mfv} \n")
fhm = means['Height'][means.index == 'f'].values[0]
fwm = means['Weight'][means.index == 'f'].values[0]
ffm = means['Footsize'][means.index == 'f'].values[0]
fhv = var['Height'][var.index == 'f'].values[0]
fwv = var['Weight'][var.index == 'f'].values[0]
ffv = var['Footsize'][var.index == 'f'].values[0]
print("Female:")
print(f"Height mean : {fhm} \nHeight variance : {fhv} \nWeight mean : {fwm} \nWeight variance : {fwv} \nFootsize mean : {ffm} \nFootsize variance : {ffv} \n")

def P_xgy(x,mean_y,var_y):
  p = 1/(np.sqrt(2*np.pi*var_y)) * np.exp(-1 * ((x - mean_y)**2)/(2*var_y))
  return p

count = 0

for i in range(len(pe)):
  prob_male = pm * P_xgy(pe['Height'][i], mhm, mhv) * P_xgy(pe['Weight'][i], mwm, mwv) * P_xgy(pe['Footsize'][i], mfm, mfv)
  print(prob_male)
  prob_female = pf * P_xgy(pe['Height'][i], fhm, fhv) * P_xgy(pe['Weight'][i], fwm, fwv) * P_xgy(pe['Footsize'][i], ffm, ffv)
  print(prob_female)
  if prob_male > prob_female:
    print(f" {i} : Male")
    if pe['Gender'][i] == 'm':
      count += 1
  else:
    print(f" {i} : Female")
    if pe['Gender'][i] == 'f':
      count += 1
print(f'Accuracy : {(count/8)*100}')