def require_role(roles=[1]):
    
    from functools import wraps
    from flask_login import current_user
    import app

    def wrap(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not current_user.role_id in roles:
                return app.login_manager.unauthorized()

            return func(*args, **kwargs)
        return decorated_view
    return wrap