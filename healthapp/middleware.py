# myproject/middleware.py

class AppSpecificSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the session key from the URL path, e.g., 'doctors/' or 'users/'
        app_prefix = request.path.split('/')[1]
        
        if app_prefix in ['doctors', 'users']:
            session_key = f"{app_prefix}_sessionid"
            request.COOKIES['sessionid'] = request.COOKIES.get(session_key, '')
        
        response = self.get_response(request)
        
        if app_prefix in ['doctors', 'users']:
            # Set specific session cookie for the app
            session_key = f"{app_prefix}_sessionid"
            if 'sessionid' in request.COOKIES:
                response.set_cookie(session_key, request.COOKIES['sessionid'])
        
        return response
