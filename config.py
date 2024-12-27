import os

telegram_token = ""

data_base = os.path.join(os.path.dirname(__file__), 'database.db')

group_id_for_notifications = -01111

start_status = 0
phone_number_status = 1
app_submit_status = 2
request_consult_status = 3
ask_question_status = 4
