
from django.views.generic import TemplateView
from litpress import settings

class BaseView(TemplateView):
    def get_bloginfo(show = '', filter = 'raw'):
        if show == 'home':
            pass
        elif show == 'siteurl':
            pass
        elif show == 'description':
            pass

    def get_posts():
        posts = lp_post.objects.filter()
        return posts
    
    
