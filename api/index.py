import os
from flask import jsonify
from app import app

# When Vercel loads functions from the api/ folder, the module __file__ is inside api/
# Ensure Flask knows the project root so templates and static files resolve correctly.
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Set template/static folders explicitly in case imports change Flask's root path
app.template_folder = os.path.join(BASE_DIR, "templates")
app.static_folder = os.path.join(BASE_DIR, "static")
app.root_path = BASE_DIR

# Lightweight health endpoint useful for quick function checks on Vercel
@app.route("/_health")
def vercel_health():
    return jsonify({
        "status": "ok",
        "use_supabase": bool(os.environ.get("SUPABASE_URL")),
        "is_vercel": bool(os.environ.get("VERCEL")) or ("VERCEL_ENV" in os.environ)
    })

# Wrap the Flask app with a small middleware that removes the Vercel rewrite
# prefix (e.g. /api/index or /api/index.py) from PATH_INFO so routes like '/'
# and '/dashboard' continue to work when Vercel forwards requests.

def strip_prefix_middleware(wsgi_app):
    def middleware(environ, start_response):
        path = environ.get("PATH_INFO", "") or ""
        for prefix in ("/api/index.py", "/api/index"):
            if path.startswith(prefix):
                # remove the prefix; ensure at least '/'
                new_path = path[len(prefix):] or "/"
                environ["PATH_INFO"] = new_path
                break
        return wsgi_app(environ, start_response)
    return middleware

application = strip_prefix_middleware(app.wsgi_app)

