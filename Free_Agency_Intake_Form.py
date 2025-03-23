import streamlit as st
import os
import pandas as pd
from datetime import datetime
import pytz
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials

est_tz = pytz.timezone("America/New_York")  # Change this to your timezone
current_dt = datetime.now(est_tz)
current_dt = current_dt.strftime("%Y-%m-%d %H:%M")
st.title(':crossed_swords::shield: Strength and Honor :shield::crossed_swords:')
st.markdown("**Free Agency Intake Form**")  # Bold

team_names = ["The Dude", "Crusaders", "BEATDOWN CREW", "BENCHWARMERS", "Dominators", "MidKnight Train",
                "Conquerors", "Dreamteam", "Football Mama", "Renegades", "Wranglers", "Theheartbreakkid" ] 
options = ['Bid', 'Cut']
list_of_transactions = []
df_transactions = pd.DataFrame(columns=['Team Name', 'Player', 'Action', 'Salary', 'Timestamp'])


#SELECT YOUR TEAM NAME
##--------------------------------------
selected_option_name = st.selectbox("Please select your team name", team_names)


user_input_player = st.text_input("Please type the player name",key='first_selection_player')
selected_option_type = st.selectbox("Please select the transaction type", options,key='first_trans')


if selected_option_type == 'Bid':
    user_input_salary = st.text_input("Please input your bid",key='first_salary')
else:
    user_input_salary = 0
    st.write("Please Submit Below")


#first_entry = st.write("You entered: ({}, {}, {}, {})".format(selected_option_name,user_input_player,selected_option_type,user_input_salary))
list1 = [selected_option_name, user_input_player,
            selected_option_type,user_input_salary, current_dt]
temp_df = pd.DataFrame([list1], columns=['Team Name', 'Player', 'Action', 'Salary', 'DateTime'])
df_transactions = pd.concat([df_transactions, temp_df], ignore_index=True)

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

#Add Player Transaction
#-------------------------------------
if st.button("+Add Player Transaction", help="Click If You Need to Bid/Cut Another Player",type="secondary",key='first_player_add'):
    st.session_state.button_clicked = True

if st.session_state.button_clicked:
    user_input_player2 = st.text_input("Please type the player name",key='second_selection_player')
    selected_option_type2 = st.selectbox("Please select the transaction type", options, key='second_trans')

    if selected_option_type2 == 'Bid':
        user_input_salary2 = st.text_input("Please input your bid",key='second_salary')
        #st.session_state.show_input = True
    else:
        user_input_salary2 = 0
        st.write('Please Submit Below')

    list2 = [selected_option_name, user_input_player2,
            selected_option_type2,user_input_salary2,current_dt]
    temp_df = pd.DataFrame([list2], columns=['Team Name', 'Player', 'Action', 'Salary', 'DateTime'])
    df_transactions = pd.concat([df_transactions, temp_df], ignore_index=True)

    #Add Player Transaction 2
    #---------------------------------
    if "button_clicked2" not in st.session_state:
        st.session_state.button_clicked2 = False
    
    if st.button("+Add Player Transaction", help="Click If You Need to Bid/Cut Another Player",type="secondary",key='second_player_add'):
        st.session_state.button_clicked2 = True
    
    if st.session_state.button_clicked2:
        user_input_player3 = st.text_input("Please type the player name",key='third_selection_player')
        selected_option_type3 = st.selectbox("Please select the transaction type", options, key='third_trans')

        if selected_option_type3 == 'Bid':
            user_input_salary3 = st.text_input("Please input your bid",key='third_salary')
            #st.session_state.show_input = True
        else:
            user_input_salary3 = 0
            st.write('Please Submit Below')

        list3 = [selected_option_name, user_input_player3,
            selected_option_type3,user_input_salary3,current_dt]
        temp_df = pd.DataFrame([list3], columns=['Team Name', 'Player', 'Action', 'Salary', 'DateTime'])
        df_transactions = pd.concat([df_transactions, temp_df], ignore_index=True)


        #Add Player Transaction 3
        #---------------------------------
        if "button_clicked3" not in st.session_state:
            st.session_state.button_clicked3 = False
    
        if st.button("+Add Player Transaction", help="Click If You Need to Bid/Cut Another Player",type="secondary",key='third_player_add'):
            st.session_state.button_clicked3 = True
    
        if st.session_state.button_clicked3:
            user_input_player4 = st.text_input("Please type the player name",key='fourth_selection_player')
            selected_option_type4 = st.selectbox("Please select the transaction type", options, key='fourth_trans')

            if selected_option_type4 == 'Bid':
                user_input_salary4 = st.text_input("Please input your bid",key='fourth_salary')
                #st.session_state.show_input = True
            else:
                user_input_salary4 = 0
                st.write('Please Submit Below')

            list4 = [selected_option_name, user_input_player4,
            selected_option_type4,user_input_salary4,current_dt]
            temp_df = pd.DataFrame([list4], columns=['Team Name', 'Player', 'Action', 'Salary', 'DateTime'])
            df_transactions = pd.concat([df_transactions, temp_df], ignore_index=True)


            #Add Player Transaction 4
            #---------------------------------
            if "button_clicked4" not in st.session_state:
                st.session_state.button_clicked4 = False
    
            if st.button("+Add Player Transaction", help="Click If You Need to Bid/Cut Another Player",type="secondary",key='fourth_player_add'):
                st.session_state.button_clicked4 = True
    
            if st.session_state.button_clicked4:
                user_input_player5 = st.text_input("Please type the player name",key='fifth_selection_player')
                selected_option_type5 = st.selectbox("Please select the transaction type", options, key='fifth_trans')

                if selected_option_type5 == 'Bid':
                    user_input_salary5 = st.text_input("Please input your bid",key='fifth_salary')
                    #st.session_state.show_input = True
                else:
                    user_input_salary5 = 0
                    st.write('Please Submit Below')

                list5 = [selected_option_name, user_input_player5,
                selected_option_type5,user_input_salary5,current_dt]
                temp_df = pd.DataFrame([list5], columns=['Team Name', 'Player', 'Action', 'Salary', 'DateTime'])
                df_transactions = pd.concat([df_transactions, temp_df], ignore_index=True)


                
                #Add Player Transaction 5
                #---------------------------------
                if "button_clicked5" not in st.session_state:
                    st.session_state.button_clicked5 = False
    
                if st.button("+Add Player Transaction", help="Click If You Need to Bid/Cut Another Player",type="secondary",key='fifth_player_add'):
                    st.session_state.button_clicked5 = True
    
                if st.session_state.button_clicked5:
                    user_input_player6 = st.text_input("Please type the player name",key='sixth_selection_player')
                    selected_option_type6 = st.selectbox("Please select the transaction type", options, key='sixth_trans')

                    if selected_option_type6 == 'Bid':
                        user_input_salary6 = st.text_input("Please input your bid",key='sixth_salary')
                        #st.session_state.show_input = True
                    else:
                        user_input_salary6 = 0
                        st.write('Please Submit Below')

                    list6 = [selected_option_name, user_input_player6,
                    selected_option_type6,user_input_salary6,current_dt]
                    temp_df = pd.DataFrame([list6], columns=['Team Name', 'Player', 'Action', 'Salary', 'DateTime'])
                    df_transactions = pd.concat([df_transactions, temp_df], ignore_index=True)

                    #Add Player Transaction 6
                    #---------------------------------
                    if "button_clicked6" not in st.session_state:
                        st.session_state.button_clicked6 = False
    
                    if st.button("+Add Player Transaction", help="Click If You Need to Bid/Cut Another Player",type="secondary",key='sixth_player_add'):
                        st.session_state.button_clicked6 = True
    
                    if st.session_state.button_clicked6:
                        user_input_player7 = st.text_input("Please type the player name",key='sev_selection_player')
                        selected_option_type7 = st.selectbox("Please select the transaction type", options, key='sev_trans')

                        if selected_option_type7 == 'Bid':
                            user_input_salary7 = st.text_input("Please input your bid",key='sev_salary')
                            #st.session_state.show_input = True
                        else:
                            user_input_salary7 = 0
                            st.write('Please Submit Below')

                        list7 = [selected_option_name, user_input_player7,
                        selected_option_type7,user_input_salary7,current_dt]
                        temp_df = pd.DataFrame([list7], columns=['Team Name', 'Player', 'Action', 'Salary', 'DateTime'])
                        df_transactions = pd.concat([df_transactions, temp_df], ignore_index=True)

                    
                        #Add Player Transaction 7
                        #---------------------------------
                        if "button_clicked7" not in st.session_state:
                            st.session_state.button_clicked7 = False
    
                        if st.button("+Add Player Transaction", help="Click If You Need to Bid/Cut Another Player",type="secondary",key='sev_player_add'):
                            st.session_state.button_clicked7 = True
    
                        if st.session_state.button_clicked7:
                            user_input_player8 = st.text_input("Please type the player name",key='eigth_selection_player')
                            selected_option_type8 = st.selectbox("Please select the transaction type", options, key='eigth_trans')

                            if selected_option_type8 == 'Bid':
                                user_input_salary8 = st.text_input("Please input your bid",key='eigth_salary')
                                #st.session_state.show_input = True
                            else:
                                user_input_salary8 = 0
                                st.write('Please Submit Below')

                            list8 = [selected_option_name, user_input_player8,
                            selected_option_type8,user_input_salary8,current_dt]
                            temp_df = pd.DataFrame([list8], columns=['Team Name', 'Player', 'Action', 'Salary', 'DateTime'])
                            df_transactions = pd.concat([df_transactions, temp_df], ignore_index=True)

                            #Add Player Transaction 8
                            #---------------------------------
                            if "button_clicked8" not in st.session_state:
                                st.session_state.button_clicked8 = False
    
                            if st.button("+Add Player Transaction", help="Click If You Need to Bid/Cut Another Player",type="secondary",key='eighth_player_add'):
                                st.session_state.button_clicked8 = True
    
                            if st.session_state.button_clicked8:
                                user_input_player9 = st.text_input("Please type the player name",key='ninth_selection_player')
                                selected_option_type9 = st.selectbox("Please select the transaction type", options, key='ninth_trans')

                                if selected_option_type9 == 'Bid':
                                    user_input_salary9 = st.text_input("Please input your bid",key='ninth_salary')
                                    #st.session_state.show_input = True
                                else:
                                    user_input_salary9 = 0
                                    st.write('Please Submit Below')

                                list9 = [selected_option_name, user_input_player9,
                                selected_option_type9,user_input_salary9,current_dt]
                                temp_df = pd.DataFrame([list9], columns=['Team Name', 'Player', 'Action', 'Salary', 'DateTime'])
                                df_transactions = pd.concat([df_transactions, temp_df], ignore_index=True)

                                #Add Player Transaction 9
                                #---------------------------------
                                if "button_clicked9" not in st.session_state:
                                    st.session_state.button_clicked9 = False
    
                                if st.button("+Add Player Transaction", help="Click If You Need to Bid/Cut Another Player",type="secondary",key='ninth_player_add'):
                                    st.session_state.button_clicked9 = True
    
                                if st.session_state.button_clicked9:
                                    user_input_player10 = st.text_input("Please type the player name",key='tenth_selection_player')
                                    selected_option_type10 = st.selectbox("Please select the transaction type", options, key='tenth_trans')

                                    if selected_option_type10 == 'Bid':
                                        user_input_salary10 = st.text_input("Please input your bid",key='tenth_salary')
                                        #st.session_state.show_input = True
                                    else:
                                        user_input_salary10 = 0
                                        st.write('Please Submit Below')

                                    list10 = [selected_option_name, user_input_player10,
                                    selected_option_type10,user_input_salary10,current_dt]
                                    temp_df = pd.DataFrame([list10], columns=['Team Name', 'Player', 'Action', 'Salary', 'DateTime'])
                                    df_transactions = pd.concat([df_transactions, temp_df], ignore_index=True)
 




if "button_clicked_sub" not in st.session_state:
    st.session_state.button_clicked_sub = False

if st.button("Submit!",type="primary",help="Submit When You're Done With All Your Transactions", key="first_submit"):
    st.session_state.button_clicked_sub = True

    # Define the scope (OLD)
    #scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    #Define the scope (NEW)
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets","https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    #PROCESS FOR RUNNING ON LOCAL MACHINE
    # Path to your downloaded credentials.json file
    #creds = ServiceAccountCredentials.from_json_keyfile_name('google_credentials.json', scope)
    # Authenticate and initialize gspread client
    #client = gspread.authorize(creds)

    #NEW PROCESS
    # Set the path to your credentials file
    # Load credentials from Streamlit secrets

    # Load credentials and specify the scope
    if "gcp_service_account" in st.secrets:
        credentials = Credentials.from_service_account_info(
            st.secrets["gcp_service_account"], scopes=SCOPES
        )
        client = gspread.authorize(credentials)
        st.success("Successfully authenticated with Google Sheets!")
    else:
        st.error("Google credentials not found! Please check Streamlit Secrets.")

    #OLD SCOPES LOGIC
    #credentials = Credentials.from_service_account_info(st.secrets["gcp_service_account"])
    #client = gspread.authorize(credentials)


    # Open a Google Sheet by name
    sheet = client.open("Free_Agency").sheet1  # Use sheet1 or specify a sheet by name

    # Insert data by appending it to the next available row
    df_transactions["DateTime"] = df_transactions["DateTime"].astype("string")
    df_list = df_transactions.values.tolist()
    sheet.insert_rows(df_list, 1)

    st.success("Data inserted successfully!")

st.write(df_transactions)

st.markdown("<span style='color:red; font-size:12px;'>This form allows for 10 total transactions at a time</span>", unsafe_allow_html=True)
st.markdown("<span style='color:red; font-size:12px;'>Please send all trades to roger.commish.goodell@gmail.com</span>", unsafe_allow_html=True)
