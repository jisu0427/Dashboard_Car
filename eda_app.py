import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle
import matplotlib.pyplot as plt
import seaborn as sns 


def run_eda_app():
    st.subheader('EDA 화면입니다')

    df = pd.read_csv('data/Car_Purchasing_Data.csv', encoding= 'ISO-8859-1')

    radio_menu = ['데이터프레임','통계치']
    selected_radio = st.radio('선택하세요',radio_menu)
    if selected_radio == '데이터프레임':
        st.dataframe(df)
    elif selected_radio == '통계치':
        st.dataframe(df.describe())

    # 컬럼을 선택하면, 해당 컬럼들만 데이터 프레임 표시하는 화면
    print(df.columns)
    selected_columns = st.multiselect('컬럼을 선택하세요',df.columns)
    if len(selected_columns) != 0:
        st.dataframe(df[selected_columns])
    else: 
        st.text('선택된 컬럼이 없습니다.')

    # 상관관계 분석을 위한, 상관계수 보여주는 화면 개발
    # 문자열이 아닌 컬럼들만 나오게 한다. gender ~ car purchase amount
    st.subheader('상관계수')

    df_corr = df.iloc[ : , 3: ]
    selected_corr = st.multiselect('상관계수 컬럼 선택',df_corr.columns)

    # 유저가 1개라도 컬럼을 선택했을 경우 
    if len(selected_corr) > 0:
        # 상관계수를 수치로도 구하고, 차트로도 표시하라.
        st.dataframe(df_corr[selected_corr].corr()) #수치 확인
        
        fig1 = sns.pairplot(data=df_corr[selected_corr])
        st.pyplot(fig1)

    # 유저가 컬럼을 선택하지 않은경우
    else :                                
        st.text('상관계수를 확인할 컬럼이 없습니다.')

    # 유저가 컬럼을 선택하면,
    # 해당 컬럼의 min과 max에 해당하는 사람이 누구인지
    # 그 사람의 데이터를 화면에 보여주는 기능 개발.
    st.subheader('해당 컬럼의 min과 maxx 검색')
    print( df.columns )
    print( df.dtypes != object )
    print( df.columns[ df.dtypes != object ] )
    
    number_columns = df.columns [ df.dtypes != object ] 
    selected_minmax_column = st.selectbox('컬럼 선택', number_columns)

    # 선택한 컬럼의 최소값과 최대값에 해당되는 사람의 데이터 출력
    if selected_minmax_column is not None :
        st.text('최솟값')
        print(df.loc[df[selected_minmax_column] == df[selected_minmax_column].min(), : ])
        st.dataframe(df.loc[df[selected_minmax_column] == df[selected_minmax_column].min(), : ])
        st.text('최댓값')
        st.dataframe(df.loc[df[selected_minmax_column] == df[selected_minmax_column].max(), : ])

    
    

    # 고객의 이름을 검색할 수 있는 기능 개발
    # 1. 유저한테 검색어 입력받기
    st.subheader('사람 검색')
    word = st.text_input('이름을 검색하세요')
    
    # 1-1 검색을 위해 다 소문자로 바꾸기
    word = word.lower()

    # 2. 검색어를 데이터프레임의 Customer Name 컬럼에서 검색해서 가져오기
    df_search = df.loc[df['Customer Name'].str.lower().str.contains(word)]

    # 3. 화면에 결과를 보여준다.
    st.dataframe( df_search )


# str.lower().str.contains(search_name)