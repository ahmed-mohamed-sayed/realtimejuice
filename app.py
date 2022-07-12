
from matplotlib.pyplot import legend
import streamlit as st 
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
import pandas as pd 
from streamlit_option_menu import option_menu
from streamlit_autorefresh import st_autorefresh
import streamlit.components.v1 as components
from pyecharts import options as opts
from pyecharts.charts import Funnel, Bar, Line,Pie




st.set_page_config(layout='wide'
                )

        
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
    #------Set cards style------------------
    st.markdown("""
        <style>
        div[data-testid="metric-container"] {
        background-color: #f4f9f2;
        border: 2px solid rgba(28, 131, 225, 0.1);
        padding: 5% 5% 5% 10%;
        border-radius: 5px;
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
#===============================================================================================
    
    st.markdown("<h1 style='text-align: center; font-weight:bold; color: #C00000;'> Real-time Sales Report</h1> " ,unsafe_allow_html=True)
    
    #----Multiselect----------------------------------
    opt = df1["Branch"].unique().tolist()
    opt.insert(0,'ALL')
    branch = st.multiselect("Branch",opt, default='ALL')
    if "ALL" in branch:
        branch = opt  
   
    df1 = df1.query( 'Branch == @branch  ')
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
        label = 'Avg Orders Per Month',
        value = round(avg_or),
    )
    t5.metric(
        label = 'Avg Order Value "Egp"',
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
    pie1 = (
        Pie(init_opts=opts.InitOpts( width="650px", height="400px",bg_color="#f0f0f0"))
    .add("", data_pair=data_pairs)
    .set_global_opts(title_opts=opts.TitleOpts(title=""))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        
    .render_embed()
    
    )
    #------------Line_chart_data----------------------------
    lin_s = df1.groupby(['Branch','MONTH']).sum()[['TOTAL']].reset_index()
    lin_sz = lin_s.query('Branch == "ZAYED"')[['TOTAL']]
    lin_ssh = lin_s.query('Branch == "SHERATON"')[['MONTH','TOTAL']].sort_values(by=['MONTH'])
    lin_stag = lin_s.query('Branch == "TAGAMOA"')[['MONTH','TOTAL']].sort_values(by=['MONTH'])
    
    line = (
            Line(init_opts=opts.InitOpts( width="650px", height="400px",bg_color="#f0f0f0"))
            .add_xaxis(xaxis_data=lin_s['MONTH'])
            .add_yaxis(
                 series_name="Zayed",
                 y_axis=lin_sz['TOTAL'],
                
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
            
            .render_embed()
)
    with st.expander('View Visuals'):   
        l1,l2 = st.columns(2)
        with l1:
            st.markdown("<h5 style='text-align: center; font-weight:bold; color: #B45904;'> Total Sales by Branch </h5> " ,unsafe_allow_html=True)   
            components.html(pie1 , width=1000, height=500)
        with l2:
            st.markdown("<h5 style='text-align: center; font-weight:bold; color: #B45904;'> Total Sales During Months </h5> " ,unsafe_allow_html=True)   
            components.html(line , width=1000, height=500)
    
#===============================================================================================
# Building Cost Report     

if selected == 'Cost Report':
    #------Set cards style------------------
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
    #----------------------------------------
    # Reading COST DF from google sheet
    sheet_id = '1BNvKxtMtoxzw22HIfxezPw9UkoRCQibKkAB5xTgpvWw'
    sheet_name = 'COST'
    url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
    # update every 10 mins
    st_autorefresh(interval=10* 60 * 1000,key=None)
    @st.experimental_memo(ttl=600)
    def get_data():
        df = pd.read_csv(url)
        return df
    df = get_data()


#===============================================================================================
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
        Pie(init_opts=opts.InitOpts( width="650px", height="400px",bg_color="#f0f0f0"))
    .add("", data_pair=data_pair1)
    .set_global_opts(title_opts=opts.TitleOpts(title=""))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        
    .render_embed()
    
    )
    #------------Line_chart_data----------------------------
    lin_dat = df.groupby(['Branch','MONTH']).sum()[['AMOUNT']].reset_index()
    lin_za = lin_dat.query('Branch == "ZAYED"')[['AMOUNT']]
    lin_sh = lin_dat.query('Branch == "SHERATON"')[['MONTH','AMOUNT']].sort_values(by=['MONTH'])
    lin_tag = lin_dat.query('Branch == "TAGAMOA"')[['MONTH','AMOUNT']].sort_values(by=['MONTH'])
    
    line = (
            Line(init_opts=opts.InitOpts( width="650px", height="400px",bg_color="#f0f0f0"))
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
            
            .render_embed()
)
    with st.expander('View Visuals'):   
        l1,l2 = st.columns(2)
        with l1:
            st.markdown("<h5 style='text-align: center; font-weight:bold; color: #009862;'> Total Cost by Branch </h5> " ,unsafe_allow_html=True)   
            components.html(pie1 , width=1000, height=500)
        with l2:
            st.markdown("<h5 style='text-align: center; font-weight:bold; color: #009862;'> Total Cost During Months </h5> " ,unsafe_allow_html=True)   
            components.html(line , width=1000, height=500)
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
            Bar(init_opts=opts.InitOpts(width="650px", height="500px", bg_color="#f0f0f0"))
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
            .render_embed()
        )
    #-------Line1 Chart Data---------------------------------

    x = df.groupby(['ExpType','MONTH']).sum()[['AMOUNT']].reset_index()
    admin = x.query('ExpType == "ADMIN"')[['MONTH','AMOUNT']].sort_values(by=['MONTH'])
    cogs = x.query('ExpType == "COGS"')[['MONTH','AMOUNT']].sort_values(by=['MONTH'])
    adver = x.query('ExpType == "ADVERTISING"')[['MONTH','AMOUNT']].sort_values(by=['MONTH'])
    #------------------------------------------------------
    line1 =    (
            Line(init_opts=opts.InitOpts( width="650px", height="500px",bg_color="#f0f0f0"))
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
            
            .render_embed()
        )
    with st.expander('View Visuals'):
        m1, m2 = st.columns(2)
        with m1:
            st.markdown("<h5 style='text-align: center; font-weight:bold; color: #009862;'> Cost Type By Branch </h5> " ,unsafe_allow_html=True)
            components.html(bar1 , width=1000, height=500)
        with m2: 
            st.markdown("<h5 style='text-align: center; font-weight:bold; color: #009862;'> Cost Type During Months </h5> " ,unsafe_allow_html=True)  
            components.html(line1 , width=1000, height=500)
    

    #------------------------------------------------------
    st.markdown("<h3 style='text-align: center; font-weight:bold; color: rgb(30, 103, 119)   ;'> Expenses Analysis </h3> " ,unsafe_allow_html=True)    

    #-------Fun1 Chart Data---------------------------------
    # exp_nm = df.groupby(['ExpName','ExpType']).sum()[['AMOUNT']].sort_values(by='AMOUNT',ascending=False).reset_index()
    # exp_nm= exp_nm[exp_nm['ExpType']== 'ADMIN']
    # x_data = exp_nm['ExpName'].unique().tolist()   
    # y_data = exp_nm['AMOUNT'].values.tolist()
    #------------------------------------------------------
    
    # data = [[x_data[i], y_data[i]] for i in range(len(x_data))]

    # fun1 = (
    #         Funnel(init_opts=opts.InitOpts(width="1050px", height="900px",bg_color="#f9f9f9"))
    #         .add(
    #             series_name="",
    #             data_pair=data,
    #             gap=3,
    #             tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}"),
    #             label_opts=opts.LabelOpts(is_show=True, position="inside"),
    #             itemstyle_opts=opts.ItemStyleOpts(border_color="#f0f0f0", border_width=1),
    #         )
    #         .set_global_opts(title_opts=opts.TitleOpts(title="", subtitle=""),
    #                          legend_opts=opts.LegendOpts( pos_top="1%"),)
    #         .render_embed()
    #     )
 
    # components.html(fun1, width=1200, height=1000 )
    
    
    #----------------Admin_data------------------------------
    dfs = df[df['ExpType'] == "ADMIN"]
    admin_d = dfs.groupby(['ExpName']).sum()[['AMOUNT']].reset_index().sort_values(by=['AMOUNT'],ascending=False)
    admin_d['PCT %'] = round(admin_d['AMOUNT']/ admin_d['AMOUNT'].sum()*100 ,1)
    admin_d['AVG_Per_Month'] = round(admin_d['AMOUNT']/ len(df['MONTH'].unique()))
    #-------
    dfd = df[df['ExpType'] == "COGS"]
    cogs_d = dfd.groupby(['ExpName']).sum()[['AMOUNT']].reset_index().sort_values(by=['AMOUNT'],ascending=False)
    cogs_d['PCT %'] = round(cogs_d['AMOUNT']/ cogs_d['AMOUNT'].sum()*100,2)
    cogs_d['AVG_Per_Month'] = round(cogs_d['AMOUNT']/ len(df['MONTH'].unique()))
    
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
    st.markdown("<h2 style='text-align: center; font-weight:bold; color: #C00000;'> Profit Report</h2> " ,unsafe_allow_html=True)
