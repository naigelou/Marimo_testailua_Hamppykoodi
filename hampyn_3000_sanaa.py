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
def _(mo):
    mo.md(r"""
    # Swedish Kelly-list columns explained (beginner-friendly)

    Each row in the Kelly-list is one **word entry** (a *lemma*) plus information about that word.

    ---

    ## 1) ID / running number (rank)
    **What it is:** The word’s **position** in the frequency list.
    **What it tells you:** Lower ID usually means the word is **more common**.

    - ID = 1 → one of the most frequent words
    - ID = 5000 → still common, but less frequent than the first ones

    **Example:** `ID = 88` means the word is around the 88th most frequent in the list.

    ---

    ## 2) Raw frequency (RF)
    **What it is:** The **total number of times** the word appears in the source text collection (corpus).
    **What it tells you:** How often it was seen **in the raw data**.

    **Example:** `RF = 2,624,032` means the word appeared 2,624,032 times in the corpus.

    **Note:** RF depends on corpus size. A larger corpus gives bigger numbers.

    ---

    ## 3) Relative frequency / Word per Million (WPM)
    **What it is:** Frequency scaled to **a standard size**: “how many times per 1,000,000 words.”
    **What it tells you:** A fair way to compare frequencies **across corpora of different sizes**.

    **Example:** `WPM = 23017.26` means that in 1,000,000 words of text, the word appears about 23,017 times.

    **Why it matters:** WPM is easier to compare than RF.

    ---

    ## 4) CEFR level (A1–C2)
    **What it is:** A difficulty/learning level from the CEFR framework.
    **What it tells you:** Roughly when learners are expected to know the word.

    - **A1** = beginner (very common, basic words)
    - **A2** = elementary
    - **B1** = intermediate
    - **B2** = upper-intermediate
    - **C1** = advanced
    - **C2** = proficient / near-native

    **Example:** `CEFR = A1` means the word is expected early in learning.

    ---

    ## 5) Source of lemma
    **What it is:** Where the headword came from (how it was selected).
    **What it tells you:** The origin of the entry, which can affect style and coverage.

    Typical sources you mentioned:
    - **SweWAC**: from the SweWAC corpus (large Swedish web corpus)
    - **T2**: from a translation list
    - **Manually added**: inserted by editors

    **Example:** `Source = SweWAC` means it comes from the corpus list.

    ---

    ## 6) Grammar information (article or infinitive marker)
    **What it is:** A short grammar hint attached to the lemma.
    **What it tells you:** How to use the word correctly in sentences.

    Common cases:
    - For **nouns**: the **article** (e.g., *en*, *ett*)
      - `en bil` (a car), `ett hus` (a house)
    - For **verbs**: the **infinitive marker** (often *att*)
      - `att vara` (to be)

    **Example:** `Grammar marker = att` suggests the lemma is a verb used as `att + verb`.

    ---

    ## 7) Lemma (sometimes with variants)
    **What it is:** The dictionary base form of the word (the “headword”).
    **What it tells you:** The form you typically look up in a dictionary.

    Sometimes variants are included:
    - spelling variants
    - stylistic variants (formal/informal)
    - spoken forms

    **Example:** `vara (vardagl. va)` means:
    - **vara** = the lemma (“to be”)
    - **va** = a more casual/spoken variant

    ---

    ## 8) Word class (POS)
    **What it is:** Part of Speech (POS).
    **What it tells you:** The grammatical category of the word.

    Common POS values:
    - **noun**
    - **verb**
    - **adjective**
    - **adverb**
    - **pronoun**
    - **preposition**
    - **conjunction**
    - **interjection**

    **Example:** `POS = verb` means the lemma is a verb.

    ---

    ## 9) Comments / examples
    **What it is:** Extra notes, clarifications, or example sentences.
    **What it tells you:** How the word is used in real context, or special meaning notes.

    **Example:** `var så god!` is a usage example for **vara**.

    ---

    # Mini example (one entry)
    **ID:** 88
    **RF:** 2,624,032
    **WPM:** 23,017.26
    **CEFR:** A1
    **Source:** SweWAC
    **Grammar marker:** att
    **Lemma:** vara (vardagl. va)
    **POS:** verb
    **Example:** var så god!

    This means: “vara” is a very common A1-level verb, drawn from the SweWAC source, and frequently used enough to appear ~23,017 times per million words in that corpus.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    https://spraakbanken.gu.se/projekt/kelly

    Siis noitten database on arvostellut eniten käyetty ja vaikeustasot. Voidaan tolla datal tehä eri Certifikaatti luokka kyselyitä
    """)
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
    import pandas as pd


    df = pd.read_csv("swe-eng-malli.csv")
    df.head(10)
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell
def _():
    from os import path

    BASE_DIR = path.dirname(path.abspath(__file__))

    print(BASE_DIR) # Alotus directory / MAIN

    DATA_DIR = path.join(BASE_DIR, "csv")  # Täältä haetaan excelit

    return (DATA_DIR,)


@app.cell
def _(DATA_DIR):
    def _():
        import os
        from os import path

        csv_files = [
            f for f in os.listdir(DATA_DIR)
            if f.lower().endswith(".csv") and path.isfile(path.join(DATA_DIR, f))
        ]
        return csv_files


    _()
    return


@app.cell
def _(df):
    len(df)

    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
