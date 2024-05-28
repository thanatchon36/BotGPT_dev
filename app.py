import streamlit as st
from streamlit_feedback import streamlit_feedback
import time
import datetime
import pandas as pd
from PIL import Image
import os
import csv
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import requests
from ast import literal_eval
import random

def get_response(prompt, temperature, context = []):
    start_time = time.time()
    api_route = 'botgpt_query_dev'
    post_params = {'prompt': f"{prompt}",
                   'context': context,
                   'temperature': temperature,
                }
    res = requests.post(f'https://pc140032646.bot.or.th/{api_route}', json = post_params, verify="/DA_WORKSPACE/GLOBAL_WS/ssl_cer/WS2B/pc140032646.bot.or.th.pem")
    execution_time = time.time() - start_time
    execution_time = round(execution_time, 2)
    return {'response': res.json()['response'], 'raw_input': res.json()['raw_input'], 'raw_output': res.json()['raw_output'], 'engine': res.json()['engine'], 'frontend_query_time': execution_time, 'backend_query_time': res.json()['query_time_sec']}

def get_response_2(prompt, temperature, context = []):
    start_time = time.time()
    api_route = 'botgpt_query_dev'
    post_params = {'prompt': f"{prompt}",
                   'context': context,
                   'temperature': temperature,
                }
    res = requests.post(f'https://pc140032645.bot.or.th/{api_route}', json = post_params, verify="/DA_WORKSPACE/GLOBAL_WS/ssl_cer/WS2A/pc140032645.bot.or.th.pem")
    execution_time = time.time() - start_time
    execution_time = round(execution_time, 2)
    return {'response': res.json()['response'], 'raw_input': res.json()['raw_input'], 'raw_output': res.json()['raw_output'], 'engine': res.json()['engine'], 'frontend_query_time': execution_time, 'backend_query_time': res.json()['query_time_sec']}
def get_response_3(message,history):
    start_time = time.time()
    url = 'https://pc140032645.bot.or.th/botgpt_query_autogen'
    myobj = { "prompt": message, "history": history }
    result = requests.post(url, json = myobj, verify = '/DA_WORKSPACE/GLOBAL_WS/ssl_cer/WS2A/pc140032645.bot.or.th.pem').json()
    execution_time = time.time() - start_time
    execution_time = round(execution_time, 2)
    result['frontend_query_time'] = execution_time
    return result
def get_response_dev(prompt, temperature, context = []):
    start_time = time.time()
    time.sleep(3)
    execution_time = time.time() - start_time
    execution_time = round(execution_time, 2)
    return {'response': 'response', 'raw_input': 'raw_input', 'raw_output': 'raw_output', 'engine': 'engine', 'frontend_query_time': execution_time, 'backend_query_time': execution_time}

def get_response_dev_2(message, history):
    # start_time = time.time()
    # time.sleep(3)
    # execution_time = time.time() - start_time
    # execution_time = round(execution_time, 2)
    return {'response': {'content': 'หากต้องการหา transaction รายเดือนของรายธนาคาร สามารถใช้ SQL ดังนี้:\n\n```sql\nSELECT\n    YEAR(transaction_date) AS year,\n    MONTH(transaction_date) AS month,\n    bank_name,\n    COUNT(*) AS transaction_count\nFROM\n    transactions\nGROUP BY\n    YEAR(transaction_date),\n    MONTH(transaction_date),\n    bank_name\nORDER BY\n    YEAR(transaction_date),\n    MONTH(transaction_date),\n    bank_name;\n```\n\nในตัวอย่าง SQL นี้ เราใช้คอลัมน์ `transaction_date` เพื่อหาปีและเดือนของแต่ละ transaction และใช้คอลัมน์ `bank_name` เพื่อแสดงรายธนาคารที่นำส่ง transaction นี้ สุดท้ายแล้วนับจำนวน transaction ทั้งหมดที่มีในแต่ละปีและเดือน และเรียงลำดับตามปีที่ก่อน (จากน้อยไปมาก) และเดือนที่ก่อน (จากมกราคมถึงธันวาคม) และแสดงผลลัพธ์ในรูปแบบตาราง\n\n[TERMINATE]',
  'role': 'user',
  'name': 'SQL_Writer'},
 'history': [{'content': 'อยากทราบการเปลี่ยนแปลงข้อมูลราย transaction รายเดือนของรายธนาคาร',
   'role': 'user',
   'name': 'User_proxy'},
  {'content': 'ฉันคิดว่าคุณอาจสนใจ cube 9 ที่มีข้อมูลสินเชื่อราย Account ราย Transaction รายวัน ซึ่งสามารถให้ข้อมูลเกี่ยวกับการเปลี่ยนแปลงข้อมูลราย transaction รายเดือนของรายธนาคารได้\n\nคุณต้องการให้ฉันช่วยเลือกตัวแปรที่เกี่ยวข้องกับคำถามจาก cube 9 หรือไม่ หรือถ้าคุณมีข้อเสนอแนะเกี่ยวกับ cube อื่น ๆ ที่คุณอยากให้ฉันพิจารณาด้วย กรุณาบอกฉันเสมอนะครับ',
   'role': 'user',
   'name': 'Cube_Selector'},
  {'content': 'โอเครได้เลย', 'role': 'user', 'name': 'Decision_Agent'},
  {'tool_calls': [{'id': 'call_B0pwzCSpcB5nivMknU8P9OTa',
     'function': {'arguments': '{\n  "user_question": "What is the population of Thailand?",\n  "qdrant_number": 3\n}',
      'name': 'API_Retriever'},
     'type': 'function'}],
   'content': '',
   'role': 'assistant',
   'name': 'API_Caller'},
  {'content': 'ตัวแปรต่อไปนี้คือตัวแปรที่เกี่ยวข้องกับคำถามของท่านที่เราได้ดึงมาจาก Cube 3 โดยการจัดอันดับของ RAG pipeline:\n1.) key_organization_id\n2.) key_br_organization_name\n3.) key_br_organization_name_eng\n4.) key_debtor_group_id\n5.) key_counterparty_id\n6.) f1_br_8_organization_country_name_eng\n7.) f1_br_9_organization_country_name\n8.) f4_22_business_loan_profile_main_factory_location_province_name\nท่านพอใจกับ cube ที่เราได้เลือกและตัวแปรเหล่านี้หรือไม่ หากไม่รบกวนระบุข้อเสนอแนะเบื้องต้นเพื่อที่เราจะสามารถเลือก cube ใหม่ที่ตรงความต้องการท่านได้ [TERMINATE]',
   'tool_responses': [{'tool_call_id': 'call_B0pwzCSpcB5nivMknU8P9OTa',
     'role': 'tool',
     'content': 'ตัวแปรต่อไปนี้คือตัวแปรที่เกี่ยวข้องกับคำถามของท่านที่เราได้ดึงมาจาก Cube 3 โดยการจัดอันดับของ RAG pipeline:\n1.) key_organization_id\n2.) key_br_organization_name\n3.) key_br_organization_name_eng\n4.) key_debtor_group_id\n5.) key_counterparty_id\n6.) f1_br_8_organization_country_name_eng\n7.) f1_br_9_organization_country_name\n8.) f4_22_business_loan_profile_main_factory_location_province_name\nท่านพอใจกับ cube ที่เราได้เลือกและตัวแปรเหล่านี้หรือไม่ หากไม่รบกวนระบุข้อเสนอแนะเบื้องต้นเพื่อที่เราจะสามารถเลือก cube ใหม่ที่ตรงความต้องการท่านได้ [TERMINATE]'}],
   'role': 'tool',
   'name': 'Field_Finder'},
  {'content': 'เขียน SQL เพื่อหา transaction รายเดือนของรายธนาคาร',
   'role': 'user',
   'name': 'Loop_Agent'},
  {'content': 'หากต้องการหา transaction รายเดือนของรายธนาคาร สามารถใช้ SQL ดังนี้:\n\n```sql\nSELECT\n    YEAR(transaction_date) AS year,\n    MONTH(transaction_date) AS month,\n    bank_name,\n    COUNT(*) AS transaction_count\nFROM\n    transactions\nGROUP BY\n    YEAR(transaction_date),\n    MONTH(transaction_date),\n    bank_name\nORDER BY\n    YEAR(transaction_date),\n    MONTH(transaction_date),\n    bank_name;\n```\n\nในตัวอย่าง SQL นี้ เราใช้คอลัมน์ `transaction_date` เพื่อหาปีและเดือนของแต่ละ transaction และใช้คอลัมน์ `bank_name` เพื่อแสดงรายธนาคารที่นำส่ง transaction นี้ สุดท้ายแล้วนับจำนวน transaction ทั้งหมดที่มีในแต่ละปีและเดือน และเรียงลำดับตามปีที่ก่อน (จากน้อยไปมาก) และเดือนที่ก่อน (จากมกราคมถึงธันวาคม) และแสดงผลลัพธ์ในรูปแบบตาราง\n\n[TERMINATE]',
   'role': 'user',
   'name': 'SQL_Writer'}]}

def reset(df):
    cols = df.columns
    return df.reset_index()[cols]

show_chat_history_no = 5
admin_list = ['thanatcc', 'da']

st.set_page_config(page_title = 'BotGPT', page_icon = 'fav.png', layout="wide")

st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.login('BotGPT Login', 'main')

if st.session_state["authentication_status"]:
    
    if "chat_id" not in st.session_state:
        now = str(datetime.datetime.now())
        st.session_state.chat_id  = now
        st.session_state.history = []

    bot_image = Image.open('fav.png')
    bot_image_2 = Image.open('fav_3.png')
    user_image = Image.open('fav_2.png')

    with st.sidebar:
        
        clear_session_click = st.button("New Chat")
        if clear_session_click:
            st.session_state.messages = []
            st.session_state.context = []
            now = str(datetime.datetime.now())
            st.session_state.chat_id  = now
            st.session_state.history = []

        context_radio = st.radio(
            "Context:",
            ["ข้อมูลประกาศ", "Datacube", "Autogen"],
        )

        temperature_value = st.slider(
                'Select a temperature',
                0.0, 1.0, 1.0, step=0.05
                )
        
        dev_checkbox = st.checkbox('Development')
        
        csv_file = f"data/{st.session_state.username}.csv"
        file_exists = os.path.isfile(csv_file)
        if file_exists:
            if len(pd.read_csv(csv_file, sep = ',')) > 0:
                # Init State Sessioin
                if 'page' not in st.session_state:
                    st.session_state['page'] = 1
                    
                with st.expander("Chat History"):
                    hist_df = pd.read_csv(f'data/{st.session_state.username}.csv', sep = ',')
                    full_hist_df = hist_df.copy()
                    hist_df = reset(hist_df.sort_values(by = 'turn_id', ascending = False))
                    hist_df = hist_df.groupby('chat_id').first().reset_index()
                    hist_df = reset(hist_df.sort_values(by = 'turn_id', ascending = False))

                    hist_df['page'] = hist_df.index
                    hist_df['page'] = hist_df['page'] / show_chat_history_no
                    hist_df['page'] = hist_df['page'].astype(int)
                    hist_df['page'] = hist_df['page'] + 1

                    st.session_state['max_page'] = hist_df['page'].max()

                    filter_hist_df_2 = reset(hist_df[hist_df['page'] == st.session_state['page']])

                    for index, row in filter_hist_df_2.iterrows():
                        if st.session_state.chat_id != row['chat_id']:
                            chat_button_click = st.button(f"{row['user_text'][:30]}" + '...', key = row['chat_id'])
                            if chat_button_click:
                                st.session_state.messages = []
                                st.session_state.context = []
                                st.session_state.chat_id = row['chat_id']
                                st.session_state.turn_id = row['turn_id']
                                fil_hist_df = full_hist_df.copy()
                                fil_hist_df = reset(fil_hist_df[fil_hist_df['chat_id'] == row['chat_id']])
                                if fil_hist_df['engine'].values[-1] != 'Autogen':
                                    for index_2, row_2 in fil_hist_df.iterrows():
                                        st.session_state.messages.append({"role": "user", "content": row_2['user_text'], "raw_content": row_2['raw_input']})
                                        st.session_state.messages.append({"role": "assistant", "content": row_2['generative_text'], "chat_id": row_2['chat_id'], "turn_id":  row_2['turn_id'],
                                                                        "raw_content": row_2['raw_output'],
                                                                        })
                                        st.session_state.context.append({"role": "user", "content": row_2['raw_input']})
                                        st.session_state.context.append({"role": "system", "content": row_2['raw_output']})
                                else:
                                    history_list = literal_eval(fil_hist_df['history'].values[-1])
                                    chat_id = fil_hist_df['chat_id'].values[-1]
                                    user_list = ['user_proxy', 'decision_agent', 'loop_agent']
                                    for i, each_dict in enumerate(history_list):
                                        if each_dict['name'].lower() in user_list:
                                            st.session_state.messages.append({"role": "user", "content": each_dict['content'], "raw_content": ""})
                                            st.session_state.context.append({"role": "user", "content": ""})
                                            # st.chat_message("user", avatar = user_image).write(each_dict['content'])
                                        else:
                                            response = f"{each_dict['name']}: {each_dict['content']}"
                                            st.session_state.messages.append({"role": "assistant", "content": response, "chat_id": chat_id, "turn_id":  chat_id + '_' + str(i),
                                                                            "raw_content": "",
                                                                            })
                                            st.session_state.context.append({"role": "system", "content": ""})
                                            # st.chat_message("assistant", avatar = bot_image_2).write(response)

                    if 'max_page' not in st.session_state:
                        st.session_state['max_page'] = 10
                    if int(st.session_state['max_page']) > 1:
                        page = st.slider('Page No:', 1, int(st.session_state['max_page']), key = 'page')

        with st.expander("Change Password"):
            try:
                if authenticator.reset_password(st.session_state["username"], 'Reset password'):
                    with open('config.yaml', 'w') as file:
                        yaml.dump(config, file, default_flow_style=False)
                    st.success('Password modified successfully')
            except Exception as e:
                st.error(e)

        if st.session_state.username in admin_list:
            with st.expander("Register User"):
                try:
                    if authenticator.register_user('Register user', preauthorization=False):
                        with open('config.yaml', 'w') as file:
                            yaml.dump(config, file, default_flow_style=False)
                        st.success('User registered successfully')
                except Exception as e:
                    st.error(e)

        authenticator.logout(f"Logout ({st.session_state['username']})", 'main', key='unique_key')

    with st.chat_message("assistant", avatar = bot_image_2):
        # Create an empty message placeholder
        mp = st.empty()
        # Create a container for the message
        sl = mp.container()
        # Add a Markdown message describing the app
        sl.markdown(f"""
            Hi {st.session_state.name}! I am BotGPT, ready to provide assistance.
        """)

        existing_df = pd.DataFrame()

    mp = st.empty()

    # Initialize chat history if it doesn't exist
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "context" not in st.session_state:
        st.session_state.context = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        if message["role"] == "assistant":
            with st.chat_message(message["role"], avatar = bot_image_2):
                if dev_checkbox:
                    st.markdown(message["raw_content"])
                else:
                    st.markdown(message["content"])
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        feedback_options = ["...",
                                            "😄", 
                                            "🙂",
                                            "😐",
                                            "🙁",
                                            ]
                        feedback_radio_1 = st.radio(
                                            "ความพึงพอใจในการใช้งาน:",
                                            feedback_options,
                                            key='radio_1_' + str(random.random()) + message['turn_id'],
                                        )
                        if feedback_radio_1 != '...':
                            csv_file = f"data/feedback.csv"
                            file_exists = os.path.isfile(csv_file)
                            if not file_exists:
                                with open(csv_file, mode='a', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerow(['username','chat_id','turn_id','feedback_text'])
                            with open(csv_file, mode='a', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerow([st.session_state.username, st.session_state.chat_id, message['turn_id'], feedback_radio_1,])
                            st.success("Thanks! Your valuable feedback is updated in the database.")
                    with col2:
                        if context_radio == 'ข้อมูลประกาศ':
                            feedback_options = ["...",
                                                "คำตอบถูกต้องครบถ้วน",
                                                "คำตอบถูกต้องบางส่วน",
                                                "คำตอบไม่ถูกต้อง",
                                                "คำตอบไม่เกี่ยวข้องกับคำถาม"]
                        elif context_radio == 'Datacube':
                            feedback_options = ["...",
                                                "เลือก field ผิด",
                                                "เลือก field ถูกแต่ไม่ครบถ้วน",
                                                "เลือก field ถูกแต่ SQL ไม่ตอบโจทย์",
                                                "เลือก field ถูกแต่ SQL syntax ผิด",
                                                "ผลลัพธ์ถูกต้อง"]
                        feedback_radio_2 = st.radio(
                                            "ความถูกต้องของคำตอบ:",
                                            feedback_options,
                                            key='radio_2_' + str(random.random()) + message['turn_id'],
                                        )
                        if feedback_radio_2 != '...':
                            csv_file = f"data/feedback.csv"
                            file_exists = os.path.isfile(csv_file)
                            if not file_exists:
                                with open(csv_file, mode='a', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerow(['username','chat_id','turn_id','feedback_text'])
                            with open(csv_file, mode='a', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerow([st.session_state.username, st.session_state.chat_id, message['turn_id'], feedback_radio_2,])
                            st.success("Thanks! Your valuable feedback is updated in the database.")
                    if context_radio == 'ข้อมูลประกาศ':
                        with col3:
                            feedback_options = ["...",
                                                "ประกาศถูกต้อง",
                                                "ประกาศถูกต้องแต่ไม่ใช่ฉบับล่าสุด",
                                                "ประกาศถูกต้องแต่อ้างอิงผิดหน้า",
                                                "ประกาศไม่สามารถตอบคำถามได้ครบถ้วน",
                                                "ประกาศไม่เกี่ยวข้องกับคำถาม"]
                            feedback_radio_3 = st.radio(
                                                "ความถูกต้องของการอ้างอิงประกาศ:",
                                                feedback_options,
                                                key='radio_3_' + str(random.random()) + message['turn_id'],
                                            )
                            if feedback_radio_3 != '...':
                                csv_file = f"data/feedback.csv"
                                file_exists = os.path.isfile(csv_file)
                                if not file_exists:
                                    with open(csv_file, mode='a', newline='') as file:
                                        writer = csv.writer(file)
                                        writer.writerow(['username','chat_id','turn_id','feedback_text'])
                                with open(csv_file, mode='a', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerow([st.session_state.username, st.session_state.chat_id, message['turn_id'], feedback_radio_3,])
                                st.success("Thanks! Your valuable feedback is updated in the database.")
        else:
            with st.chat_message(message["role"], avatar = user_image):
                if dev_checkbox == False:
                    st.markdown(message["content"])
                else:
                    st.markdown(message["raw_content"])
                
    # Check if there's a user input prompt
    if dev_checkbox == False:
        # with st.chat_message("AI"):
        #     st.write("Hello 👋")
        if prompt := st.chat_input(placeholder="Kindly input your query or command for prompt assistance..."):
                if context_radio == 'ข้อมูลประกาศ':
                    # Display user input in the chat
                    st.chat_message("user", avatar = user_image).write(prompt)
                    with st.spinner('Thinking...'):
                        response_dict = get_response(prompt, temperature_value, context = st.session_state.context)
                        response = response_dict['response']
                        raw_input = response_dict['raw_input']
                        raw_output = response_dict['raw_output']
                        engine = response_dict['engine']
                        frontend_query_time = response_dict['frontend_query_time']
                        backend_query_time = response_dict['backend_query_time']

                        with st.chat_message("assistant", avatar = bot_image_2):
                            full_response = ""
                            message_placeholder = st.empty()
                            for chunk in response.split("\n"):
                                time.sleep(0.05)
                                message_placeholder.markdown(full_response + "▌")
                                full_response += chunk + "  \n" 
                                message_placeholder.markdown(full_response)

                        csv_file = f"data/{st.session_state.username}.csv"
                        file_exists = os.path.isfile(csv_file)
                        if not file_exists:
                            with open(csv_file, mode='a', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerow(['username','chat_id','turn_id','user_text','generative_text','raw_input','raw_output','engine','frontend_query_time','backend_query_time','history'])
                        with open(csv_file, mode='a', newline='', encoding = 'utf-8') as file:
                            writer = csv.writer(file)
                            current_time = str(datetime.datetime.now())
                            st.session_state.turn_id = current_time
                            writer.writerow([st.session_state.username, st.session_state.chat_id, st.session_state.turn_id, prompt, full_response, raw_input, raw_output, engine, frontend_query_time, backend_query_time, ""])
                        # Add the assistant's response to the chat history
                            st.session_state.messages.append({"role": "user", "content": prompt, "raw_content": raw_input})
                            st.session_state.messages.append({"role": "assistant", "content": full_response, "chat_id": st.session_state.chat_id, "turn_id":  st.session_state.turn_id,
                                                                "raw_content": raw_output,
                                                                })
                            st.session_state.context.append({"role": "user", "content": raw_input})
                            st.session_state.context.append({"role": "system", "content": raw_output})
                            st.rerun()

                elif context_radio == 'Datacube':
                    # Display user input in the chat
                    st.chat_message("user", avatar = user_image).write(prompt)
                    with st.spinner('Thinking...'):
                        response_dict = get_response_2(prompt, temperature_value, context = st.session_state.context)
                        response = response_dict['response']
                        raw_input = response_dict['raw_input']
                        raw_output = response_dict['raw_output']
                        engine = response_dict['engine']
                        frontend_query_time = response_dict['frontend_query_time']
                        backend_query_time = response_dict['backend_query_time']

                        with st.chat_message("assistant", avatar = bot_image_2):
                            full_response = ""
                            message_placeholder = st.empty()
                            for chunk in response.split("\n"):
                                time.sleep(0.05)
                                message_placeholder.markdown(full_response + "▌")
                                full_response += chunk + "  \n" 
                                message_placeholder.markdown(full_response)

                        csv_file = f"data/{st.session_state.username}.csv"
                        file_exists = os.path.isfile(csv_file)
                        if not file_exists:
                            with open(csv_file, mode='a', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerow(['username','chat_id','turn_id','user_text','generative_text','raw_input','raw_output','engine','frontend_query_time','backend_query_time','history'])
                        with open(csv_file, mode='a', newline='', encoding = 'utf-8') as file:
                            writer = csv.writer(file)
                            current_time = str(datetime.datetime.now())
                            st.session_state.turn_id = current_time
                            writer.writerow([st.session_state.username, st.session_state.chat_id, st.session_state.turn_id, prompt, full_response, raw_input, raw_output, engine, frontend_query_time, backend_query_time, ""])
                        # Add the assistant's response to the chat history
                        st.session_state.messages.append({"role": "user", "content": prompt, "raw_content": raw_input})
                        st.session_state.messages.append({"role": "assistant", "content": full_response, "chat_id": st.session_state.chat_id, "turn_id":  st.session_state.turn_id,
                                                            "raw_content": raw_output,
                                                            })
                        st.session_state.context.append({"role": "user", "content": raw_input})
                        st.session_state.context.append({"role": "system", "content": raw_output})
                        st.rerun()

                elif context_radio == 'Autogen':
                    with st.spinner('Thinking...'):
                        response_dict = get_response_3(prompt, history = st.session_state.history)
                        st.session_state.history = response_dict['history']
                        full_response = response_dict['response']['content']
                        raw_input = ""
                        raw_output = ""
                        engine = "Autogen"
                        frontend_query_time = response_dict['frontend_query_time']
                        backend_query_time = 0
                        history_list = response_dict['history']
                        user_list = ['user_proxy', 'decision_agent', 'loop_agent']
                        for i, each_dict in enumerate(history_list):
                            if each_dict['name'].lower() in user_list:
                                st.chat_message("user", avatar = user_image).write(each_dict['content'])
                                st.session_state.messages.append({"role": "user", "content": each_dict['content'], "raw_content": ""})
                                st.session_state.context.append({"role": "user", "content": ""})
                            else:
                                response = f"{each_dict['name']}: {each_dict['content']}"
                                with st.chat_message("assistant", avatar = bot_image_2):
                                    full_response = ""
                                    message_placeholder = st.empty()
                                    for chunk in response.split("\n"):
                                        time.sleep(0.05)
                                        message_placeholder.markdown(full_response + "▌")
                                        full_response += chunk + "  \n" 
                                        message_placeholder.markdown(full_response)
                                st.session_state.messages.append({"role": "assistant", "content": response, "chat_id": st.session_state.chat_id, "turn_id":  st.session_state.chat_id + '_' + str(i),
                                                                "raw_content": "",
                                                                })
                                st.session_state.context.append({"role": "system", "content": ""})
                        csv_file = f"data/{st.session_state.username}.csv"
                        file_exists = os.path.isfile(csv_file)
                        if not file_exists:
                            with open(csv_file, mode='a', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerow(['username','chat_id','turn_id','user_text','generative_text','raw_input','raw_output','engine','frontend_query_time','backend_query_time','history'])
                        with open(csv_file, mode='a', newline='', encoding = 'utf-8') as file:
                            writer = csv.writer(file)
                            current_time = str(datetime.datetime.now())
                            st.session_state.turn_id = current_time
                            writer.writerow([st.session_state.username, st.session_state.chat_id, st.session_state.turn_id, prompt, full_response, raw_input, raw_output, engine, frontend_query_time, backend_query_time, response_dict['history'] ])
                        st.rerun()

elif st.session_state["authentication_status"] == False:
    st.error("Username/password is incorrect. If you encounter any issues related to user login, please contact Thanatchon Chongmankhong at thanatcc@bot.or.th.")
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password. If you encounter any issues related to user login, please contact Thanatchon Chongmankhong at thanatcc@bot.or.th.')