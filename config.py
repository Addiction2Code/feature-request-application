# Statement for enabling the development environment
FLASK_APP = 'app'
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'main.db')
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "QszrCTRT7MAoNgFpzERfDKK9oaFnko4PhqY2NfqnU6m4lpuTum649q4U059yGnil"

# Secret key for signing cookies
SECRET_KEY = "slYOv5nW5BH3vUk46SU9dDFVHHtIcmYOEBvrmS6Ux5rQzKUDowIaxTfztcXhH5gU"
