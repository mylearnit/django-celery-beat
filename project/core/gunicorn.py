import gunicorn

if gunicorn.version_info != (20, 1, 0):  # pragma: no cover
    raise ValueError(
        "Remove this gunicorn setting from config/gunicorn according to version"
    )
gunicorn.SERVER = "Server"