import os
from app import app

# When Vercel loads functions from the api/ folder, the module __file__ is inside api/
# Ensure Flask knows the project root so templates and static files resolve correctly.
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Set template/static folders explicitly in case imports change Flask's root path
app.template_folder = os.path.join(BASE_DIR, "templates")
app.static_folder = os.path.join(BASE_DIR, "static")
app.root_path = BASE_DIR

# Export the WSGI callable expected by Vercel
application = app

