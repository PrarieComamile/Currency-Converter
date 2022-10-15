import requests
import json

# veriyi alma
link = "https://hasanadiguzel.com.tr/api/kurgetir"
url = requests.get(link)

# veriyi isleme
url = url.text
url = json.loads(url)

# doviz kurlari
usd = url["TCMB_AnlikKurBilgileri"][0]["ForexSelling"]
avustralya_dolar = url["TCMB_AnlikKurBilgileri"][1]["ForexSelling"]
danimarka_kron = url["TCMB_AnlikKurBilgileri"][0]["ForexSelling"]
euro = url["TCMB_AnlikKurBilgileri"][3]["ForexBuying"]
sterlin = url["TCMB_AnlikKurBilgileri"][4]["ForexSelling"]
frang = url["TCMB_AnlikKurBilgileri"][5]["ForexBuying"]
isvec_kron = url["TCMB_AnlikKurBilgileri"][6]["ForexSelling"]
canada_dolar = url["TCMB_AnlikKurBilgileri"][7]["ForexBuying"]
kuveyt_dinar = url["TCMB_AnlikKurBilgileri"][8]["ForexBuying"]
norvec_kron = url["TCMB_AnlikKurBilgileri"][9]["ForexSelling"]
arabistan_riyal = url["TCMB_AnlikKurBilgileri"][10]["ForexBuying"]
japon_yeni = url["TCMB_AnlikKurBilgileri"][11]["ForexBuying"]# 100 japon yeni
rus_ruble = url["TCMB_AnlikKurBilgileri"][14]["ForexSelling"]
cin_yuan = url["TCMB_AnlikKurBilgileri"][16]["ForexBuying"]
guneykore_won = url["TCMB_AnlikKurBilgileri"][19]["ForexSelling"]
azerbaycan_manat = url["TCMB_AnlikKurBilgileri"][20]["ForexBuying"]



