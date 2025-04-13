import streamlit as st
from SearchResult import skip_get_url as sgu
from SearchResult import get_video_url as gvu

def basestruct():
    st.title("动漫梦工厂")
    st.write("超简洁版---个人使用")
    st.write('---')
    cartoon_name = st.text_input("输入动漫名称")

    if st.button("搜索",key='search'):
        st.session_state.seach = True
    st.write('---')
    return cartoon_name

def result_show(detail):

    for i in range(0,(len(detail)-2),3):
        col1, col2 = st.columns(2)
        with col1:
            st.image(detail[i+2])
        with col2:
            st.write(detail[i+1])
            see_num = st.text_input('输入观看集数（输入0是最后一集）：',key=f'input{i}')
            num=sgu(str(detail[i]))[0]
            
            if st.button("集数获取",key=f'button{i}'):
                st.write(f"共{num}集")
                if not see_num.isdigit():
                    try:
                        if int(see_num) <=0 :
                            st.write("集数当然是从“1”开始啦！！！")
                    except:
                        st.write(f"你TM了个巴子的，集数是数字！整数！！你TM了个巴子的输入“{see_num}”  ？\n\n小心额锤你")
               
                else:
                    if see_num != '':
                        if int(see_num) > int(num):
                            st.write(f"你TM了个巴子的，一共才{num}集，你却要看{see_num}集\n\n小心额锤你")
                        else:
                            st.write(gvu(sgu(str(detail[i]))[1][int(see_num)-1]))
                

        st.write("---")








