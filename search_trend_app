import streamlit as st
import csv
from pytrends.request import TrendReq
import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np
import peakutils
from collections import Counter
import pytrends


st.title('Benvenuti nella mia fantasmagorica APP per il search trend')
st.subheader('Cosa aspetti? carica il tuo dataset di keywords')
tipo_di_trend = st.radio('Di che tipo di trend hai bisogno?', ['Giornaliero', 'Mensile'])
start_date = str(st.date_input('Start date'))
end_date = str(st.date_input('End date'))
uploaded_file = st.file_uploader(label="carica il tuo set di keywords in formato CSV", type='csv')
if uploaded_file is not None:
     st.write(type(uploaded_file))
     colnames = ["keywords"]
     df = pd.read_csv(uploaded_file, names=colnames)
     pytrend = TrendReq()
     startTime = time.time()
     pytrend = TrendReq(hl='it', tz=360)
     df2 = df["keywords"].values.tolist()
     dataset = []

     for x in range(0, len(df2)):
          keywords = [df2[x]]
          pytrend.build_payload(kw_list=keywords, cat=0, geo='IT', timeframe=start_date+' '+end_date)
          data = pytrend.interest_over_time()
          if not data.empty:
               data = data.drop(labels=['isPartial'], axis='columns')
               dataset.append(data)
     if tipo_di_trend == 'Giornaliero':
          result = pd.concat(dataset, axis=1)
          result['Date'] = result.index
          result['Date'] = pd.to_datetime(result['Date'])
          result['months'] = result['Date'].dt.month
          result2 = result.set_index('months')
          result3 = result2.reset_index().groupby('Date').mean().T
          st.download_button(label="Clicca per Scaricare", data=result3.to_csv(), file_name='text/csv',
                             key='download-csv')
     else:
          result = pd.concat(dataset, axis=1)
          result['Date'] = result.index
          result['Date'] = pd.to_datetime(result['Date'])
          result['months'] = result['Date'].dt.month
          result2 = result.set_index('months')
          result3 = result2.reset_index().groupby('months').mean().T
          st.download_button(label="Clicca per Scaricare", data=result3.to_csv(), file_name='text/csv',
                             key='download-csv')
