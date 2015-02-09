def UserDisplay(request):
    user_dict = {}
    cur_user = request.user or None
    if cur_user and not cur_user.is_anonymous():
        ustr = "logged in as {0}".format(cur_user.username)
        user_dict['user_display'] = ustr + "(<a href='/logout'>logout</a>)"
    return user_dict
