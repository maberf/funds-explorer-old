# MAIN
#
# # Code to connect Jupyter Notebook in Google Colab
# from google.colab import drive
# drive.mount('/content/drive')
#
# import sys
# # Create a folder named src and put the modules webtableparser
# # and fundsexplorer into it
# sys.path.append('/content/drive/My Drive/\
# ColabNotemodules/funds-explorer-filter')
# # To check the modules are being reacheble by this code (linux command)
# # !ls /content/drive/My\ Drive/ColabNotemodules/funds-explorer-filter/src
#
# packages: urllib, beatiful soup, html5, pandas, plotly, jupyter lab
#
from src.webtableparser import WebTableParser
from src.fundsexplorer import processFE_df
import plotly.offline as py
import plotly.graph_objs as go
from datetime import datetime
from pytz import timezone
#
# running time reading
# running time reading
dt = datetime.now()
tz = timezone('America/Sao_Paulo')
dt_sp = dt.astimezone(tz)
date_time_sp = dt_sp.strftime('%d/%m/%Y %H:%M')
# site capture and parsing
site = WebTableParser()
site.create('https://www.fundsexplorer.com.br/ranking',
            'id', 'table-ranking')
table = site.capture()
df = site.parse(table)
#
# real state fund varible, df processing to make analysis feasible (filters)
rsf = processFE_df(df)
# real state funds (rsf) dataframe manipulation
# specific assets choosen by user in my_rsf - change the asset in the code
my_rsf = rsf.loc[(rsf['codigo'] == 'HGRU11') | (rsf['codigo'] == 'XPLG11') |
                 (rsf['codigo'] == 'VISC11') | (rsf['codigo'] == 'SADI11') |
                 (rsf['codigo'] == 'HFOF11')]
#
# real state funds (rsf) dataframe in general being filtered by criteria
rsf = rsf.loc[rsf['dy12macum%'] >= 4.00]  # 1st filter DY > 4%
rsf = rsf.sort_values(by='dy12macum%',  ascending=False)
rsf = rsf.loc[rsf['patrliqR$'] >= 500000000.00]  # 2nd filter > BRL 500 M
rsf = rsf.loc[rsf['liqdiariaNeg'] >= 1000]  # 3rd filter tradings >= 1000/day
rsf = rsf.loc[rsf['p/vpaN'] <= 1.25]  # 4th filter P/VPA <= 1.25
# splitting into two new variables: brick and paper funds
rsf_brick = rsf.loc[rsf['qtdativosN'] >= 10]  # 5th filter >= 10 assets
rsf_paper = rsf.loc[rsf['qtdativosN'] == 0]  # 5 th filter = 0 assets
#
# pd.options.plotting.backend="plotly"
py.init_notebook_mode(connected=True)
#
# BAR CHARTS - YOU SHOULD TO COMMENT ONE TO GET ANOTHER
# bar chart 0 - my funds
x0 = [my_rsf['setor'], my_rsf['codigo']]
trace00 = go.Bar(x=x0, y=my_rsf['dy12macum%'],
                 name='DY% Ano', marker_color='rgb(36, 124, 220)')
trace01 = go.Bar(x=x0, y=my_rsf['p/vpaN'],
                 name='P/VPA', marker_color='rgb(85, 171, 124)')
trace02 = go.Bar(x=x0, y=my_rsf['vacfisica%'],
                 name='%Vacância Física', marker_color='rgb(213, 83, 43)')
data0 = [trace00, trace01, trace02]
fig0 = go.Figure(data0)
fig0.update_layout(title='MEUS FIIs | DY Acum Ano, P/VPA, Vacância Física')
fig0.show()
py.plot(fig0)
print(date_time_sp)
#
# bar chart 1 - brick funds
'''x1 = [rsf_brick['setor'], rsf_brick['codigo']]
trace10 = go.Bar(x=x1, y=rsf_brick['dy12macum%'],
                 name='DY% Ano', marker_color='rgb(36, 124, 220)')
trace11 = go.Bar(x=x1, y=rsf_brick['p/vpaN'],
                 name='P/VPA', marker_color='rgb(85, 171, 124)')
trace12 = go.Bar(x=x1, y=rsf_brick['vacfisica%'],
                 name='%Vacância Física', marker_color='rgb(213, 83, 43)')
data1 = [trace10, trace11, trace12]
fig1 = go.Figure(data1)
fig1.update_layout(title='ANÁLISE FIIs TIJOLOS | DY Ano >= 4%, Patr. > 500M, \
Neg/dia > 1000, P/VPA =< 1.25, Ativos >= 10, Vacância Física < 15%')
fig1.show()
py.plot(fig1)
print(date_time_sp)'''
#
# bar chart 2 - paper funds
'''x2 = [rsf_paper['setor'], rsf_paper['codigo']]
trace20 = go.Bar(x=x2, y=rsf_paper['dy12macum%'], name='DY% Ano',
                 marker_color='rgb(36, 124, 220)')
trace21 = go.Bar(x=x2, y=rsf_paper['p/vpaN'], name='P/VPA',
                 marker_color='rgb(85, 171, 124)')
trace22 = go.Bar(x=x2, y=rsf_paper['varpatr%'], name='%Var. Patr. Acum',
                 marker_color='rgb(213, 83, 43)')
data2 = [trace20, trace21, trace22]
fig2 = go.Figure(data2)
fig2.update_layout(title='ANÁLISE FIIs PAPEL | DY Ano >= 4%, Patr. > 500M, \
Neg/dia > 1000, P/VPA =< 1.25')
fig2.show()
py.plot(fig2)
print(date_time_sp)'''
#
