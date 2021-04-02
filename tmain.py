import config
import logging
from api import Api


def main():
    try:
        logging.info(f'Starting, logging into: {config.log_filename}')
        api = Api(config.api_key)
        api.hello()
        logging.info('Finished.')
    except Exception as e:
        logging.exception(f'Exception {e.__class__} : {e}')
        raise
    finally:
        logging.info('End of the utility')


if __name__ == '__main__':
    main()
