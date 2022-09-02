import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport

df = pd.read_csv('Products Data.csv')
df.columns = ['Month', 'Ashirbad Wheat Flour Selling Price', 'Fair and Lovely Face Cream Selling Price',
              'Fortune Cooking Oil Selling Price', 'Maggi Sauce Selling Price', 'Potatoes Selling Price',
              'Sriram Papad Selling Price', 'Ashirbad Wheat Flour Sales Volume',
              'Fair and Lovely Face Cream Sales Volume', 'Fortune Cooking Oil Sales Volume',
              'Maggi Sauce Sales Volume', 'Potatoes Sales Volume', 'Sriram Papad Sales Volume',
              'Ashirbad Wheat Flour Inventory', 'Fair and Lovely Face Cream Inventory',
              'Fortune Cooking Oil Inventory', 'Maggi Sauce Inventory', 'Potatoes Inventory', 'Sriram Papad Inventory',
              'Ashirbad Wheat Flour Acquisition Cost', 'Fair and Lovely Face Cream Acquisition Cost',
              'Fortune Cooking Oil Acquisition Cost', 'Maggi Sauce Acquisition Cost', 'Potatoes Acquisition Cost',
              'Sriram Papad Acquisition Cost', 'Ashirbad Wheat Flour Revenue', 'Fair and Lovely Face Cream Revenue',
              'Fortune Cooking Oil Revenue', 'Maggi Sauce Revenue', 'Potatoes Revenue', 'Sriram Papad Revenue',
              'Ashirbad Wheat Flour Marginal Revenue', 'Fair and Lovely Face Cream Marginal Revenue',
              'Fortune Cooking Oil Marginal Revenue', 'Maggi Sauce Marginal Revenue', 'Potatoes Marginal Revenue',
              'Sriram Papad Marginal Revenue', 'Ashirbad Wheat Flour Profit', 'Fair and Lovely Face Cream Profit',
              'Fortune Cooking Oil Profit', 'Maggi Sauce Profit', 'Potatoes Profit', 'Sriram Papad Profit']
profile = ProfileReport(df)

st.write('Indraneel Dey')
st.write('21f3002696')
st.write('Indian Institute of Technology, Madras')
st.title('Profile Report of Products Data')
st.write(df)
st_profile_report(profile)
