

import streamlit as st 
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
import pandas as pd 
from streamlit_option_menu import option_menu
from streamlit_autorefresh import st_autorefresh
import streamlit.components.v1 as components
from pyecharts import options as opts
from streamlit_echarts import st_pyecharts
from pyecharts.charts import Bar, Line,Pie
from streamlit_lottie import st_lottie
import json





# set app layout 
st.set_page_config(layout='wide'
                )
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)
# def local_style(file_name):
#         with open(file_name) as f:
#             st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
# local_style(".streamlit/config.toml")


#===============================================================================================

# Set Navigation Menu

with st.sidebar:
    selected = option_menu(
        menu_title = 'Report Navigation',
        options = ['Home','Sales Report', 'Cost Report' , 'Profit Report'],
        icons=['house','bar-chart','coin','currency-pound'],
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
# Building Home
if selected == 'Home':
    st.markdown("<h1 style='text-align: center; font-weight:bold; color: #C00000;'> Real-time Report (Sales - Cost - Profit)</h1> " ,unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; font-weight:bold; color: #354968;'> Milk Shake & Juice Shop</h3> " ,unsafe_allow_html=True)
    #bold line separator:
    st.markdown("""<hr style="height:2x;border:none;color:#C00000;background-color:#C00000;" /> """, unsafe_allow_html=True)
    
    #function to read animation from json file 
    def load_lottiefile(filepath: str):
        with open (filepath,"r") as f:
            return json.load(f)
        
    lottie_coding = load_lottiefile('dashboard.json')
    st_lottie(
        lottie_coding,
        speed=1,
        height= 800
       
    )
    st.markdown("<h4 style='text-align: center; font-weight:bold; color: #354968;'> This report gets data from Google Sheets with auto-update & auto-refresh time of 10 min. Although this report is responsive. But it's preferable to open from a laptop/desktop.   </h4> " ,unsafe_allow_html=True)

    #bold line separator:
    st.markdown("""<hr style="height:4px;border:none;color:#C00000;background-color:#C00000;" /> """, unsafe_allow_html=True)
    #lottie files
    lt1, lt2, lt3 = st.columns(3)
    lottie_coding1 = load_lottiefile('sales.json')
    lottie_coding2 = load_lottiefile('cost.json')
    lottie_coding3 = load_lottiefile('profit.json')
    with lt1:    
        
        st_lottie(
            lottie_coding1,
            speed=1,
            height = 200,  
        )
        st.markdown("<h3 style='text-align: center; font-weight:bold; color: #C00000;'> Sales Report Metrics</h3> " ,unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; font-weight:bold; color: #354968;'> - Total Sales (All or By Branch)</h6> " ,unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; font-weight:bold; color: #354968;'> - Average Sales Per Month (All or By Branch)</h6> " ,unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; font-weight:bold; color: #354968;'> - No. Of Orders (All or By Branch)</h6> " ,unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; font-weight:bold; color: #354968;'> - Average Order Value (All or By Branch)</h6> " ,unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; font-weight:bold; color: #354968;'> - Average No. Of Orders Per Month (All or By Branch)</h6> " ,unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; font-weight:bold; color: #354968;'> - Cash Sales VS On Acc Sales (All or By Branch)</h6> " ,unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; font-weight:bold; color: #354968;'> - Take Away VS Delivery Sales (All or By Branch)</h6> " ,unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; font-weight:bold; color: #354968;'> - Sales By Day Of Week (All or By Branch)</h6> " ,unsafe_allow_html=True)






    with lt2:    
        st_lottie(
            lottie_coding2,
            speed=1,
            height = 200,  
        )
        st.markdown("<h3 style='text-align: center; font-weight:bold; color: #C00000;'> Cost Report Metrics</h3> " ,unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; font-weight:bold; color: #354968;'> - Total Cost (All or By Branch)</h6> " ,unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; font-weight:bold; color: #354968;'> - Average Cost Per Month (All or By Branch)</h6> " ,unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; font-weight:bold; color: #354968;'> - Cost Distribution By Cost Type: Admin, Cogs & Advertising    (All or By Branch)</h6> " ,unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; font-weight:bold; color: #354968;'> - Cost Analysis for Admin, Cogs  (All or By Branch)</h6> " ,unsafe_allow_html=True)

    with lt3:    
        st_lottie(
            lottie_coding3,
            speed=1,
            height = 200,  
        )
        st.markdown("<h3 style='text-align: center; font-weight:bold; color: #C00000;'> Profit Report Metrics</h3> " ,unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; font-weight:bold; color: #354968;'> - Net Profit (All or By Branch)</h6> " ,unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; font-weight:bold; color: #354968;'> - Average Profit Per Month (All or By Branch)</h6> " ,unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; font-weight:bold; color: #354968;'> - Cost to Profit Ratio%(All or By Branch)</h6> " ,unsafe_allow_html=True)
    #bold line separator:
    st.markdown("""<hr style="height:4px;border:none;color:#C00000;background-color:#C00000;" /> """, unsafe_allow_html=True)
    #Contact Form
    st.header(":mailbox: Get In Touch With Me!")
    contact_form = ('''<form action="https://formsubmit.co/ahmed.sayed.ams@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Your Name" required>
     <input type="email" name="email" placeholder = "Your Email"  required>
     <textarea name="message" placeholder="Your Message Here"></textarea>
     <button type="submit">Send</button>
    </form>''')    
    st.markdown(contact_form,unsafe_allow_html=True)
    
    #Use local css file
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
    local_css("style/style.css")
    #Use local style file
    
    
#===============================================================================================
# Building Sales Report   

if selected == 'Sales Report':
    #------Set cards style------------------
    st.markdown("""
        <style>
        div[data-testid="metric-container"] {
        background-color: rgba(28, 131, 225, 0.1);
        border: 2px solid rgba(28, 131, 225, 0.1);
        padding: 5% 5% 5% 10%;
        border-radius: 10px;
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
        font-size:17px;
        }
        </style>
        
        """
        , unsafe_allow_html=True)
    #----------------------------------------
    # Reading Sales DF from google sheet
    sheet_id = '1BNvKxtMtoxzw22HIfxezPw9UkoRCQibKkAB5xTgpvWw'
    sheet_name = 'SALES'
    url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
    # update every 10 mins
    st_autorefresh(interval=2* 60 * 1000,key=None)
    @st.experimental_memo(ttl=120)
    def get_sales_data():
        df = pd.read_csv(url)
        return df
    df1 = get_sales_data()
    df2= get_sales_data()
    df3= get_sales_data()
#===============================================================================================
    #main title
    st.markdown("<h1 style='text-align: center; font-weight:bold; color: #C00000;'> Real-time Sales Report</h1> " ,unsafe_allow_html=True)
    #bold line separator
    st.markdown("""<hr style="height:4px;border:none;color:#C00000;background-color:#C00000;" /> """, unsafe_allow_html=True)
    # title
    st.markdown("<h2 style='text-align: center; font-weight:bold; color: #354968;'> General Sales Insights</h2> " ,unsafe_allow_html=True)    

    # Radio Buttons style
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;border:2px solid #C00000;border-radius:10px} </style>', unsafe_allow_html=True)
    st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;font-size:19px;color:#B45904;}</style>', unsafe_allow_html=True)
    #----Multiselect----------------------------------
    choose=st.radio("",("All","Zayed","Sheraton","Tagamoa"))
    if choose == 'Zayed':
      df1=  df1.query('Branch == "ZAYED"')
    if choose == 'Sheraton':
      df1=  df1.query('Branch == "SHERATON"')
    if choose == 'Tagamoa':
      df1=  df1.query('Branch == "TAGAMOA"')
    st.markdown("")
    st.markdown("")
    #-------------------------------------------------
    #Total Sales KPI's--------------------------------
    tot_s = df1['TOTAL'].sum()
    tot_or = df1['NO_OREDRS'].sum()
    avg_s = tot_s  / len(df1['MONTH'].unique())
    avg_or = tot_or  / len(df1['MONTH'].unique())
    
    t1,t2, t3, t4, t5 = st.columns(5)
    t1.metric(
        label = 'Total Sales',
        value = str(round(tot_s/ 1e6, 2)) + " M",
    )
    t2.metric(
        label = 'Avg Sales Per Month',
        value = str(round(avg_s/ 1e3, 2)) + " K",
    )
    t3.metric(
        label = 'Total Orders',
        value = tot_or,
    )
    t4.metric(
        label = 'Avg Orders/Month',
        value = round(avg_or),
    )
    t5.metric(
        label = 'Avg Order Value',
        value = round(tot_s/tot_or),
    )
        
    #-------- Branch_Data----------------------------------  
    zayed_s = df1.query('Branch == "ZAYED"')['TOTAL'].sum()
    sharton_s = df1.query('Branch == "SHERATON"')['TOTAL'].sum()
    tagam_s = df1.query('Branch == "TAGAMOA"')['TOTAL'].sum()
    
    #------------Branch_metrics----------------------------
    st.markdown("<h3 style='text-align: center; font-weight:bold; color: #354968;'> Total Sales  By Branch </h3> " ,unsafe_allow_html=True)    
    b1, b2, b3= st.columns(3)
    b1.metric(
        label = 'Zayed Sales %',
        value = str(round(zayed_s/tot_s, 2)*100) + " %",
    )
    b2.metric(
        label = 'Sheraton Sales %',
        value = str(round(sharton_s/tot_s, 2)*100) + " %",
    )
    b3.metric(
        label = 'Tagamoa Sales %',
        value = str(round(tagam_s/tot_s, 2)*100) + " %",
    )
    #------------Pie1_chart_data----------------------------
    sal_br = df1.groupby(['Branch']).sum()[['TOTAL']].reset_index()
    sal_brn = sal_br['Branch'].unique().tolist()
    xs = sal_brn   
    ys = sal_br['TOTAL'].values.tolist()
    #------------------------------------------------------
    data_pairs = [list(z) for z in zip(xs, ys)]
    data_pairs.sort(key=lambda x: x[1])
    pie = (
        Pie(init_opts=opts.InitOpts( bg_color="#f0f0f0"))
    .add("", data_pair=data_pairs)
    .set_global_opts(title_opts=opts.TitleOpts(title=""))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        
    
    
    )
    #------------Line_chart_data----------------------------
    lin_s = df1.groupby(['Branch','MONTH']).sum()[['TOTAL']].reset_index()
    lin_sz = lin_s.query('Branch == "ZAYED"')[['TOTAL']]
    lin_ssh = lin_s.query('Branch == "SHERATON"')[['MONTH','TOTAL']].sort_values(by=['MONTH'])
    lin_stag = lin_s.query('Branch == "TAGAMOA"')[['MONTH','TOTAL']].sort_values(by=['MONTH'])
    #colors = ["#5793f3", "#d14a61", "#675bba"]
    line = (
            Line(init_opts=opts.InitOpts( bg_color="#f0f0f0"))
            .add_xaxis(xaxis_data=lin_s['MONTH'])
            .add_yaxis(
                 series_name="Zayed",
                 y_axis=lin_sz['TOTAL'],
                 #color=colors[0]
                
             )
            .add_yaxis(
                series_name="Sheraton",
                y_axis=lin_ssh['TOTAL'],
                
            )
            .add_yaxis(
                series_name="Tagamoa",
                y_axis=lin_stag['TOTAL'],
                
            )
            
            .set_global_opts(
                title_opts=opts.TitleOpts(title=""),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                toolbox_opts=opts.ToolboxOpts(is_show=True),
                xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
                datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")]
                
            )
            
            
            
        )
    
    with st.expander('View Visuals'):   
        l1,l2 = st.columns(2)
        with l1:
            st.markdown("<h5 style='text-align: center; font-weight:bold; color: #B45904;'> Total Sales by Branch </h5> " ,unsafe_allow_html=True)   
            st_pyecharts(pie,height=350)
        with l2:
            st.markdown("<h5 style='text-align: center; font-weight:bold; color: #B45904;'> Total Sales During Months </h5> " ,unsafe_allow_html=True)   
            st_pyecharts(line,height=350)
    #--------------------------------------------------------------
    
    
    #------------set radio buttons for branches  ----------------------------
    #Bold Line separatoer
    st.markdown("""<hr style="height:4px;border:none;color:#C00000;background-color:#C00000;" /> """, unsafe_allow_html=True)
    #Title
    st.markdown("<h3 style='text-align: center; font-weight:bold; color: #354968;'> (Cash VS On Acc) & (T.away VS On Delivery)</h3> " ,unsafe_allow_html=True)
    
   
    choose=st.radio("",("ALL","Zayed","Sheraton","Tagamoa"))
    if choose == 'Zayed':
      df2=  df2.query('Branch == "ZAYED"')
    if choose == 'Sheraton':
      df2=  df2.query('Branch == "SHERATON"')
    if choose == 'Tagamoa':
      df2=  df2.query('Branch == "TAGAMOA"')
    st.markdown("")
    st.markdown("")
    #-------- cash_vs_on_acc_Data----------------------------------  
    cash_s = df2['CASH'].sum()
    onacc_s = df2['ON_ACC'].sum()
    tawa_s = df2['T_AWAY'].sum()
    del_s = df2['DELIVERY'].sum()
    tot_s1 = df2['TOTAL'].sum()    
    
    
    
    sl1, sl2, sl3, sl4 = st.columns(4)
    sl1.metric(
        label='Cash Sales %',
        value= str(round(cash_s / tot_s1,2)*100) + " %"
    )
    sl2.metric(
        label='On Acc Sales %',
        value= str(round(onacc_s / tot_s1,2)*100) + " %"
    )
    sl3.metric(
        label='Take Away Sales %',
        value= str(round(tawa_s / tot_s1,2)*100) + " %"
    )
    sl4.metric(
        label='Delivery Sales %',
        value= str(round(del_s / tot_s1,2)*100) + " %"
    ) 
    #------------Pie2_chart_data----------------------------
    sal_br1 = df2.groupby(['Branch']).sum()[['CASH','ON_ACC']].reset_index()
    sal_br2 = df2.groupby(['Branch']).sum()[['T_AWAY','DELIVERY']].reset_index()
    xs1 = ['CASH', 'ON_ACC'] 
    xs2 = ['T_Away', 'Delivery']  
    ys1 = sal_br1[['CASH','ON_ACC']].sum()
    ys2 = sal_br2[['T_AWAY','DELIVERY']].sum()
    #------------------------------------------------------
    data_pairs1 = [list(z) for z in zip(xs1, ys1)]
    data_pairs1.sort(key=lambda x: x[1])
    pie1 = (
        Pie(init_opts=opts.InitOpts( bg_color="#f0f0f0"))
    .add("", data_pair=data_pairs1)
    .set_global_opts(title_opts=opts.TitleOpts(title=""))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        
    
    
    )
    
    data_pairs2 = [list(z) for z in zip(xs2, ys2)]
    data_pairs2.sort(key=lambda x: x[1])
    pie2 = (
        Pie(init_opts=opts.InitOpts( bg_color="#f0f0f0"))
    .add("", data_pair=data_pairs2)
    .set_global_opts(title_opts=opts.TitleOpts(title=""))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        
    
    
    )  
    
    #------------Line_chart_data----------------------------
    lin_ca_on = df2.groupby(['MONTH']).sum()[['CASH','ON_ACC']].reset_index()
    lin_tk_dv = df2.groupby(['MONTH']).sum()[['T_AWAY','DELIVERY']].reset_index()
    
    line1 = (
            Line(init_opts=opts.InitOpts( bg_color="#f0f0f0"))
            .add_xaxis(xaxis_data=lin_ca_on['MONTH'])
            .add_yaxis(
                 series_name="ON_ACC",
                 y_axis=lin_ca_on['ON_ACC'],
             )
            .add_yaxis(
                series_name="Cash",
                y_axis=lin_ca_on['CASH'],
                
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title=""),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                toolbox_opts=opts.ToolboxOpts(is_show=True),
                xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
                datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")] 
            )
            
        )
    line2 = (
            Line(init_opts=opts.InitOpts( bg_color="#f0f0f0"))
            .add_xaxis(xaxis_data=lin_tk_dv['MONTH'])
            .add_yaxis(
                 series_name="Delivery",
                 y_axis=lin_tk_dv['DELIVERY'],
             )
            .add_yaxis(
                series_name="T_Away",
                y_axis=lin_tk_dv['T_AWAY'],
                
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title=""),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                toolbox_opts=opts.ToolboxOpts(is_show=True),
                xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
                datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")] 
            )
            
        )
    with st.expander('View Visuals'):   
        m1,m2 = st.columns(2) 
        with m1:
            st.markdown("<h5 style='text-align: center; font-weight:bold; color: #B45904;'>Cash & On Acc Sales</h5> " ,unsafe_allow_html=True)   
            st_pyecharts(pie1,height=350)  
        with m2:
            st.markdown("<h5 style='text-align: center; font-weight:bold; color: #B45904;'>T.Away & Delivery Sales</h5> " ,unsafe_allow_html=True)   
            st_pyecharts(pie2,height=350)
        m3,m4 = st.columns(2)
        with m3:
            st.markdown("<h5 style='text-align: center; font-weight:bold; color: #B45904;'>Cash & On Acc Sales During Months</h5> " ,unsafe_allow_html=True)   
            st_pyecharts(line1,height=350)
        with m4:
            st.markdown("<h5 style='text-align: center; font-weight:bold; color: #B45904;'>T.Away & Delivery Sales During Months</h5> " ,unsafe_allow_html=True)   
            st_pyecharts(line2,height=350)
    #------------set radio buttons for Dayweek  ----------------------------
    #bold line separator
    st.markdown("""<hr style="height:4px;border:none;color:#C00000;background-color:#C00000;" /> """, unsafe_allow_html=True)
    #title
    st.markdown("<h3 style='text-align: center; font-weight:bold; color: #354968;'> Sales By Day of Week (Total, T.Away & Delivery)</h3> " ,unsafe_allow_html=True)


   
    choose=st.radio(".",("ALL","Zayed","Sheraton","Tagamoa"))
    if choose == 'Zayed':
      df3=  df3.query('Branch == "ZAYED"')
    if choose == 'Sheraton':
      df3=  df3.query('Branch == "SHERATON"')
    if choose == 'Tagamoa':
      df3=  df3.query('Branch == "TAGAMOA"')
    st.markdown("")
    st.markdown("")
    #------------Weekday Data & Visual----------------------------
    day = df3['DAY'].unique().tolist()
    tot_day = df3['TOTAL'].values.tolist()
    tawy_day = df3['T_AWAY'].values.tolist()
    del_day = df3['DELIVERY'].values.tolist()
    bar = (
    Bar(init_opts=opts.InitOpts( bg_color="#f0f0f0"))
        .add_xaxis(day)
        .add_yaxis("Total", tot_day)
        .add_yaxis("T_Away", tawy_day)
        .add_yaxis("Delivery", del_day)
        .set_global_opts(
            title_opts=opts.TitleOpts(title=""),
            datazoom_opts=opts.DataZoomOpts(type_="inside"),
        )
        
)   
    #st.markdown("<h5 style='text-align: center; font-weight:bold; color: #B45904;'>Day Of Week Sales</h5> " ,unsafe_allow_html=True)   

    st_pyecharts(bar,height=450)
#===============================================================================================
# Building Cost Report     

if selected == 'Cost Report':
    #------Set cards style------------------
    st.markdown("""
        <style>
        div[data-testid="metric-container"] {
        background-color: #FFEBF1;
        border: 2px solid rgba(28, 131, 225, 0.1);
        padding: 5% 5% 5% 10%;
        border-radius: 10px;
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
        font-size:17px;
        }
        </style>
        
        """
        , unsafe_allow_html=True)
    #----------------------------------------
    # Reading COST DF from google sheet
    sheet_id = '1BNvKxtMtoxzw22HIfxezPw9UkoRCQibKkAB5xTgpvWw'
    sheet_name = 'COST'
    url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
    # update every 10 mins
    st_autorefresh(interval=10* 60 * 1000,key=None)
    @st.experimental_memo(ttl=600)
    def get_cost_data():
        df = pd.read_csv(url)
        return df
    df4 = get_cost_data()
    df5= get_cost_data()
    df6= get_cost_data()


#===============================================================================================
    st.markdown("<h1 style='text-align: center; font-weight:bold; color: #C00000;'> Real-time Cost Report</h1> " ,unsafe_allow_html=True)
    
    #---------------------------------------------------------------------------
    #bold line separator
    st.markdown("""<hr style="height:4px;border:none;color:#C00000;background-color:#C00000;" /> """, unsafe_allow_html=True)
    # title
    st.markdown("<h2 style='text-align: center; font-weight:bold; color: #354968;'> General Cost Insights</h2> " ,unsafe_allow_html=True)    

    # Radio Buttons style
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;border:2px solid #C00000;border-radius:10px} </style>', unsafe_allow_html=True)
    st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;font-size:19px;color:#C00000;}</style>', unsafe_allow_html=True)
    #----Multiselect----------------------------------
    choose=st.radio("",("All","Zayed","Sheraton","Tagamoa"))
    if choose == 'Zayed':
      df4=  df4.query('Branch == "ZAYED"')
    if choose == 'Sheraton':
      df4=  df4.query('Branch == "SHERATON"')
    if choose == 'Tagamoa':
      df4=  df4.query('Branch == "TAGAMOA"')
    st.markdown("")
    st.markdown("")
    #-------------------------------------------------
    #---------------------------------------------------------------------------
    #Create KPI's & Graph
    tot = df4['AMOUNT'].sum() 
    avg = df4['AMOUNT'].sum() / len(df4['MONTH'].unique())
    typ_dis = df4.groupby(['ExpType']).sum()[['AMOUNT']].reset_index()
    ad_typ = df4.query('ExpType == "ADMIN"')['AMOUNT'].sum()
    cog_typ = df4.query('ExpType == "COGS"')['AMOUNT'].sum()
    adv_typ = df4.query('ExpType == "ADVERTISING"')['AMOUNT'].sum()
    
    
    
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
    total_br = df4['AMOUNT'].sum()  
    zayed_c = df4.query('Branch == "ZAYED"')['AMOUNT'].sum()
    sharton_c = df4.query('Branch == "SHERATON"')['AMOUNT'].sum()
    tagam_c = df4.query('Branch == "TAGAMOA"')['AMOUNT'].sum()
    
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
    data_br = df4.groupby(['Branch']).sum()[['AMOUNT']].reset_index()
    data_brn = data_br['Branch'].unique().tolist()
    xd = data_brn   
    yd = data_br['AMOUNT'].values.tolist()
    #------------------------------------------------------
    data_pair1 = [list(z) for z in zip(xd, yd)]
    data_pair1.sort(key=lambda x: x[1])
    pie = (
        Pie(init_opts=opts.InitOpts( bg_color="#f0f0f0"))
    .add("", data_pair=data_pair1)
    .set_global_opts(title_opts=opts.TitleOpts(title=""))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        
    
    
    )
    #------------Line_chart_data----------------------------
    lin_dat = df4.groupby(['Branch','MONTH']).sum()[['AMOUNT']].reset_index()
    lin_za = lin_dat.query('Branch == "ZAYED"')[['AMOUNT']]
    lin_sh = lin_dat.query('Branch == "SHERATON"')[['MONTH','AMOUNT']].sort_values(by=['MONTH'])
    lin_tag = lin_dat.query('Branch == "TAGAMOA"')[['MONTH','AMOUNT']].sort_values(by=['MONTH'])
    
    line = (
            Line(init_opts=opts.InitOpts(bg_color="#f0f0f0"))
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
                title_opts=opts.TitleOpts(title=""),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                toolbox_opts=opts.ToolboxOpts(is_show=True),
                xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
                datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")]
                
            )
            
            
)
    with st.expander('View Visuals'):   
        l1,l2 = st.columns(2)
        with l1:
            st.markdown("<h5 style='text-align: center; font-weight:bold; color: #009862;'> Total Cost by Branch </h5> " ,unsafe_allow_html=True)   
            st_pyecharts(pie,height=350)
        with l2:
            st.markdown("<h5 style='text-align: center; font-weight:bold; color: #009862;'> Total Cost During Months </h5> " ,unsafe_allow_html=True)   
            st_pyecharts(line,height=350)
    
    #------------------------------------------------------
    #bold line separator
    st.markdown("""<hr style="height:4px;border:none;color:#C00000;background-color:#C00000;" /> """, unsafe_allow_html=True)
    #title
    st.markdown("<h3 style='text-align: center; font-weight:bold; color: #354968;'> Cost Distribution By Cost Type </h3> " ,unsafe_allow_html=True) 
    # Radio Buttons style
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;border:2px solid #C00000;border-radius:10px} </style>', unsafe_allow_html=True)
    st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;font-size:19px;color:#C00000;}</style>', unsafe_allow_html=True)
    #----Multiselect----------------------------------
    choose=st.radio("",("ALL","Zayed","Sheraton","Tagamoa"))
    if choose == 'Zayed':
      df5=  df5.query('Branch == "ZAYED"')
    if choose == 'Sheraton':
      df5=  df5.query('Branch == "SHERATON"')
    if choose == 'Tagamoa':
      df5=  df5.query('Branch == "TAGAMOA"')
    st.markdown("")
    st.markdown("")
    #------------------------------------------------- 
      #Create KPI's & Graph
    tot1 = df5['AMOUNT'].sum() 
    ad_typ1 = df5.query('ExpType == "ADMIN"')['AMOUNT'].sum()
    cog_typ1 = df5.query('ExpType == "COGS"')['AMOUNT'].sum()
    adv_typ1 = df5.query('ExpType == "ADVERTISING"')['AMOUNT'].sum()
    #--------------------------------------------------  
    kpi6, kpi7, kpi8= st.columns(3)
    kpi6.metric(
        label = 'Admin Cost %',
        value = str(round(ad_typ1/tot1,2)*100) + " %",
    )
    kpi7.metric(
        label = 'COGS %',
        value = str(round(cog_typ1/tot1, 2)*100) + " %",
    )
    kpi8.metric(
        label = 'Advertising %',
        value = str(round(adv_typ1/tot1, 2)*100) + " %",
    )
    #-------bar1 Chart Data---------------------------------
    cost_br = pd.pivot_table( df5,columns=['ExpType'] ,index= ['Branch'] ,values='AMOUNT',aggfunc= 'sum').reset_index()
    admin_br =cost_br['ADMIN'].sum() 
    
    bar1 = (
            Bar(init_opts=opts.InitOpts( bg_color="#f0f0f0"))
            .add_xaxis(cost_br['Branch'].unique().tolist())
            .add_yaxis('Total Admin',cost_br['ADMIN'].values.tolist())
            .add_yaxis('Total COGS',cost_br['COGS'].values.tolist())  
            .add_yaxis('Total ADVER',cost_br['ADVERTISING'].values.tolist()) 
            .set_global_opts(
                title_opts=opts.TitleOpts(title=""),
                legend_opts=opts.LegendOpts( pos_top="1%", pos_left="40%"),
                toolbox_opts=opts.ToolboxOpts(),
                datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")])
            .set_series_opts(
                label_opts=opts.LabelOpts(is_show=False),
                
        )
            
        )
    #-------Line1 Chart Data---------------------------------

    x = df5.groupby(['ExpType','MONTH']).sum()[['AMOUNT']].reset_index()
    admin = x.query('ExpType == "ADMIN"')[['MONTH','AMOUNT']].sort_values(by=['MONTH'])
    cogs = x.query('ExpType == "COGS"')[['MONTH','AMOUNT']].sort_values(by=['MONTH'])
    adver = x.query('ExpType == "ADVERTISING"')[['MONTH','AMOUNT']].sort_values(by=['MONTH'])
    #------------------------------------------------------
    line1 =    (
            Line(init_opts=opts.InitOpts( bg_color="#f0f0f0"))
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
                title_opts=opts.TitleOpts(title=""),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                toolbox_opts=opts.ToolboxOpts(is_show=True),
                xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
                datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")]
                
            )
            
            
        )
    with st.expander('View Visuals'):
        m1, m2 = st.columns(2)
        with m1:
            st.markdown("<h5 style='text-align: center; font-weight:bold; color: #009862;'> Cost Type By Branch </h5> " ,unsafe_allow_html=True)
            st_pyecharts(bar1,height=350)
        with m2: 
            st.markdown("<h5 style='text-align: center; font-weight:bold; color: #009862;'> Cost Type During Months </h5> " ,unsafe_allow_html=True)  
            st_pyecharts(line1,height=350)
    

    #------------------------------------------------------
    #bold line separator
    st.markdown("""<hr style="height:4px;border:none;color:#C00000;background-color:#C00000;" /> """, unsafe_allow_html=True)
    #title
    st.markdown("<h3 style='text-align: center; font-weight:bold; color: #354968   ;'> Expenses Analysis </h3> " ,unsafe_allow_html=True)    
    # Radio Buttons style
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;border:2px solid #C00000;border-radius:10px} </style>', unsafe_allow_html=True)
    st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;font-size:19px;color:#C00000;}</style>', unsafe_allow_html=True)
    #----Multiselect----------------------------------
    choose=st.radio(".",("ALL","Zayed","Sheraton","Tagamoa"))
    if choose == 'Zayed':
      df6=  df6.query('Branch == "ZAYED"')
    if choose == 'Sheraton':
      df6=  df6.query('Branch == "SHERATON"')
    if choose == 'Tagamoa':
      df6=  df6.query('Branch == "TAGAMOA"')
    st.markdown("")
    st.markdown("")
    #----------------Admin_data------------------------------
    dfs = df6[df6['ExpType'] == "ADMIN"]
    admin_d = dfs.groupby(['ExpName']).sum()[['AMOUNT']].reset_index().sort_values(by=['AMOUNT'],ascending=False)
    admin_d['PCT %'] = round(admin_d['AMOUNT']/ admin_d['AMOUNT'].sum()*100 ,1)
    admin_d['AVG_Per_Month'] = round(admin_d['AMOUNT']/ len(df6['MONTH'].unique()))
    #-------
    dfd = df6[df6['ExpType'] == "COGS"]
    cogs_d = dfd.groupby(['ExpName']).sum()[['AMOUNT']].reset_index().sort_values(by=['AMOUNT'],ascending=False)
    cogs_d['PCT %'] = round(cogs_d['AMOUNT']/ cogs_d['AMOUNT'].sum()*100,2)
    cogs_d['AVG_Per_Month'] = round(cogs_d['AMOUNT']/ len(df6['MONTH'].unique()))
    
    #------------------------------------------------------
    d1,d2 = st.columns(2)
    with d1:
        st.markdown("<h5 style='text-align: center; font-weight:bold; color: #009862;'> Admin Cost  </h5> " ,unsafe_allow_html=True)

        gb = GridOptionsBuilder.from_dataframe(admin_d)
        gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
        #gb.configure_side_bar() #Add a sidebar
        #gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
        gridOptions = gb.build()

        grid_response = AgGrid(
        admin_d,
        gridOptions=gridOptions,
        data_return_mode='FILTERED', 
        update_mode='MODEL_CHANGED', 
        fit_columns_on_grid_load=True,
        theme='blue', #Add theme color to the table
        enable_enterprise_modules=True,
        height=350, 
        width='100%',
        reload_data=True
    )
    
        
    with d2:
        st.markdown("<h5 style='text-align: center; font-weight:bold; color: #009862;'> COGS  </h5> " ,unsafe_allow_html=True)

        gb = GridOptionsBuilder.from_dataframe(cogs_d)
        gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
        #gb.configure_side_bar() #Add a sidebar
        #gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
        gridOptions = gb.build()

        grid_response = AgGrid(
        cogs_d,
        gridOptions=gridOptions,
        data_return_mode='AS_INPUT', 
        update_mode='MODEL_CHANGED', 
        fit_columns_on_grid_load=True,
        theme='blue', #Add theme color to the table
        enable_enterprise_modules=True,
        height=350, 
        width='100%',
        reload_data=True
    )
 
#===============================================================================================
# Building Profit Report  
if selected == 'Profit Report':
    #------Set cards style------------------
    st.markdown("""
        <style>
        div[data-testid="metric-container"] {
        background-color: #f4f9f2;
        border: 2px solid rgba(28, 131, 225, 0.1);
        padding: 5% 5% 5% 10%;
        border-radius: 10px;
        border-color: #B45904;
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
        font-size:17px
        }
        </style>
        
        """
        , unsafe_allow_html=True)
    # Reading COST DF from google sheet
    sheet_id = '1BNvKxtMtoxzw22HIfxezPw9UkoRCQibKkAB5xTgpvWw'
    sheet_name_C = 'COST'
    sheet_name_S = 'SALES'
    url_C = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name_C}'
    url_S = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name_S}'
    # update every 10 mins
    st_autorefresh(interval=10* 60 * 1000,key=None)
    @st.experimental_memo(ttl=600)
    def get_pft_data():
        df_C = pd.read_csv(url_C)
        cost = df_C.groupby(['Branch','MONTH']).sum()[['AMOUNT']].reset_index()
        cost = cost.rename(columns={'MONTH':'MONTH_C', 'Branch':'Branch_C'})
        df_S = pd.read_csv(url_S)
        sales = df_S.groupby(['Branch','MONTH','MONTH_NAME']).sum()[['TOTAL']].reset_index()
        sales = sales.rename(columns={'MONTH':'MONTH_S', 'Branch':'Branch_S'})
        df = pd.concat([cost, sales], axis=1).reset_index()
        df.drop(['Branch_C','MONTH_C'],axis=1, inplace=True)
        df['Profit'] = df['TOTAL'] - df['AMOUNT']
        return df
    df_pf = get_pft_data()
    df_pf1 = get_pft_data()
    #----------------------------------------
    #main title
    st.markdown("<h1 style='text-align: center; font-weight:bold; color: #C00000;'> Real-time Profit Report</h1> " ,unsafe_allow_html=True)
    #bold line separator
    st.markdown("""<hr style="height:4px;border:none;color:#C00000;background-color:#C00000;" /> """, unsafe_allow_html=True)
    # title
    st.markdown("<h2 style='text-align: center; font-weight:bold; color: #354968;'> General Profit Insights</h2> " ,unsafe_allow_html=True)
    # Radio Buttons style
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;border:2px solid #C00000;border-radius:10px} </style>', unsafe_allow_html=True)
    st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;font-size:19px;color:#28965A;}</style>', unsafe_allow_html=True)
    #----set radio buttons----------------------------------
    choose=st.radio("",("All","Zayed","Sheraton","Tagamoa"))
    if choose == 'Zayed':
      df_pf=  df_pf.query('Branch_S == "ZAYED"')
      
      
    if choose == 'Sheraton':
      df_pf=  df_pf.query('Branch_S == "SHERATON"')
      
    if choose == 'Tagamoa':
      df_pf=  df_pf.query('Branch_S == "TAGAMOA"')
      
    st.markdown("")
    st.markdown("")
    #-------------------------------------------------
    #Profit KPI's--------------------------------
    tot_pf = df_pf['Profit'].sum()
    avg_p = tot_pf / len(df_pf['MONTH_S'].unique())
    c_to_pf = df_pf['AMOUNT'].sum() / tot_pf
    c_to_p_measure = round(1000 * c_to_pf)
    #-------------------------------
    pf1, pf2, pf3 = st.columns(3)
    pf1.metric(
        label='Total Profit',
        value= str(round(tot_pf/ 1e3,2)) + " K"
    )
    pf2.metric(
        label='Avg Profit/Month',
        value= str(round(avg_p/ 1e3,2)) + " K"
    )
    pf3.metric(
        label='Cost To Profit %',
        value= str(round(c_to_pf,2)) + " %"
    )
    #-------- Profit_Branch_Data---------------------------------- 
    zayed_pf = df_pf.query('Branch_S == "ZAYED"')['Profit'].sum()
    sheraton_pf = df_pf.query('Branch_S == "SHERATON"')['Profit'].sum()
    tagamoa_pf = df_pf.query('Branch_S == "TAGAMOA"')['Profit'].sum()
    #------------Profit cards----------------------------
    st.markdown("<h3 style='text-align: center; font-weight:bold; color: #354968;'> Profit Distribution By Branch </h3> " ,unsafe_allow_html=True)    
    pf1, pf2, pf3= st.columns(3)
    pf1.metric(
        label = 'Zayed Profit %',
        value = str(round(zayed_pf/tot_pf, 4 )*100) + " %",
    )
    pf2.metric(
        label = 'Sheraton Profit %',
        value = str(round(sheraton_pf/tot_pf, 4)*100) + " %",
    )
    pf3.metric(
        label = 'Tagamoa Profit %',
        value = str(round(tagamoa_pf/tot_pf, 4)*100) + " %",
    )
    #------------Pie1_chart_data----------------------------
    pie_dat = df_pf.groupby(['Branch_S']).sum()[['Profit']].reset_index()
    x = pie_dat['Branch_S'].unique().tolist() 
    y = pie_dat['Profit'].values.tolist()
    
    #------------------------------------------------------
    data_pair = [list(z) for z in zip(x, y)]
    data_pair.sort(key=lambda x: x[1])
    pie1 = (
        Pie(init_opts=opts.InitOpts( bg_color="#f0f0f0"))
    .add("", data_pair=data_pair)
    .set_global_opts(title_opts=opts.TitleOpts(title=""))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        
    
    
    )
    #------------Line_chart_data----------------------------
    lin_dat = df_pf.groupby(['Branch_S','MONTH_S']).sum()[['Profit']].reset_index()
    lin_za = lin_dat.query('Branch_S == "ZAYED"')[['Profit']]
    lin_sh = lin_dat.query('Branch_S == "SHERATON"')[['MONTH_S','Profit']].sort_values(by=['MONTH_S'])
    lin_tag = lin_dat.query('Branch_S == "TAGAMOA"')[['MONTH_S','Profit']].sort_values(by=['MONTH_S'])
    line = (
            Bar(init_opts=opts.InitOpts( width="650px", height="400px",bg_color="#f0f0f0"))
            .add_xaxis(lin_dat['MONTH_S'].unique().tolist())
            .add_yaxis("Zayed", lin_za['Profit'].values.tolist())
            .add_yaxis("Shheraton", lin_sh['Profit'].values.tolist())
            .add_yaxis("Tagamoa", lin_tag['Profit'].values.tolist())
            .set_global_opts(
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            title_opts=opts.TitleOpts(title=""),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        )
            
    )
            
    with st.expander('View Visuals'):   
        l1,l2 = st.columns(2)
        with l1:
            st.markdown("<h5 style='text-align: center; font-weight:bold; color: #009862;'> Profit By Branch </h5> " ,unsafe_allow_html=True)
            st_pyecharts(pie1,height=350)
        with l2:
            st.markdown("<h5 style='text-align: center; font-weight:bold; color: #009862;'> Profit During Months </h5> " ,unsafe_allow_html=True)
            st_pyecharts(line,height=350)
    
    #------------------------------------------------------
    
