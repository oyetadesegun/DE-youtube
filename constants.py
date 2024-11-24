import configparser
import os

# Construct config file path
config_path = os.path.join(os.path.dirname(__file__), '.\\config\\config.local')

# Check if the file exists
if not os.path.exists(config_path):
    raise FileNotFoundError(f"Configuration file '{config_path}' not found.")

# Parse the configuration
parser = configparser.ConfigParser()
parser.read(config_path)

# Check for section and key
if 'youtube' not in parser:
    raise configparser.NoSectionError("youtube")

if not parser.has_option('youtube', 'API_KEY'):
    raise configparser.NoOptionError('API_KEY', 'youtube')

# Retrieve the API key
YOUTUBE_API_KEY = parser.get('youtube', 'API_KEY')
