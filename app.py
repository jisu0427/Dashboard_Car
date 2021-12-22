import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle

from eda_app import run_eda_app
from ml_app import run_ml_app

def main():
    st.title('자동차 가격 예측')

    # 사이드바 메뉴
    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == 'Home' :
        st.write('이 앱은 고객데이터와 자동차 구매 데이터에 대한 내용입니다. 해당 고객의 정보를 입력하면, 얼마정도의 차량을 구매할 수 있는지 예측해 줍니다.')
        st.write('왼쪽의 사이드바에서 선택하세요.')
    elif choice == 'EDA' :
        run_eda_app()
    elif choice == 'ML' :
        run_ml_app()


if __name__ == '__main__' :
    main()

