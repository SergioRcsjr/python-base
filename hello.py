#!/usr/bin/env python3
"""Hello World Multi Languages.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Usage:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execution:

    python3 hello.py
    or
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Sergio.Rcsjr"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG") [:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour le Monde!"

print(msg)