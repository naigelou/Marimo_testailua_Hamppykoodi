1. Ensin sun pitää asentaa uv , Python install manager, tehty rustilla paljon nopeempi.

AJA NÄÄ GIT BASHIN LÄPI SUN WIN KONEEL!!!!


gitbash - Install uv using the official installer:
```
curl -LsSf https://astral.sh/uv/install.sh | sh

```

Restart your terminal (or reload your shell), then verify:
uv --version


-----

" JOS HALUUT YKSIN TESTAA JA KATTOO KUI TOIMIII " 

"""
Tehdään marimo-test folder, cd -> liikutaan sinne , uv init Tekee tälle folderille pyproject.toml , Voidaan tätä kautta hallita versio managmentteja yhdestä paikka meidän virtuaali ympäristössä
"""


mkdir marimo-test
cd marimo-test
uv init

------

Aja "Marimo_testailua_Hamppykoodi"  alla olevat comennot niin dashboard aukee localhost:2719

uv init
uv python pin 3.12
uv add marimo
uv run marimo edit
