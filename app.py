from flask import Flask, render_template, request
import main

app = Flask(__name__)


@app.route("/", methods = ['POST', 'GET'])
def homepage():
    # seçilen kurun karşılığında gelen değer bilgisi
    doviz_c = {
        "_usd": main.usd,
        "_tl": 1,
        "_avustralya_dolar": main.avustralya_dolar,
        "_danimarka_kron": main.danimarka_kron,
        "_euro": main.euro,
        "_sterlin": main.sterlin,
        "_frang": main.frang,
        "_isvec_kron": main.isvec_kron,
        "_canada_dolar": main.canada_dolar,
        "_kuveyt_dinar": main.kuveyt_dinar,
        "_norvec_kron": main.norvec_kron,
        "_arabistan_riyal": main.arabistan_riyal,
        "_japon_yeni": main.japon_yeni,
        "_rus_ruble": main.rus_ruble,
        "_cin_yuan": main.cin_yuan,
        "_guneykore_won": main.guneykore_won,
        "_azerbaycan_manat": main.azerbaycan_manat
    }
    
    if request.method == "POST":
        number1 = request.form.get("number1")
        doviz = request.form.get("doviz")
        doviz1 = request.form.get("doviz1")
        
        kur1 = doviz_c[doviz]
        kur2 = doviz_c[doviz1]
        islem1 = kur1/kur2
        islem2 = float(islem1)*float(number1)
        cevrilmis_kur = round(islem2, 4)
        
        return render_template("index.html",
        cevrilmis_kur = cevrilmis_kur,
        doviz = doviz,
        number1 = number1,
        usd = main.usd,
        avustralya_dolar = main.avustralya_dolar,
        danimarka_kron = main.danimarka_kron,
        euro = main.euro,
        sterlin = main.sterlin,
        frang = main.frang,
        isvec_kron = main.isvec_kron,
        canada_dolar = main.canada_dolar,
        kuveyt_dinar = main.kuveyt_dinar,
        norvec_kron = main.norvec_kron,
        arabistan_riyal = main.arabistan_riyal,
        japon_yeni = main.japon_yeni,
        rus_ruble = main.rus_ruble,
        cin_yuan = main.cin_yuan,
        guneykore_won = main.guneykore_won,
        azerbaycan_manat = main.azerbaycan_manat)
    else:
        pass
    
    return render_template("index.html",
        usd = main.usd,
        avustralya_dolar = main.avustralya_dolar,
        danimarka_kron = main.danimarka_kron,
        euro = main.euro,
        sterlin = main.sterlin,
        frang = main.frang,
        isvec_kron = main.isvec_kron,
        canada_dolar = main.canada_dolar,
        kuveyt_dinar = main.kuveyt_dinar,
        norvec_kron = main.norvec_kron,
        arabistan_riyal = main.arabistan_riyal,
        japon_yeni = main.japon_yeni,
        rus_ruble = main.rus_ruble,
        cin_yuan = main.cin_yuan,
        guneykore_won = main.guneykore_won,
        azerbaycan_manat = main.azerbaycan_manat
        )


if __name__ == "__main__":
    app.run(debug=True)
