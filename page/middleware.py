from django.utils.timezone import now

class ResetDailyPostLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.user.role == "employer":
            user = request.user
            today = now().date()
            if not user.last_reset_date or user.last_reset_date != today:
                user.free_posts_today = min(user.free_posts_today + 2, 2)
                user.last_reset_date = today
                user.save()
        return self.get_response(request)
