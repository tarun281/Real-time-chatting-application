
class BaseMiddleware:
    def __init__(self, get_response: callable):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        print("Response ketishidan oldingi amallar")
        response = self.get_response(request, *args, **kwargs)
        print("Response ketganidan keyingi amallar")
        return response