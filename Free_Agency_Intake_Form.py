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
st.image("https://cdn.mississippitoday.org/uploads/2017/07/22030122/AP_882940498833-1200x960.jpg", use_container_width=True)

st.markdown("**Free Agency Intake Form**")  # Bold

team_names = [" ","Dominators", "The Dude", "Hello Kitty", "MidKnight Train", "BEATDOWN CREW", "Crusaders",
                "Renegades", "Theheartbreakkid", "BENCHWARMERS", "Dreamteam", "Wranglers", "Conquerors" ] 
options = ['Bid', 'Cut', 'Trade']
list_of_transactions = []
notes = None
df_transactions = pd.DataFrame(columns=['Team Name', 'Player', 'Action', 'Salary', 'Trade Notes', 'Timestamp'])


#SELECT YOUR TEAM NAME
##--------------------------------------
st.markdown("<span style='color:red; font-size:14px;'># REMEMBER TO SELECT YOUR TEAM NAME BELOW #</span>", unsafe_allow_html=True)
selected_option_name = st.selectbox("Please select your team name", team_names)

selected_option_type = st.radio(
    "Please select the transaction type",
    options,
    horizontal=True,
    key="first_trans"
)

if selected_option_type == "Bid":
    user_input_player = st.text_input("Please type the player name",key='first_selection_player')
    user_input_salary = st.text_input("Please input your bid",key='first_salary')
    trade_notes = None

elif selected_option_type == "Cut":
    user_input_player = st.text_input("Please type the player name",key='first_selection_player_cut')
    user_input_salary = 0
    trade_notes = None

elif selected_option_type == "Trade":
    user_input_player = None
    user_input_salary = 0
    trade_notes = st.text_area(
        "Trade Notes (required)",
        placeholder="Example: Trading Jacory Croskey-Merritt to Crusaders for Jahymr Gibbs",
        key="trade_notes"
    )


#first_entry = st.write("You entered: ({}, {}, {}, {})".format(selected_option_name,user_input_player,selected_option_type,user_input_salary))
list1 = [selected_option_name, user_input_player,
            selected_option_type, user_input_salary, trade_notes, current_dt]
temp_df = pd.DataFrame([list1], columns=['Team Name', 'Player', 'Action', 'Salary', 'Trade Notes', 'Timestamp'])
df_transactions = pd.concat([df_transactions, temp_df], ignore_index=True)

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

#Add Player Transaction
#-------------------------------------
if st.button("+Add Player Transaction", help="Click If You Need to Bid/Cut Another Player",type="secondary",key='first_player_add'):
    st.session_state.button_clicked = True

if st.session_state.button_clicked:

    selected_option_type2 = st.radio(
    "Please select the transaction type",
    options,
    horizontal=True,
    key="second_trans"
    )

    if selected_option_type2 == "Bid":
        user_input_player2 = st.text_input("Please type the player name",key='second_selection_player')
        user_input_salary2 = st.text_input("Please input your bid",key='second_salary')
        trade_notes2 = None

    elif selected_option_type2 == "Cut":
        user_input_player2 = st.text_input("Please type the player name",key='second_selection_player_cut')
        user_input_salary2 = 0
        trade_notes2 = None

    elif selected_option_type2 == "Trade":
        user_input_player2 = None
        user_input_salary2 = 0
        trade_notes2 = st.text_area(
        "Trade Notes (required)",
        placeholder="Example: Trading Jacory Croskey-Merritt to Crusaders for Jahymr Gibbs",
        key="trade_notes2"
    )


    list2 = [selected_option_name, user_input_player2,
            selected_option_type2,user_input_salary2,trade_notes2,current_dt]
    temp_df = pd.DataFrame([list2], columns=['Team Name', 'Player', 'Action', 'Salary', 'Trade Notes','Timestamp'])
    df_transactions = pd.concat([df_transactions, temp_df], ignore_index=True)

    #Add Player Transaction 2
    #---------------------------------
    if "button_clicked2" not in st.session_state:
        st.session_state.button_clicked2 = False
    
    if st.button("+Add Player Transaction", help="Click If You Need to Bid/Cut Another Player",type="secondary",key='second_player_add'):
        st.session_state.button_clicked2 = True
    
    if st.session_state.button_clicked2:

        selected_option_type3 = st.radio(
            "Please select the transaction type",
            options,
            horizontal=True,
            key="third_trans"
            )
        
        if selected_option_type3 == "Bid":
                user_input_player3 = st.text_input("Please type the player name",key='third_selection_player')
                user_input_salary3 = st.text_input("Please input your bid",key='third_salary')
                trade_notes3 = None
        
        elif selected_option_type3 == "Cut":
                user_input_player3 = st.text_input("Please type the player name",key='third_selection_player_cut')
                user_input_salary3 = 0
                trade_notes3 = None
        
        elif selected_option_type3 == "Trade":
                user_input_player3 = None
                user_input_salary3 = 0
                trade_notes3 = st.text_area(
                "Trade Notes (required)",
                placeholder="Example: Trading Jacory Croskey-Merritt to Crusaders for Jahymr Gibbs",
                key="trade_notes3"
            )


        list3 = [selected_option_name, user_input_player3,
            selected_option_type3,user_input_salary3,trade_notes3,current_dt]
        temp_df = pd.DataFrame([list3], columns=['Team Name', 'Player', 'Action', 'Salary', 'Trade Notes', 'Timestamp'])
        df_transactions = pd.concat([df_transactions, temp_df], ignore_index=True)


        #Add Player Transaction 3
        #---------------------------------
        if "button_clicked3" not in st.session_state:
            st.session_state.button_clicked3 = False
    
        if st.button("+Add Player Transaction", help="Click If You Need to Bid/Cut Another Player",type="secondary",key='third_player_add'):
            st.session_state.button_clicked3 = True
    
        if st.session_state.button_clicked3:

            selected_option_type4 = st.radio(
                "Please select the transaction type",
                options,
                horizontal=True,
                key="fourth_trans"
                )
            
            if selected_option_type4 == "Bid":
                user_input_player4 = st.text_input("Please type the player name",key='fourth_selection_player')
                user_input_salary4 = st.text_input("Please input your bid",key='fourth_salary')
                trade_notes4 = None
            
            elif selected_option_type4 == "Cut":
                user_input_player4 = st.text_input("Please type the player name",key='fourth_selection_player_cut')
                user_input_salary4 = 0
                trade_notes4 = None
            
            elif selected_option_type4 == "Trade":
                user_input_player4 = None
                user_input_salary4 = 0
                trade_notes4 = st.text_area(
                "Trade Notes (required)",
                placeholder="Example: Trading Jacory Croskey-Merritt to Crusaders for Jahymr Gibbs",
                key="trade_notes4"
                )


            list4 = [selected_option_name, user_input_player4,
            selected_option_type4,user_input_salary4,trade_notes4,current_dt]
            temp_df = pd.DataFrame([list4], columns=['Team Name', 'Player', 'Action', 'Salary', 'Trade Notes', 'Timestamp'])
            df_transactions = pd.concat([df_transactions, temp_df], ignore_index=True)


            #Add Player Transaction 4
            #---------------------------------
            if "button_clicked4" not in st.session_state:
                st.session_state.button_clicked4 = False
    
            if st.button("+Add Player Transaction", help="Click If You Need to Bid/Cut Another Player",type="secondary",key='fourth_player_add'):
                st.session_state.button_clicked4 = True
    
            if st.session_state.button_clicked4:

                selected_option_type5 = st.radio(
                    "Please select the transaction type",
                    options,
                    horizontal=True,
                    key="fifth_trans"
                    )
                
                if selected_option_type5 == "Bid":
                    user_input_player5 = st.text_input("Please type the player name",key='fifth_selection_player')
                    user_input_salary5 = st.text_input("Please input your bid",key='fifth_salary')
                    trade_notes5 = None
                
                elif selected_option_type5 == "Cut":
                    user_input_player5 = st.text_input("Please type the player name",key='fifth_selection_player_cut')
                    user_input_salary5 = 0
                    trade_notes5 = None
                
                elif selected_option_type5 == "Trade":
                    user_input_player5 = None
                    user_input_salary5 = 0
                    trade_notes5 = st.text_area(
                    "Trade Notes (required)",
                    placeholder="Example: Trading Jacory Croskey-Merritt to Crusaders for Jahymr Gibbs",
                    key="trade_notes5"
                    )

                list5 = [selected_option_name, user_input_player5,
                selected_option_type5,user_input_salary5,trade_notes5,current_dt]
                temp_df = pd.DataFrame([list5], columns=['Team Name', 'Player', 'Action', 'Salary', 'Trade Notes', 'Timestamp'])
                df_transactions = pd.concat([df_transactions, temp_df], ignore_index=True)


                
                #Add Player Transaction 5
                #---------------------------------
                if "button_clicked5" not in st.session_state:
                    st.session_state.button_clicked5 = False
    
                if st.button("+Add Player Transaction", help="Click If You Need to Bid/Cut Another Player",type="secondary",key='fifth_player_add'):
                    st.session_state.button_clicked5 = True
    
                if st.session_state.button_clicked5:

                    selected_option_type6 = st.radio(
                        "Please select the transaction type",
                        options,
                        horizontal=True,
                        key="sixth_trans"
                        )
                    
                    if selected_option_type6 == "Bid":
                        user_input_player6 = st.text_input("Please type the player name",key='sixth_selection_player')
                        user_input_salary6 = st.text_input("Please input your bid",key='sixth_salary')
                        trade_notes6 = None
                    
                    elif selected_option_type6 == "Cut":
                        user_input_player6 = st.text_input("Please type the player name",key='sixth_selection_player_cut')
                        user_input_salary6 = 0
                        trade_notes6 = None
                    
                    elif selected_option_type6 == "Trade":
                        user_input_player6 = None
                        user_input_salary6 = 0
                        trade_notes6 = st.text_area(
                        "Trade Notes (required)",
                        placeholder="Example: Trading Jacory Croskey-Merritt to Crusaders for Jahymr Gibbs",
                        key="trade_notes6"
                        )



                    list6 = [selected_option_name, user_input_player6,
                    selected_option_type6,user_input_salary6,trade_notes6,current_dt]
                    temp_df = pd.DataFrame([list6], columns=['Team Name', 'Player', 'Action', 'Salary', 'Trade Notes', 'Timestamp'])
                    df_transactions = pd.concat([df_transactions, temp_df], ignore_index=True)

                    #Add Player Transaction 6
                    #---------------------------------
                    if "button_clicked6" not in st.session_state:
                        st.session_state.button_clicked6 = False
    
                    if st.button("+Add Player Transaction", help="Click If You Need to Bid/Cut Another Player",type="secondary",key='sixth_player_add'):
                        st.session_state.button_clicked6 = True
    
                    if st.session_state.button_clicked6:

                        selected_option_type7 = st.radio(
                            "Please select the transaction type",
                            options,
                            horizontal=True,
                            key="seventh_trans"
                            )
                        
                        if selected_option_type7 == "Bid":
                            user_input_player7 = st.text_input("Please type the player name",key='seventh_selection_player')
                            user_input_salary7 = st.text_input("Please input your bid",key='seventh_salary')
                            trade_notes7 = None
                        
                        elif selected_option_type7 == "Cut":
                            user_input_player7 = st.text_input("Please type the player name",key='seventh_selection_player_cut')
                            user_input_salary7 = 0
                            trade_notes7 = None
                        
                        elif selected_option_type7 == "Trade":
                            user_input_player7 = None
                            user_input_salary7 = 0
                            trade_notes7 = st.text_area(
                            "Trade Notes (required)",
                            placeholder="Example: Trading Jacory Croskey-Merritt to Crusaders for Jahymr Gibbs",
                            key="trade_notes7"
                            )

                        list7 = [selected_option_name, user_input_player7,
                        selected_option_type7,user_input_salary7,trade_notes7,current_dt]
                        temp_df = pd.DataFrame([list7], columns=['Team Name', 'Player', 'Action', 'Salary', 'Trade Notes', 'Timestamp'])
                        df_transactions = pd.concat([df_transactions, temp_df], ignore_index=True)

                    
                        #Add Player Transaction 7
                        #---------------------------------
                        if "button_clicked7" not in st.session_state:
                            st.session_state.button_clicked7 = False
    
                        if st.button("+Add Player Transaction", help="Click If You Need to Bid/Cut Another Player",type="secondary",key='sev_player_add'):
                            st.session_state.button_clicked7 = True
    
                        if st.session_state.button_clicked7:

                            selected_option_type8 = st.radio(
                                "Please select the transaction type",
                                options,
                                horizontal=True,
                                key="eighth_trans"
                                )
                        
                            if selected_option_type8 == "Bid":
                                user_input_player8 = st.text_input("Please type the player name",key='eighth_selection_player')
                                user_input_salary8 = st.text_input("Please input your bid",key='eighth_salary')
                                trade_notes8 = None
                        
                            elif selected_option_type8 == "Cut":
                                user_input_player8 = st.text_input("Please type the player name",key='eighth_selection_player_cut')
                                user_input_salary8 = 0
                                trade_notes8 = None
                        
                            elif selected_option_type8 == "Trade":
                                user_input_player8 = None
                                user_input_salary8 = 0
                                trade_notes8 = st.text_area(
                                "Trade Notes (required)",
                                placeholder="Example: Trading Jacory Croskey-Merritt to Crusaders for Jahymr Gibbs",
                                key="trade_notes8"
                                )

                            list8 = [selected_option_name, user_input_player8,
                            selected_option_type8,user_input_salary8,trade_notes8,current_dt]
                            temp_df = pd.DataFrame([list8], columns=['Team Name', 'Player', 'Action', 'Salary', 'Trade Notes', 'Timestamp'])
                            df_transactions = pd.concat([df_transactions, temp_df], ignore_index=True)

                            #Add Player Transaction 8
                            #---------------------------------
                            if "button_clicked8" not in st.session_state:
                                st.session_state.button_clicked8 = False
    
                            if st.button("+Add Player Transaction", help="Click If You Need to Bid/Cut Another Player",type="secondary",key='eighth_player_add'):
                                st.session_state.button_clicked8 = True
    
                            if st.session_state.button_clicked8:

                                selected_option_type9 = st.radio(
                                    "Please select the transaction type",
                                    options,
                                    horizontal=True,
                                    key="ninth_trans"
                                    )
                        
                                if selected_option_type9 == "Bid":
                                    user_input_player9 = st.text_input("Please type the player name",key='ninth_selection_player')
                                    user_input_salary9 = st.text_input("Please input your bid",key='ninth_salary')
                                    trade_notes9 = None
                        
                                elif selected_option_type9 == "Cut":
                                    user_input_player9 = st.text_input("Please type the player name",key='ninth_selection_player_cut')
                                    user_input_salary9 = 0
                                    trade_notes9 = None
                        
                                elif selected_option_type9 == "Trade":
                                    user_input_player9 = None
                                    user_input_salary9 = 0
                                    trade_notes9 = st.text_area(
                                    "Trade Notes (required)",
                                    placeholder="Example: Trading Jacory Croskey-Merritt to Crusaders for Jahymr Gibbs",
                                    key="trade_notes9"
                                    )

                                list9 = [selected_option_name, user_input_player9,
                                selected_option_type9,user_input_salary9,trade_notes9,current_dt]
                                temp_df = pd.DataFrame([list9], columns=['Team Name', 'Player', 'Action', 'Salary', 'Trade Notes', 'Timestamp'])
                                df_transactions = pd.concat([df_transactions, temp_df], ignore_index=True)

                                #Add Player Transaction 9
                                #---------------------------------
                                if "button_clicked9" not in st.session_state:
                                    st.session_state.button_clicked9 = False
    
                                if st.button("+Add Player Transaction", help="Click If You Need to Bid/Cut Another Player",type="secondary",key='ninth_player_add'):
                                    st.session_state.button_clicked9 = True
    
                                if st.session_state.button_clicked9:

                                    selected_option_type10 = st.radio(
                                        "Please select the transaction type",
                                        options,
                                        horizontal=True,
                                        key="tenth_trans"
                                        )
                        
                                    if selected_option_type10 == "Bid":
                                        user_input_player10 = st.text_input("Please type the player name",key='tenth_selection_player')
                                        user_input_salary10 = st.text_input("Please input your bid",key='tenth_salary')
                                        trade_notes10 = None
                        
                                    elif selected_option_type10 == "Cut":
                                        user_input_player10 = st.text_input("Please type the player name",key='tenth_selection_player_cut')
                                        user_input_salary10 = 0
                                        trade_notes10 = None
                        
                                    elif selected_option_type10 == "Trade":
                                        user_input_player10 = None
                                        user_input_salary10 = 0
                                        trade_notes10 = st.text_area(
                                        "Trade Notes (required)",
                                        placeholder="Example: Trading Jacory Croskey-Merritt to Crusaders for Jahymr Gibbs",
                                        key="trade_notes10"
                                        )

                                    list10 = [selected_option_name, user_input_player10,
                                    selected_option_type10,user_input_salary10,trade_notes10,current_dt]
                                    temp_df = pd.DataFrame([list10], columns=['Team Name', 'Player', 'Action', 'Salary', 'Trade Notes', 'Timestamp'])
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
    df_transactions["Timestamp"] = df_transactions["Timestamp"].astype("string")
    df_list = df_transactions.values.tolist()
    sheet.insert_rows(df_list, 1)

    st.success("Data inserted successfully!")

st.write(df_transactions)

st.markdown("<span style='color:red; font-size:12px;'>This form allows for 10 total transactions at a time</span>", unsafe_allow_html=True)

st.image("https://img.apmcdn.org/bbdbc1df7f5802e5cd2ced5e75ed432e509a95f5/uncropped/889525-20250109-foreman-1200.png",use_container_width=True)
