import marimo

__generated_with = "0.19.4"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Noin 3000 yleisintä ruotsin kielen sanaa alkaen yleisimmästä. Eli alussa on jag ja du ja näitä.

    ID: sanalle id: alkaa ykkösestä,
    Swedish column: vain yksi sana perusmuodossa
    English column: 1-3 lähintä käännöstä.
    forms: sanan formit
    word_type: mikä tyyppi
    swedish_example, yksi esimerkki lause ruotsiksi
    english_example: lauseen käännös

    Sitten tricky part. esimerkkilauseissa esiintyy muita listan sanoja sopivissa kohdin ja määrin.
    Esimerkiksi jag id on 1 ja startar id on 10, bil id 25: esimerkki lause voisi olla: jag har röda bil men det startar inte.

    Eli tässä jag sanan esimerkki lause antaa jo pian tulevasta sanasa bil id 25 ja antaa reminderin jo olleesta sanasta startar id 10.
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Mission Statement:
    - Tarvitaan ID: column - > rolling

    - Swedish column: vain yksi sana perusmuodossa

    - English column: 1-3 lähintä käännöstä

    - forms: sanan formit

    - word_type: mikä tyyppi

    - swedish_example, yksi esimerkki lause ruotsiksi

    - english_example: lauseen käännös
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Tehdään ylläoleville asioille numerointi.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Kun teen databasen prob duckdb, niin käytetään näitä arvoja per haluttu asia

    ID_COLUMN  = 0
    SWEDISH_COLUMN = 1
    ENGLISH_COLUMN = 2
    FORMS = 3
    WORD_TYPE = 4
    SWEDISH_EXAMPLES = 5
    ENGLISH_EXAMPLES = 6
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


if __name__ == "__main__":
    app.run()
