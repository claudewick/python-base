#!/usr/bin/env python3

import os
import logging


# BOILERPLATE
# TODO: usar função
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
# nossa instância
log = logging.Logger("logs.py", log_level) # primeiro parâmetro = nome / segundo = nível de log
# level
ch = logging.StreamHandler() # Console/terminal/stderr
ch.setLevel(log_level)
# formatação
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s'
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
# destino
log.addHandler(ch)
"""
# root logger
logging.debug("Mensagem pro dev, qe, sysadmin")
logging.info("Mensagem geral para usuários")
logging.warning("Aviso que não causa erro")
logging.error("Erro que afeta uma única execução")
logging.critical("Erro geral ex: banco de dados sumiu")

# log customizado
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuários")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma única execução")
log.critical("Erro geral ex: banco de dados sumiu")
"""

print("---")
try:
    1/0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
    #stdout
    #stderr
