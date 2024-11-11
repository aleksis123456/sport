import json
from datetime import datetime 

file_path= 'abonementi.json'

def read_data():
    try:
        with open (file_path, 'r', encoding='utf-8') as file:
            return json.load (file)
    except FileNotFoundError:
        return()

def write data(data):
with open (file_path, 'w',encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

def add_member():
    data=read_data()
    ID= input ("Dalībnieka id: ")
    Vārds = input ("Dalībnieka vārds: ")
    Tālr = input(" Dalībnieka tālrunis: ")
    Pilsēta = input ("Dalībnieka pilsēta: ")
    Apmeklejums = input ( "Vai vēlies abonementam papildu pakalpojumu (y\n) ")
    Treniņa_stundas = 0
    Biezums = 0

    if dalībnieka.lower=='y':
        Treniņa_stundas= int(input('Cik ilgst dalībnieka studas'))
        Biezums= int(input('Dalībnieka biezums'))

registration_date= datetime.now()

dvielu_skaits=int(input("Dvielu skaits:"))
dvielu_maksa=0.50
dvielu_noma_summa=dvielu_skaits*dvielu_maksa

member_data={
    "ID" : id,
    "Vārds" : vārds,
    "Tālr" : tālr,
    "Pilsēta": pilsēta, 
    "Treniņa_stundas": treniņa_stundas, 
    "Biezums": Biezums,
    "registration_date": registration_date,
    "dvielu_noma": dvielu_noma_summa
    }
data(id)= member_data
write_data(data)
print (' {id} veiksmiga treniņa')





    

