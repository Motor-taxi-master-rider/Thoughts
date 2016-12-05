import pandas as pd
import numpy as np

years=range(1880,2011)
pieces=[]
columns=['names','sex','births']
for year in years:
    path='../pydata-book-master/ch02/names/yob%d.txt' % year
    frame=pd.read_csv(path,names=columns)
    frame['year']=year
    pieces.append(frame)
names=pd.concat(pieces,ignore_index=True)
total_births=names.pivot_table(values='births'
,index='year'
,columns='sex'
,aggfunc=sum)
#print(total_births.tail())
total_births.plot(title='Total births by sex and year')
def add_prop(group):
    births=group.births.astype(float)
    group['prop']=births/births.sum()
    return group
names=names.groupby(['year','sex']).apply(add_prop)
np.allclose(names.groupby(['year','sex']).prop.sum(),1)

def get_top1000(group):
    return group.sort_values('births',ascending=False)[:1000]

grouped=names.groupby(['year','sex'])
top1000=grouped.apply(get_top1000)
boys=top1000[top1000.sex=='M']
girls=top1000[top1000.sex=='F']
total_births=top1000.pivot_table(values='births'
,index='year'
,columns='names'
,aggfunc=sum)
subset=total_births[['John','Harry','Mary','Marilyn']]
subset.plot(subplots=True
,figsize=(12,10)
,grid=False
,title="Number of births per year")
table=top1000.pivot_table('prop',index='year',columns='sex',aggfunc=sum)
'''table.plot(title='Sum of table1000.prop by year and sex'
,yticks=np.linespace(0,1.2,13)
,xticks=range(1880,2020,10))'''

def get_quantile_count(group,q=0.5):
    group=group.sort_values('prop',ascending=False)
    return (group.prop.cumsum().searchsorted(q)+1)[0]

diversity=top1000.groupby(['year','sex']).apply(get_quantile_count)
diversity=diversity.unstack('sex')
diversity.plot(title='Number of polular names in top 50%')

get_last_letter=lambda x:x[-1]
last_letters=names.names.map(get_last_letter)
last_letters.name='last_letter'
table=names.pivot_table(values='births'
,index=last_letters
,columns=['sex','year']
,aggfunc=sum)
subtable=table.reindex(columns=[1910,1960,2010],level='year')
letter_prop=subtable/subtable.sum().astype(float)

import matplotlib.pyplot as plt
fig,axes=plt.subplots(2,1,figsize=(10,8))
letter_prop['M'].plot(kind='bar',rot=0,ax=axes[0],title='Male')
letter_prop['F'].plot(kind='bar',rot=0,ax=axes[1],title='Female',legend=False)

letter_prop=table/table.sum().astype(float)
dny_ts=letter_prop.ix[['d','n','y'],'M'].T
dny_ts.plot()

all_names=top1000.names.unique()
mask=np.array(['lesl' in x.lower() for x in all_names])
lesley_like=all_names[mask]
filtered=top1000[top1000.names.isin(lesley_like)]
filtered.groupby('names').births.sum()
table=filtered.pivot_table(values='births',index='year',columns='sex',aggfunc=sum)
table=table.div(table.sum(1),axis=0)
table.plot(style={'M':'k-','F':'k--'})
print(table)
