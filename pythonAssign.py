''' Python Assignment
    Analysis of Census data
    Submitted by Sandip Dewalkar
    22/07/2022'''

import pandas as pd
import numpy as np

#reading excel sheet
df = pd.read_excel(r'C:\Users\SandipDewalkar\Desktop\Python training\Python_Project\Census.xlsx', header=[1,2,3,4,5,6])
#print(df)
pd.set_option('display.max_rows', 4000)
pd.set_option('display.max_columns', 50)

index = df.columns
#print(index)  #columns o dataframe

#print(df[index[1]]) #state code

#unique state code
#print(df[index[1]].unique())

#creating excel sheet for each statecode with literacy andd illeteracy percentage
writer = pd.ExcelWriter("SplitedStateData1.xlsx", engine='xlsxwriter')
for statecode in df[index[1]].unique():
    newDf = df[df[index[1]] == statecode]

    # calculating illiteracy (total person / illiterate person) *100
    illiteracy = 100 * (df[index[9]] / df[index[6]])

    # calculating illiteracy in male (total male / illiterate male) *100
    illiteracy_male = 100 * (df[index[10]] / df[index[7]])

    # calculating illiteracy in female (total female / illiterate female) *100
    illiteracy_female = 100 * (df[index[11]] / df[index[8]])

    # calculating literacy (total person / literate person) *100
    literacy = 100 * (df[index[12]] / df[index[6]])

    # calculating literacy in male (total male / literate male) *100
    literacy_male = 100 * (df[index[13]] / df[index[7]])

    # calculating literacy in female (total female / literate female) *100
    literacy_female = 100 * (df[index[14]] / df[index[8]])

    newDf = newDf.assign(illiteracy= illiteracy, \
                       illiteracy_male= illiteracy_male,\
                       illiteracy_female=illiteracy_female,\
                       literacy=literacy,\
                       literacy_male=literacy_male,\
                       literacy_female=literacy_female)
    #df2['illiteracy'] = np.round(df2['illiteracy'], decimals = 2)
    newDf=np.round(newDf,decimals=2)
    #df2.to_excel(writer, sheet_name=str(statecode), index =False)
    newDf.to_excel(writer, sheet_name=str(statecode))

writer.save()


#calculating percentage of person with different qualification level
writer2 = pd.ExcelWriter("SplitedStateData2.xlsx", engine='xlsxwriter')
for statecode in df[index[1]].unique():
    newDf2 = df[df[index[1]] == statecode]

    #percentage or education level
    below_primary_level = 100 * (df[index[18]] / df[index[6]])
    primary_level = 100 * (df[index[21]] / df[index[6]])
    middle_level = 100 * (df[index[24]] / df[index[6]])
    secondary_level = 100 * (df[index[27]] / df[index[6]])
    higher_secondary_level = 100 * (df[index[30]] / df[index[6]])
    non_technical_diploma = 100 * (df[index[33]] / df[index[6]])
    technical_diploma = 100 * (df[index[36]] / df[index[6]])
    graduate_and_above = 100 * (df[index[39]] / df[index[6]])

    newDf2 = newDf2.assign(below_primary_level= below_primary_level, \
                       primary_level= primary_level,\
                       middle_level=middle_level,\
                       secondary_level=secondary_level,\
                       higher_secondary_level=higher_secondary_level,\
                       non_technical_diploma=non_technical_diploma, \
                       technical_diploma=technical_diploma, \
                       graduate_and_above=graduate_and_above)

    newDf2=np.round(newDf2,decimals=2)
    #df2.to_excel(writer, sheet_name=str(statecode), index =False)
    newDf2.to_excel(writer2, sheet_name=str(statecode))

writer2.save()

#calculating good literacy rate in each state for male

writer = pd.ExcelWriter("GoodLiteracyRate.xlsx", engine='xlsxwriter')
df1 = df.filter(items=[index[1],index[3],index[4],index[5]])
#we can filter rows for all ages
#df1=df1[df[index[5]] == 'All ages']
good_literacy_male = 100 * (df[index[13]] / df[index[7]])
df1 =df1.assign(good_literacy_male = good_literacy_male)
df1=np.round(df1,decimals=2)
df1=df1.sort_values(by='good_literacy_male', ascending=False)
df1.to_excel(writer, sheet_name='good_literacy_male')

#calculating good literacy rate in each state for male
df2 = df.filter(items=[index[1],index[3],index[4],index[5]])
#we can filter rows for all ages
#df2=df2[df[index[5]] == 'All ages']
good_literacy_female = 100 * (df[index[14]] / df[index[8]])
df2 = df2.assign(good_literacy_female = good_literacy_female )
df2 = np.round(df2,decimals=2)
df2 = df2.sort_values(by='good_literacy_female', ascending=False)
df2.to_excel(writer, sheet_name='good_literacy_female')

#calculating good literacy rate in each education level
#below_primary_level
df3 = df.filter(items=[index[1],index[3],index[4],index[5]])
#we can filter rows for all ages
#df3=df3[df[index[5]] == 'All ages']
below_primary_level = 100 * (df[index[18]] / df[index[6]])
df3 = df3.assign(below_primary_level = below_primary_level )
df3 = np.round(df3,decimals=2)
df3 = df3.sort_values(by='below_primary_level', ascending=False)
df3.to_excel(writer, sheet_name='below_primary_level')


#primary_level
df4 = df.filter(items=[index[1],index[3],index[4],index[5]])
#we can filter rows for all ages
#df4=df4[df[index[5]] == 'All ages']
primary_level = 100 * (df[index[21]] / df[index[6]])
df4 = df4.assign(primary_level = primary_level )
df4 = np.round(df4,decimals=2)
df4 = df4.sort_values(by='primary_level', ascending=False)
df4.to_excel(writer, sheet_name='primary_level')

#middle_level
df5 = df.filter(items=[index[1],index[3],index[4],index[5]])
#we can filter rows for all ages
#df5=df5[df[index[5]] == 'All ages']
middle_level = 100 * (df[index[24]] / df[index[6]])
df5 = df5.assign(middle_level = middle_level )
df5 = np.round(df5,decimals=2)
df5 = df5.sort_values(by='middle_level', ascending=False)
df5.to_excel(writer, sheet_name='middle_level')

#secondary_level
df6 = df.filter(items=[index[1],index[3],index[4],index[5]])
#we can filter rows for all ages
#df6=df6[df[index[5]] == 'All ages']
secondary_level = 100 * (df[index[27]] / df[index[6]])
df6 = df6.assign(secondary_level = secondary_level )
df6 = np.round(df6,decimals=2)
df6 = df6.sort_values(by='secondary_level', ascending=False)
df6.to_excel(writer, sheet_name='secondary_level')

#higher_secondary_level
df7 = df.filter(items=[index[1],index[3],index[4],index[5]])
#we can filter rows for all ages
#df7=df7[df[index[5]] == 'All ages']
higher_secondary_level = 100 * (df[index[30]] / df[index[6]])
df7 = df7.assign(higher_secondary_level = higher_secondary_level )
df7 = np.round(df7,decimals=2)
df7 = df7.sort_values(by='higher_secondary_level', ascending=False)
df7.to_excel(writer, sheet_name='higher_secondary_level')

#non_technical_diploma
df8 = df.filter(items=[index[1],index[3],index[4],index[5]])
#we can filter rows for all ages
#df8=df8[df[index[5]] == 'All ages']
non_technical_diploma = 100 * (df[index[33]] / df[index[6]])
df8 = df8.assign(non_technical_diploma = non_technical_diploma )
df8 = np.round(df8,decimals=2)
df8 = df8.sort_values(by='non_technical_diploma', ascending=False)
df8.to_excel(writer, sheet_name='non_technical_diploma')

#technical_diploma
df9 = df.filter(items=[index[1],index[3],index[4],index[5]])
#we can filter rows for all ages
#df9=df9[df[index[5]] == 'All ages']
technical_diploma = 100 * (df[index[36]] / df[index[6]])
df9 = df9.assign(technical_diploma = technical_diploma )
df9 = np.round(df9,decimals=2)
df9 = df9.sort_values(by='technical_diploma', ascending=False)
df9.to_excel(writer, sheet_name='technical_diploma')

#graduate_and_above
df10 = df.filter(items=[index[1],index[3],index[4],index[5]])
#we can filter rows for all ages
#df10=df10[df[index[5]] == 'All ages']
graduate_and_above = 100 * (df[index[39]] / df[index[6]])
df10 = df10.assign(graduate_and_above = graduate_and_above )
df10 = np.round(df10,decimals=2)
df10 = df10.sort_values(by='graduate_and_above', ascending=False)
df10.to_excel(writer, sheet_name='graduate_and_above')


#calculating good literacy rate in each state
df11 = df.filter(items=[index[1],index[3],index[4],index[5]])
#we can filter rows for all ages
#df11=df11[df[index[5]] == 'All ages']
state_literacy = 100 * (df[index[12]] / df[index[6]])
df11 = df11.assign(state_literacy = state_literacy )
df11 = df11.groupby(index[3]).first()
df11 = np.round(df11,decimals=2)
df11 = df11.sort_values(by='state_literacy', ascending=False)
df11.to_excel(writer, sheet_name='state_literacy')
writer.save()
