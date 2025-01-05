import logging
import os

logging.basicConfig(level=logging.INFO)
class Logger:
    _LOG_FORMAT = "%(asctime)s %(name)s [%(levelname)s]: %(message)s in %(name)s.py line:%(lineno)d"
    _LOG_LEVEL = logging.INFO

    def __init__(self, api_class_name_log, base_api_log_name):
        # Main logger setup
        self.main_logger = logging.getLogger(base_api_log_name)
        if len(self.main_logger.handlers) == 0:
            main_logger_file_handler = logging.FileHandler("main_log.log")
            main_logger_file_handler.setLevel(self._LOG_LEVEL)
            main_logger_file_handler.setFormatter(logging.Formatter(self._LOG_FORMAT))
            self.main_logger.addHandler(main_logger_file_handler)
        self.main_logger.setLevel(logging.CRITICAL)
        self.main_logger.propagate = True  # Prevent messages from going to the root logger

        # Class-level logger setup
        self.class_logger = logging.getLogger(f"{base_api_log_name}.{api_class_name_log}")
        if len(self.class_logger.handlers) == 0:
            class_logger_file_handler = logging.FileHandler(f"{api_class_name_log}_log.log")
            class_logger_file_handler.setLevel(self._LOG_LEVEL)
            class_logger_file_handler.setFormatter(logging.Formatter(self._LOG_FORMAT))
            self.class_logger.addHandler(class_logger_file_handler)
        self.class_logger.setLevel(self._LOG_LEVEL)
        self.class_logger.propagate = True  # Enable propagation to the main logger




















        # def __init__(self, api_class_name_log, base_api_log_name):
        #
        #     self.main_logger = logging.getLogger(base_api_log_name)
        #     self.main_logger.setLevel(self._LOG_LEVEL)
        #     if len(self.main_logger.handlers) == 0:
        #         main_logger_file_handler = logging.FileHandler("main_log.log")
        #         main_logger_file_handler.setLevel(self._LOG_LEVEL)
        #         main_logger_file_handler.setFormatter(logging.Formatter(self._LOG_FORMAT))
        #         self.main_logger.addHandler(main_logger_file_handler)
        #
        #
        #     self.class_logger = logging.getLogger(api_class_name_log)
        #     self.class_logger.setLevel(self._LOG_LEVEL) # setting the main logger
        #     self.class_logger.propagate = False  # Prevent propagation to parent loggers
        #     if len(self.class_logger.handlers) == 0:
        #         logger_file_handler = logging.FileHandler(f"{api_class_name_log}_log.log")
        #         logger_file_handler.setLevel(self._LOG_LEVEL)
        #         logger_file_handler.setFormatter(logging.Formatter(self._LOG_FORMAT))
        #         self.class_logger.addHandler(logger_file_handler)