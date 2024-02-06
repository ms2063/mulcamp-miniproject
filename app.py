import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def type_mean(df, year, month, housing_type):
    # 데이터타입
    df['year'] = df['year'].astype(int)
    df['month'] = df['month'].astype(int)
    df['mean'] = df['mean'].astype(int)

    #특정 년도 및 월 선택
    filtered_df = df[(df['year'] == year) & (df['month'] == month)]
    filtered_df = filtered_df.sort_values(by='mean', ascending=False)

    # 건물 용도별 제목
    title_map = {
        '아파트': '구별 아파트 매매(실거래가) 평균',
        '오피스텔': '구별 오피스텔 매매(실거래가) 평균',
        '단독다가구': '구별 단독다가구 매매(실거래가) 평균',
        '연립다세대': '구별 연립다세대 매매(실거래가) 평균'
    }
    title = f"{title_map[housing_type]} <br><sup> 단위(만원)</sup>"

    # 시각화 
    fig = go.Figure(data=[
        go.Bar(
            name='매매값',
            y=filtered_df['mean'],
            x=filtered_df['SIG_KOR_NM'],
            marker_color='green',
            opacity=1,
            marker_pattern_shape='-',
        )
    ])

    fig.update_layout(
        title=title,
        title_font_family="맑은고딕",
        title_font_size=18,
        hoverlabel=dict(
            bgcolor='black',
            font_size=15,
            font_color='white'
        ),
        hovermode="x unified",
        template='plotly_white',
        xaxis_tickangle=90,
        yaxis_tickformat=',',
        legend=dict(orientation='h', xanchor="center", x=0.85, y=1.1),
        barmode='group'
    )
    return fig

@st.cache_data
def load_data(filepath):
    return pd.read_csv(filepath)

def type_scatter(df, house_type):
    df_filtered = df[df['HOUSE_TYPE'] == house_type]
    fig = px.scatter(df_filtered, x='BLDG_AREA', y='OBJ_AMT',
                     title=f'{house_type} 크기(㎡) 대비 매매 가격(만 원)',
                     labels={'BLDG_AREA': '크기(㎡)', 'OBJ_AMT': '매매 가격(만 원)'},
                     trendline='ols')
    return fig

def plot_price_trends_for_selection(df, sgg_nms, house_type):
    # Prepare a figure to plot trends for selected SGG_NM and HOUSE_TYPE
    fig = go.Figure()
    
    for sgg_nm in sgg_nms:
        # Filter data for each selected SGG_NM and HOUSE_TYPE
        filtered_df = df[(df['SGG_NM'] == sgg_nm) & (df['HOUSE_TYPE'] == house_type)]
        
        if not filtered_df.empty:
            # Aggregate data by DEAL_YMD to calculate average price
            price_trends = filtered_df.groupby(filtered_df['DEAL_YMD'].dt.to_period('M'))['OBJ_AMT'].mean().reset_index()
            price_trends['DEAL_YMD'] = price_trends['DEAL_YMD'].dt.to_timestamp()
            
            # Add each SGG_NM trend to the figure
            fig.add_trace(go.Scatter(x=price_trends['DEAL_YMD'], y=price_trends['OBJ_AMT'], mode='lines', name=sgg_nm))
    
    # Update layout for the combined figure
    fig.update_layout(title=f'{house_type} 가격 변동 추이 비교', xaxis_title='계약일', yaxis_title='평균 거래 가격 (만원)', hovermode="x unified")
    return fig

def main():
    st.title('부동산 유형별 데이터 분석')

    # 분석 유형 선택
    analysis_type = st.sidebar.selectbox("분석 유형을 선택하세요.",
                                         ["크기와 매매 가격 분석", "구별 매매 가격 평균", "지역별 가격 변동 추이"])

    if analysis_type == "크기와 매매 가격 분석":
        house_type = st.sidebar.selectbox('부동산 유형을 선택하세요.',
                                          ['아파트', '오피스텔', '단독다가구', '연립다세대'])
        #파일 로드 
        df = load_data('./data/data.csv')  
        fig = type_scatter(df, house_type)
        st.plotly_chart(fig)
    elif analysis_type == '구별 매매 가격 평균':
        year = int(st.sidebar.selectbox('년도를 입력하세요.', ['2024', '2023']))

        #선택된 년도에 따른 조건문
        if year == '2024':
            month_options = ['1']
            
        elif year == '2023':
            month_options = ['5', '6', '7', '8', '9', '10', '11', '12']

        month_options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
            
        month = st.sidebar.selectbox('월을 입력하세요.', month_options)
        month = int(month)
    
        
        housing_type = st.sidebar.selectbox('부동산 유형을 선택하세요.',
                                            ['아파트', '오피스텔', '단독다가구', '연립다세대'])
        
        file_paths = {
            '아파트': './data/merge_df1.csv',
            '오피스텔': './data/merge_df2.csv',
            '단독다가구': './data/merge_df3.csv',
            '연립다세대': './data/merge_df4.csv',
        }
        df = load_data(file_paths[housing_type])
        fig = type_mean(df, year, month, housing_type)
        st.plotly_chart(fig)
    
    elif analysis_type == "지역별 가격 변동 추이":
        df = load_data('./data/data.csv') 
        df['DEAL_YMD'] = pd.to_datetime(df['DEAL_YMD'], format='%Y%m%d')  
        
       # Select multiple SGG_NM values for comparison
        selected_sgg_nms = st.sidebar.multiselect('자치구명을 선택하세요.', df['SGG_NM'].unique(), default=df['SGG_NM'].unique()[0:2])
    
        # Select HOUSE_TYPE for analysis
        selected_house_type = st.sidebar.selectbox('주택 유형을 선택하세요.', df['HOUSE_TYPE'].unique())
    
        # Generate and display the visualization
        if selected_sgg_nms and selected_house_type:
            fig = plot_price_trends_for_selection(df, selected_sgg_nms, selected_house_type)
            st.plotly_chart(fig)
        else:
            st.warning('자치구명과 주택 유형을 선택해주세요.')

if __name__ == '__main__':
    main()
