from datetime import date 
from datetime import datetime 


def data_para_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


def str_para_data(data: str) -> date:
    return datetime.strptime(data,'%d/%m/%Y')


