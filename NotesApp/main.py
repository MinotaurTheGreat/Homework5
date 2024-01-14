# run.py

from website import create_app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

    #doar daca rulam acest fisier, nu importam, o sa executam....
    #...acest cod , ptr rularea serverului web, acest cod inseamna ca de fiecare data ...
    #...cand schimbam codul website-ului, va fi modificat in timp ce ruleaza xdd
    