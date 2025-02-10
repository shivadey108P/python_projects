import logging

# Configure the logging with a proper timestamp format
logging.basicConfig(
    format="%(asctime)s : %(levelname)s : %(name)s : %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",  # Adds a readable timestamp format
    level=logging.INFO,
)

# Create a logger
logger = logging.getLogger(__name__)

# Log an info message
logger.info("Here is the information")
