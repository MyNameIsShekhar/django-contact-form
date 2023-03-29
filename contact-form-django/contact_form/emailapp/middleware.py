from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta


class AntiSpamMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.last_request_time = {}
        self.time_threshold = 120    # Time threshold 

    def __call__(self, request):
        if request.method == 'POST':
            ip_address = request.META.get('REMOTE_ADDR')
            if ip_address in self.last_request_time:
                last_request = self.last_request_time[ip_address]
                if last_request + timedelta(seconds=self.time_threshold) > timezone.now():                      
                     return render(request, 'emailapp/success.html', {'view_name': 'spam'})
            self.last_request_time[ip_address] = timezone.now()

        response = self.get_response(request)

        if response.status_code == 302 and response.url.startswith('/contactus/') and 'view_name=spam' in response.url:
            request.session['view_name'] = 'spam'

        return response