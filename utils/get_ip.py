
def get_user_ip(request):
    ip = request.META.get('REMOTE_ADDR')
    return ip