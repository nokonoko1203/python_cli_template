import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = Path('.env')
load_dotenv(dotenv_path)

SAMPLE_STATES = os.environ.get("SAMPLE_STATES")
