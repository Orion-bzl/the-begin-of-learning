import streamlit as st
import os
from openai import OpenAI
from datetime import datetime
import json
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")
def save_session():
    if st.session_state.current_dialogue:
        session_data={
            "name":st.session_state["name"],
            "character":st.session_state["character"],
            "current_dialogue":st.session_state.current_dialogue,
            "messages":st.session_state.messages
        }
        if not os.path.exists("session_data"):
                    os.makedirs("session_data")
        with open(f"session_data/{st.session_state.current_dialogue}", "w",encoding="utf-8") as f:
                    json.dump(session_data, f,indent=4,ensure_ascii=False)
#初始化缓存
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "name"  not in st.session_state:
    st.session_state["name"]="deepseek"
if "character" not in st.session_state:
    st.session_state["character"]="You are a helpful assistant"
if "current_dialogue" not in st.session_state:
    st.session_state["current_dialogue"]=datetime.now().strftime("%Y-%m-%d_%H-%M-%S.json")
#加载全部会话信息
def load_session():
    session_list=[]
    if os.path.exists("session_data"):
        for file in os.listdir("session_data"):
            if file.endswith(".json"):
                 session_list.append(file[:-5])
    session_list.reverse()
    return session_list
                
#加载指定会话信息
def load_dialogue(dialogue_name):
     if os.path.exists(f"session_data/{dialogue_name}.json"):
        with open(f"session_data/{dialogue_name}.json", "r",encoding="utf-8") as f:
            dialogue_data = json.load(f)
            st.session_state.messages = dialogue_data["messages"]
            st.session_state["name"]=dialogue_data["name"]
            st.session_state["character"]=dialogue_data["character"]
            st.session_state.current_dialogue=f"{dialogue_name}.json"

        
#删除指定会话信息
def delete_dialogue(dialogue_name):
     if os.path.exists(f"session_data/{dialogue_name}.json"):
          os.remove(f"session_data/{dialogue_name}.json")

#页面布局
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

#标题
st.title("AI智能伴侣")

#logo
st.logo("🤖")

for message in st.session_state.messages:#显示历史对话
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    elif message["role"] == "assistant":
        st.chat_message("assistant").write(message["content"])

#侧边栏
with st.sidebar:
    st.subheader("AI控制面板")
    if st.button("新建对话",width="stretch"):
        save_session()
        if st.session_state.messages:
            st.session_state.messages = []
            st.session_state.current_dialogue=datetime.now().strftime("%Y-%m-%d_%H-%M-%S.json")
            save_session()
            st.rerun()
    st.text("历史对话记录")
    session_list=load_session()
    for session in session_list:
        col1,col2=st.columns([4,1])
        with col1:
             if st.button(session,width="stretch",type="primary" if f"{session}.json"==st.session_state.current_dialogue else "secondary"):
                load_dialogue(session)
                st.rerun()
        with col2:
             if st.button("",icon="🗑️",width="stretch",key=session):
                delete_dialogue(session)
                if session==st.session_state.current_dialogue:
                    st.session_state.messages=[]
                    st.session_state.current_dialogue=datetime.now().strftime("%Y-%m-%d_%H-%M-%S.json")
                st.rerun()


    st.divider()
    
    name=st.text_input("伴侣名称",placeholder="请输入伴侣名称",value="deepseek")
    character=st.text_area("伴侣性格",placeholder="请输入伴侣性格",value="You are a helpful assistant")
    if name:
        st.session_state["name"]=name
    if character:
        st.session_state["character"]=character

#输入框
system_prompt = """
你是用户的伴侣，请回答用户问题。
1.请用用户使用的语言回答问题
2.每次只回复一条消息
3.有需要的话可以使用emoji表情
4.根据指定的名称和性格给出相应的回复

你的伴侣名称是：%s
你的伴侣性格是：%s
"""%(st.session_state["name"],st.session_state["character"])
promot=st.chat_input("请输入")
print(promot)
if promot:
    st.chat_message("user").write(promot)
    st.session_state.messages.append({"role": "user", "content": promot})#保存用户输入

#调用ai大模型
    response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": system_prompt},
        *st.session_state.messages,
    ],
    stream=True,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
    )
    #非流式输出
    #print(response.choices[0].message.content)
    #st.chat_message("assistant").write(response.choices[0].message.content)
    #st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})#保存ai输出
    #流式输出
    respones_text=st.empty()#创建一个空对象
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content:
            full_response += chunk.choices[0].delta.content
            respones_text.chat_message("assistant").write(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    save_session()



