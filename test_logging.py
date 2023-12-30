import logging

logger = logging.getLogger('test_logger')
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)

logger.addHandler(handler)

# def test_logging():
#     logger.info("Test logging message")
#     assert True
