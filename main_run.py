from Page import basestruct as bs,result_show as rs
from SearchResult import get_search_result as gsr
import streamlit as st


# 初始化 session_state
if 'seach' not in st.session_state:
    st.session_state.seach = False

with st.sidebar:
    selected_function = st.radio("功能菜单", ["搜索页面"])
    name=bs()

if selected_function == '搜索页面':
    if st.session_state.seach:
        print(rs(gsr(name)))
    else:
        st.title("使用法则！使用法则！使用法则！")
        st.write('---')
        st.write("首先在侧边栏里搜索你想看的动漫\n\n其次在你想看的动漫那里点击”获取集数“\n\n最后你想看哪一集就输入哪一集然后再次点击”获取集数“")
        st.write('---')





# with st.sidebar:
#     selected_function = st.radio("功能菜单", ["搜索页面","搜索结果"])
#
# if selected_function == '搜索页面':
#     name=bs()
#     st.session_state.name=name
#
#
# if selected_function == '搜索结果':
#     if st.session_state.seach:
#         st.session_state.seach = False
#         name=st.session_state.name
#         ra(gsr(name))
#     else:
#         st.write("摸鱼中……")
