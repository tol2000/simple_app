import logging
from datetime import datetime
from pathlib import Path

base_dir = Path(__file__).resolve().parent

log_filename = f'{datetime.today().strftime("%Y-%m-%d-%H-%M-%S")}.log'

logging.basicConfig(
    level=logging.INFO,
    format="[LINE:%(lineno)-10d] # %(levelname)-8s [%(asctime)s] %(message)s",
    filename=base_dir.joinpath('logs').joinpath(
        log_filename
    ),
    filemode='w'
)

# In productive mode this option may be turned off, if logging to file exists
duplicate_logging_to_stderr = True

# Duplicating logging to screen
if duplicate_logging_to_stderr:
    console = logging.StreamHandler()
    logging.getLogger('').addHandler(console)

api_key = ''

"""
If true then:
  Only 1 item from each cycle (one mark, from each mark - one model, etc...)  
"""
debug_preview = True
