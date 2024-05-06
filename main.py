import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np


parkinsson_model=pickle.load(open('parkinsson_disease.sav','rb'))



#side bar for navigation......

with st.sidebar:
    selected=option_menu('Disease Prediction System',
                         ['Parkinsson Disease Prediction'],
                         icons=['activity','person'],
                         default_index=0)

    

if(selected=='Parkinsson Disease Prediction'):
    st.title('Parkinsson Prediction using ML')
    MDVPFo=st.text_input('MDVP:Fo(Hz)')
    MDVPFhi=st.text_input('MDVP:Fhi(Hz)')
    MDVPFlo=st.text_input('MDVP:Flo(Hz)')
    MDVPJitter=st.text_input('MDVP:Jitter(%)')
    MDVPJitterAbs=st.text_input('MDVP:Jitter(Abs)')
    MDVPRAP=st.text_input('MDVP:RAP')
    MDVPPPQ=st.text_input('MDVP:PPQ ')
    JitterDDP=st.text_input('Jitter:DDP')
    MDVPShimmer=st.text_input('MDVP:Shimmer')
    MDVPShimmer=st.text_input('MDVP:Shimmer(dB)')
    ShimmerAPQ3=st.text_input('Shimmer:APQ3')
    ShimmerAPQ5=st.text_input('Shimmer:APQ5 ')
    MDVPAPQ=st.text_input('MDVP:APQ')
    ShimmerDDA=st.text_input('Shimmer:DDA')
    NHR=st.text_input('NHR')
    HNR=st.text_input('HNR')
    RPDE=st.text_input('RPDE')
    DFA=st.text_input('DFA')
    spread1=st.text_input('spread1')
    spread2=st.text_input('spread2')
    D2=st.text_input('D2')
    PPE=st.text_input('PPE')
    result=""
    if(st.button('check for parkinsson')):
        prediction2=parkinsson_model.predict([[MDVPFo,MDVPFhi,MDVPFlo,MDVPJitter,MDVPJitterAbs,MDVPRAP,MDVPPPQ,JitterDDP,MDVPShimmer,MDVPShimmer,ShimmerAPQ3,ShimmerAPQ5,MDVPAPQ,ShimmerDDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        if(prediction2[0]==0):
            result='The person is not having the parkinsson disease'
        else:
            result='The person having a parkinsson disease'
    st.success(result)
