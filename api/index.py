import os

from flask import jsonify

from app import app

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
app.template_folder = os.path.join(BASE_DIR, "templates")
app.static_folder = os.path.join(BASE_DIR, "static")
app.root_path = BASE_DIR


@app.route("/_health")
def vercel_health():
	return jsonify({
		"status": "ok",
		"use_supabase": bool(os.environ.get("SUPABASE_URL")),
		"is_vercel": bool(os.environ.get("VERCEL")) or "VERCEL_ENV" in os.environ,
	})


def strip_prefix_middleware(wsgi_app):
	def middleware(environ, start_response):
		path = environ.get("PATH_INFO", "") or ""
		script = environ.get("SCRIPT_NAME", "") or ""

		for prefix in ("/api/index.py", "/api/index"):
			if path.startswith(prefix):
				environ["PATH_INFO"] = path[len(prefix):] or "/"
				break
			if script.startswith(prefix):
				environ["SCRIPT_NAME"] = ""
				environ["PATH_INFO"] = script[len(prefix):] or "/"
				break

		return wsgi_app(environ, start_response)

	return middleware


application = strip_prefix_middleware(app.wsgi_app)

