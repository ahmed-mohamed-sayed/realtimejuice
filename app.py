
from matplotlib.pyplot import legend
import streamlit as st 
import pandas as pd 
from streamlit_option_menu import option_menu
from streamlit_autorefresh import st_autorefresh
import streamlit.components.v1 as components
from pyecharts import options as opts
from pyecharts.charts import Funnel, Bar, Line,Pie




st.set_page_config(layout='wide'
                )
st.markdown("""
        <style>
        div[data-testid="metric-container"] {
        background-color: rgba(28, 131, 225, 0.1);
        border: 2px solid rgba(28, 131, 225, 0.1);
        padding: 5% 5% 5% 10%;
        border-radius: 5px;
        border-color: #B2182B;
        color: rgb(30, 103, 119);
        overflow-wrap: break-word;
        text-align: center;
        }
        

        /* breakline for metric text         */
        div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
        overflow-wrap: break-word;
        white-space: break-spaces;
        color: #C00000;
        font-weight: bold;
        }
        </style>
        
        """
        , unsafe_allow_html=True)
        
#===============================================================================================
#Setting project Style

with open ('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
    
#===============================================================================================
# Reading DF from google sheet
sheet_url = 'https://docs.google.com/spreadsheets/d/1BNvKxtMtoxzw22HIfxezPw9UkoRCQibKkAB5xTgpvWw/edit#gid=0'
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
# update every 5 mins
st_autorefresh(interval=10 * 60 * 1000,key=None)
@st.experimental_memo(ttl=600)
def get_data():
    df = pd.read_csv(url_1)
    return df
df = get_data()
df1 =  get_data()

#===============================================================================================
# Set Navigation Menu

with st.sidebar:
    selected = option_menu(
        menu_title = 'Report Navigation',
        options = ['Sales Report', 'Cost Report' , 'Profit Report'],
        icons=['bar-chart','coin','currency-pound'],
        menu_icon='cast',
        default_index = 0,
        styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "15px"},
                "nav-link": {
                    "font-size": "15px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#f0f0f0",
                },
                "nav-link-selected": {"background-color": '#C00000'},
            },
        )
    
#===============================================================================================
# Building Sales Report   

if selected == 'Sales Report':
    st.markdown("<h2 style='text-align: center; font-weight:bold; color: #C00000;'> Sales Report</h2> " ,unsafe_allow_html=True)
    
    
#===============================================================================================
# Building Cost Report     

if selected == 'Cost Report':
    st.markdown("<h1 style='text-align: center; font-weight:bold; color: #C00000;'> Real-time Cost Report</h1> " ,unsafe_allow_html=True)
    
    #---------------------------------------------------------------------------
    #Create Columns
    # col1, col2, col3, col4, col5 = st.columns(5)
    # with col1:
    opt1 = df["Branch"].unique().tolist()
    opt1.insert(0,'ALL')
    branch = st.multiselect("Branch",opt1, default='ALL')
    if "ALL" in branch:
        branch = opt1   
    df = df.query( 'Branch == @branch  ')
    # with col2:
    #         opt3 = df['ExpType'].unique().tolist()
    #         opt3.insert(0,'ALL')
    #         expt = st.multiselect("Exp Type",opt3, default='ALL')
    #         if "ALL" in expt:
    #             expt = opt3   
    # df = df.query('ExpType == @expt')
    # with col3:
    #         opt2 = df['ExpName'].unique().tolist()
    #         opt2.insert(0,'ALL')
    #         exp = st.multiselect("Exp Name",opt2, default='ALL')
    #         if "ALL" in exp:
    #             exp = opt2   
    # df = df.query('ExpName == @exp' )
    # with col4:
    #     start = st.selectbox("Start Month",df["MONTH"].unique())
    # df = df[df["MONTH"] >= start]
    # with col5:
    #     end = st.selectbox("End Month",df["MONTH"].unique())
    # df = df[df["MONTH"] <= end]
    #---------------------------------------------------------------------------
    #Create KPI's & Graph
    tot = df['AMOUNT'].sum() 
    avg = df['AMOUNT'].sum() / len(df['MONTH'].unique())
    typ_dis = df.groupby(['ExpType']).sum()[['AMOUNT']].reset_index()
    ad_typ = df.query('ExpType == "ADMIN"')['AMOUNT'].sum()
    cog_typ = df.query('ExpType == "COGS"')['AMOUNT'].sum()
    adv_typ = df.query('ExpType == "ADVERTISING"')['AMOUNT'].sum()
    
    
    
    kpi1, kpi2, kpi3, kpi4, kpi5= st.columns(5)
    kpi1.metric(
        label = 'Total Cost',
        value = str(round(tot/ 1e6, 2)) + " M",
    )
    kpi2.metric(
        label = 'Avg Cost Per Month',
        value = str(round(avg/ 1e3, 2)) + " K",
    )
    kpi3.metric(
        label = 'Admin Cost $',
        value = str(round(typ_dis['AMOUNT'][0]/ 1e3, 2)) + " K",
    )
    kpi4.metric(
        label = 'COGS $',
        value = str(round(typ_dis['AMOUNT'][2]/ 1e3, 2)) + " K",
    )
    kpi5.metric(
        label = 'Advertising Cost $',
        value = str(round(typ_dis['AMOUNT'][1]/ 1e3, 2)) + " K",
    )
    #------------------------------------------------------ 
    #-------- Branch_Data---------------------------------- 
    total_br = df['AMOUNT'].sum()  
    zayed_c = df.query('Branch == "ZAYED"')['AMOUNT'].sum()
    sharton_c = df.query('Branch == "SHERATON"')['AMOUNT'].sum()
    tagam_c = df.query('Branch == "TAGAMOA"')['AMOUNT'].sum()
    
    #------------Pie1_chart----------------------------
    st.markdown("<h3 style='text-align: center; font-weight:bold; color: #354968;'> Cost Distribution By Branch </h3> " ,unsafe_allow_html=True)    
    br1, br2, br3= st.columns(3)
    br1.metric(
        label = 'Zayed Cost %',
        value = str(round(zayed_c/total_br, 2)*100) + " %",
    )
    br2.metric(
        label = 'Sheraton Cost %',
        value = str(round(sharton_c/total_br, 2)*100) + " %",
    )
    br3.metric(
        label = 'Tagamoa Cost %',
        value = str(round(tagam_c/total_br, 2)*100) + " %",
    )
    #------------Pie1_chart_data----------------------------
    data_br = df.groupby(['Branch']).sum()[['AMOUNT']].reset_index()
    data_brn = data_br['Branch'].unique().tolist()
    xd = data_brn   
    yd = data_br['AMOUNT'].values.tolist()
    #------------------------------------------------------
    data_pair1 = [list(z) for z in zip(xd, yd)]
    data_pair1.sort(key=lambda x: x[1])
    pie1 = (
        Pie(init_opts=opts.InitOpts( width="1050px", height="400px",bg_color="#f0f0f0"))
    .add("", data_pair=data_pair1)
    .set_global_opts(title_opts=opts.TitleOpts(title="Total Cost by Branch"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        
    .render_embed()
    
    )
    #------------Line_chart_data----------------------------
    lin_dat = df.groupby(['Branch','MONTH']).sum()[['AMOUNT']].reset_index()
    lin_za = lin_dat.query('Branch == "ZAYED"')[['AMOUNT']]
    lin_sh = lin_dat.query('Branch == "SHERATON"')[['MONTH','AMOUNT']].sort_values(by=['MONTH'])
    lin_tag = lin_dat.query('Branch == "TAGAMOA"')[['MONTH','AMOUNT']].sort_values(by=['MONTH'])
    
    line = (
            Line(init_opts=opts.InitOpts( width="1050px", height="500px",bg_color="#f0f0f0"))
            .add_xaxis(xaxis_data=lin_dat['MONTH'])
            .add_yaxis(
                 series_name="Zayed",
                 y_axis=lin_za['AMOUNT'],
                
             )
            .add_yaxis(
                series_name="Sheraton",
                y_axis=lin_sh['AMOUNT'],
                
            )
            .add_yaxis(
                series_name="Tagamoa",
                y_axis=lin_tag['AMOUNT'],
                
            )
            
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Total Cost During Months"),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                toolbox_opts=opts.ToolboxOpts(is_show=True),
                xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
                
            )
            
            .render_embed()
)
    
    
    
    
    
    
    #with st.expander('View Visuals'):
    components.html(pie1 , width=1200, height=500)
    components.html(line , width=1200, height=500)
    #-------bar1 Chart Data---------------------------------
    cost_br = pd.pivot_table( df,columns=['ExpType'] ,index= ['Branch'] ,values='AMOUNT',aggfunc= 'sum').reset_index()
    admin_br =cost_br['ADMIN'].sum() 
    #------------------------------------------------------
    st.markdown("<h3 style='text-align: center; font-weight:bold; color: #980036;'> Cost Distribution By Cost Type </h3> " ,unsafe_allow_html=True)    
    kpi6, kpi7, kpi8= st.columns(3)
    kpi6.metric(
        label = 'Admin Cost %',
        value = str(round(ad_typ/tot, 1)*100) + " %",
    )
    kpi7.metric(
        label = 'COGS %',
        value = str(round(cog_typ/tot, 2)*100) + " %",
    )
    kpi8.metric(
        label = 'Advertising %',
        value = str(round(adv_typ/tot, 2)*100) + " %",
    )
    
    
    bar1 = (
            Bar(init_opts=opts.InitOpts(width="1000px", height="500px", bg_color="#f0f0f0"))
            .add_xaxis(cost_br['Branch'].unique().tolist())
            .add_yaxis('Total Admin',cost_br['ADMIN'].values.tolist())
            .add_yaxis('Total COGS',cost_br['COGS'].values.tolist())  
            .add_yaxis('Total ADVER',cost_br['ADVERTISING'].values.tolist()) 
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Cost By Branch"),
                legend_opts=opts.LegendOpts( pos_top="1%", pos_left="40%"),
                toolbox_opts=opts.ToolboxOpts(),
                datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")])
            .set_series_opts(
                label_opts=opts.LabelOpts(is_show=False),
                
        )
            .render_embed()
        )
    #-------Line1 Chart Data---------------------------------

    x = df.groupby(['ExpType','MONTH']).sum()[['AMOUNT']].reset_index()
    admin = x.query('ExpType == "ADMIN"')[['MONTH','AMOUNT']].sort_values(by=['MONTH'])
    cogs = x.query('ExpType == "COGS"')[['MONTH','AMOUNT']].sort_values(by=['MONTH'])
    adver = x.query('ExpType == "ADVERTISING"')[['MONTH','AMOUNT']].sort_values(by=['MONTH'])
    #------------------------------------------------------
    line1 =    (
            Line(init_opts=opts.InitOpts( width="1000px", height="500px",bg_color="#f0f0f0"))
            .add_xaxis(xaxis_data=x['MONTH'])
            .add_yaxis(
                 series_name="Admin",
                 y_axis=admin['AMOUNT'],
                
             )
            .add_yaxis(
                series_name="COGS",
                y_axis=cogs['AMOUNT'],
                
            )
            .add_yaxis(
                series_name="Advertising",
                y_axis=adver['AMOUNT'],
                
            )
            
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Cost Type During Months"),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                toolbox_opts=opts.ToolboxOpts(is_show=True),
                xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
                
            )
            
            .render_embed()
        )
    with st.expander('View Visuals'):
        components.html(bar1 , width=1000, height=500)
        components.html(line1 , width=1000, height=500)
    

    #------------------------------------------------------
    st.markdown("<h3 style='text-align: center; font-weight:bold; color: rgb(30, 103, 119)   ;'> Admin Cost Analysis </h3> " ,unsafe_allow_html=True)    

    #-------Fun1 Chart Data---------------------------------
    exp_nm = df.groupby(['ExpName','ExpType']).sum()[['AMOUNT']].sort_values(by='AMOUNT',ascending=False).reset_index()
    exp_nm= exp_nm[exp_nm['ExpType']== 'ADMIN']
    x_data = exp_nm['ExpName'].unique().tolist()   
    y_data = exp_nm['AMOUNT'].values.tolist()
    #------------------------------------------------------
    
    data = [[x_data[i], y_data[i]] for i in range(len(x_data))]

    fun1 = (
            Funnel(init_opts=opts.InitOpts(width="1050px", height="900px",bg_color="#f9f9f9"))
            .add(
                series_name="",
                data_pair=data,
                gap=3,
                tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}"),
                label_opts=opts.LabelOpts(is_show=True, position="inside"),
                itemstyle_opts=opts.ItemStyleOpts(border_color="#f0f0f0", border_width=1),
            )
            .set_global_opts(title_opts=opts.TitleOpts(title="", subtitle=""),
                             legend_opts=opts.LegendOpts( pos_top="1%"),)
            .render_embed()
        )
 
    components.html(fun1, width=1200, height=1000 )
    #------------------------------------------------------
    # col1, col2 = st.columns(2)
    # exp_nm1 = df.groupby(['ExpName','ExpType']).sum()[['AMOUNT']].sort_values(by='AMOUNT',ascending=False).reset_index()
    # exp_nm1= exp_nm1[exp_nm1['ExpType']== 'COGS']
    # x1_data = exp_nm1['ExpName'].unique().tolist()   
    # y1_data = exp_nm1['AMOUNT'].values.tolist()
    # data_pair = [list(z) for z in zip(x1_data, y1_data)]
    # data_pair.sort(key=lambda x: x[1])
        
    # pie2 = (
    #     Pie(init_opts=opts.InitOpts( width="450px", height="400px",bg_color="#f0f0f0"))
    # .add("", data_pair=data_pair)
    # .set_global_opts(title_opts=opts.TitleOpts(title="New Reg"))
    # .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        
    #     .render_embed()
    
    # )
    # with col1:
    #     components.html(pie2 , width=1000, height=500)
    
    
    #View Data
    expander = st.expander('View Data')
    expander.dataframe(df.style)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    
#===============================================================================================
# Building Profit Report  
if selected == 'Profit Report':
    st.markdown("<h2 style='text-align: center; font-weight:bold; color: #C00000;'> Profit Report</h2> " ,unsafe_allow_html=True)