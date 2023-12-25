import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():

    df = pd.read_csv('epa-sea-level.csv')
    Lin_Reg = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    y2=Lin_Reg.intercept + Lin_Reg.slope * df['Year']
    sns.scatterplot(x='Year',y='CSIRO Adjusted Sea Level',data=df,label='CSIRO Sea Level')
    sns.lineplot(x='Year',y= y2,data=df,color='r',label='fitted line')
    plt.title('Sea Level by CSIRO')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')


    df_last = df[df['Year']>=2000]
    Lin_Reg_Last = linregress(x=df_last['Year'], y=df_last['CSIRO Adjusted Sea Level'])
    print(Lin_Reg_Last)
    x1= df_last['Year']
    y1=df_last['CSIRO Adjusted Sea Level']
    x2=np.arange(2000,2051)
    y2=Lin_Reg_Last.intercept + Lin_Reg_Last.slope*x2
    plt.scatter(x1, y1, label='CSIRO Sea Level')
    plt.plot(x2, y2, label='fitted line',color='r')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Sea Level by CSIRO Until Year 2050')
    plt.legend()
    plt.show()
    val_2050 = Lin_Reg_Last.intercept + Lin_Reg_Last.slope*2050
    print(val_2050)

    plt.savefig('sea_level_plot.png')
    return plt.gca()