import logging

def setup_logging(log_file_path):
    logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Example usage:
log_file_path = "C:/Users/Nikhil Kadam/NikhilProjects/swag_fr_Auto2/demo/logfile2log"
setup_logging(log_file_path)