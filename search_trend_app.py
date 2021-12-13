import streamlit as st
from pytrends.request import TrendReq
import pandas as pd
import time
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import pytrends


st.title('Benvenuti nella mia fantasmagorica APP per il search trend')
st.write("by [Alessandro Storari](https://www.linkedin.com/in/alessandro-storari/)")
st.subheader('Cosa aspetti? carica il tuo dataset di keywords')
tipo_di_trend = st.radio('Di che tipo di trend hai bisogno?', ['Giornaliero', 'Mensile'])
Countries = st.selectbox('Seleziona un paese',['Italia', 'Francia', 'Stati Uniti', 'Inghilterra', 'Spagna', 'Germania'])
st.title('ATTENZIONE')
st.subheader("Non prendete i dati dell'ultimo mese disponibile in quanto non potrebbero ancora essere disponibili")
st.subheader("Per vedere fino a che giorno sono disponibili i dati sul trend vai su [Google trend](https://trends.google.it/trends/?geo=IT)")
start_date = str(st.date_input('Start date'))
end_date = str(st.date_input('End date'))
st.subheader("ESEMPIO DI FILE CSV DA CARICARE")
image = Image.open('![image](https://user-images.githubusercontent.com/66023657/145842285-308d18f7-956a-4b9f-95ac-e4df69f7f9a7.png')
st.image(image, caption='Esempio di file CSV da caricare')
uploaded_file = st.file_uploader(label="carica il tuo set di keywords in formato CSV", type='csv')
if uploaded_file is not None:
     st.write(type(uploaded_file))
     colnames = ["keywords"]
     df = pd.read_csv(uploaded_file, names=colnames)
     pytrend = TrendReq()
     startTime = time.time()
     df2 = df["keywords"].values.tolist()
     dataset = []

     for x in range(0, len(df2)):
          keywords = [df2[x]]
          if Countries is 'Italia':
               pytrend.build_payload(kw_list=keywords, cat=0, geo='IT', timeframe=start_date + ' ' + end_date)
          elif Countries is 'Francia':
               pytrend.build_payload(kw_list=keywords, cat=0, geo='FR', timeframe=start_date + ' ' + end_date)
          elif Countries is 'Stati Uniti':
               pytrend.build_payload(kw_list=keywords, cat=0, geo='US', timeframe=start_date + ' ' + end_date)
          elif Countries is 'Inghilterra':
               pytrend.build_payload(kw_list=keywords, cat=0, geo='GB', timeframe=start_date + ' ' + end_date)
          elif Countries is 'Spagna':
               pytrend.build_payload(kw_list=keywords, cat=0, geo='ES', timeframe=start_date + ' ' + end_date)
          elif Countries is 'Germania':
               pytrend.build_payload(kw_list=keywords, cat=0, geo='DE', timeframe=start_date + ' ' + end_date)
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
st.subheader('La mia app ti è stata utile?')
bottone_si=st.button('Si, molto!')
bottono_no=st.button('No, potevi fare di meglio')
if bottone_si:
     st.balloons()
     st.subheader("Grande! Per altre news e info sulla SEO [seguimi su Linkedin](https://www.linkedin.com/in/alessandro-storari/)")
elif bottono_no:
     st.subheader("Hai idee su come migliorare l'app? Mandami il tuo feedback [QUI](https://www.linkedin.com/in/alessandro-storari/)")
