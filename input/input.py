import threading
import requests
import pandas as pd
import os
import pymysql
from dbutils.pooled_db import PooledDB
import time
from datetime import datetime
import logging
from dotenv import load_dotenv
from packet_info_schema import PacketInfoSchema

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
URL = os.getenv('POST_URL')

packet_info_schema = PacketInfoSchema()
current_index = {}

pool = PooledDB(
    creator=pymysql,  
    maxconnections=20,  
    mincached=5,  
    maxcached=15,  
    maxusage=None,  
    blocking=True,  
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME'),
    charset='utf8mb4'
)

def send_request(data, filename):
    time.sleep(0.001)
    try:
        db_connection = pool.connection() 
        if filename not in current_index:
            current_index[filename] = 0

        if current_index[filename] < len(data):
            current_row = data.iloc[current_index[filename]]  
            current_index[filename] += 1
        else:
            logging.info(f"All rows have been processed for {filename}")
            return

        ip = current_row['srcip']  
        port = str(current_row['sport'])  
        input_id = current_row['index']  
        label = current_row['category_label'] 
        timestamp = datetime.now().isoformat()

        body = {'timestamp': timestamp}

        with db_connection.cursor() as cursor:
            user_labels = ['WEB_ATTACK_BRUTE_FORCE', 'FTP_PATATOR', 'SSH_PATATOR']
            script_labels = ['WEB_ATTACK_XSS', 'WEB_ATTACK_SQL_INJECTION', 'BACKDOOR', 'INFILTRATION', 'SHELLCODE', 'EXPLOITS', 'GENERIC']
            restricted_script_labels = ['EXPLOITS', 'GENERIC']

            if label in user_labels:

                cursor.execute("SELECT username, password FROM dummy_users WHERE type = %s", (label,))

                result = cursor.fetchone()
                if result:
                    body.update({
                        'username': result['username'],
                        'password': result['password']
                    })


            elif label in script_labels:
                if label in restricted_script_labels:

                    cursor.execute("SELECT content FROM dummy_scripts WHERE type != 'WEB_ATTACK_SQL_INJECTION'")

                else:
                    cursor.execute("SELECT content FROM dummy_scripts WHERE type = %s", (label,))

                result = cursor.fetchone()
                if result:

                    body.update({
                        'script': result['content']
                    })

        packet_info = packet_info_schema.from_dataframe(current_row)  

        request_data = {
            'ip': ip,
            'port': port,
            'input_id': int(input_id),
            'body': body,
            'packet_info': packet_info
        }
        response = requests.post(URL, json=request_data)
    except Exception as e:
        logging.error(f'Error in send_request: {str(e)}')

def load_data():
    filenames = [f"../data/origin/re_cm_unsw_nb15_{i}.csv" for i in range(1,31)]
    datas = []
    for fn in filenames:
        try:
            data = pd.read_csv(fn)
            datas.append((fn, data))
            logging.info(f'Successfully loaded {fn}')
            current_index[fn] = 0  
        except Exception as e:
            logging.error(f'{fn} could not be loaded: {str(e)}')
    return datas

def send_multiple_requests(datas):
    logging.info("Starting send_multiple_requests")
    threads = []
    
    for filename, data in datas:
        thread = threading.Thread(target=send_request, args=(data, filename))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    logging.info("Completed send_multiple_requests")
    

if __name__ == "__main__":
    datas = load_data()

    total_remaining = sum(len(data) - current_index[fn] for fn, data in datas)
    while total_remaining > 0:
        send_multiple_requests(datas)
        total_remaining = sum(len(data) - current_index[fn] for fn, data in datas)
        logging.info(f"{total_remaining} data remaining.")
