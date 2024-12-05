import logging

logging.basicConfig(
    handlers=[logging.StreamHandler(), logging.FileHandler("mediatheory.log")],
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
