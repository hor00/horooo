import pandas as pd
import time
def making():
    red_df.to_csv('winequality-red2.csv',index=False)
    white_df.to_csv('winequality-white2.csv',index=False)
def red():
    red_df.head()
    red_df.insert(0,column='type',value='red')
    white_df.insert(0,column='type',value='white')
    red_df.head()
    red_df.shape
def white():
    white_df.head()
    white_df.insert(0,column='type',value='white')
    white_df.head()
    white_df.shape
def conect():
    wine=pd.concat([red_df,white_df])
    wine.shape
    #win(wine)
    #winsave(wine)
    wine.to_csv('wine.csv',index=False)
    #print(wine.info())
    wine.columns=wine.columns.str.replace(' ','_')
    wine.head()
    wine.describe()
    wine.to_csv('wine.csv',index=False)
red_df=pd.read_csv('E:\mygit\winedate\winequality-red.csv',sep=';')
white_df=pd.read_csv('E:\mygit\winedate\winequality-white.csv',sep=';')

red()
white()
conect()