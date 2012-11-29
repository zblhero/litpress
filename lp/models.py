from django.db import models

# Create your models here.
class comments(models.Model):
    comment_id = models.IntegerField(primary_key = True)
    comment_post_id = models.IntegerField(default = 0)
    comment_author = models.CharField(max_length = 100)
    comment_author_email = models.CharField(max_length = 100)
    comment_author_url = models.CharField(max_length = 200)
    comment_author_IP = models.CharField(max_length = 100)
    comment_date = models.DateTimeField()
    comment_date_gmt = models.DateTimeField()
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length = 20)
    comment_agent = models.CharField(max_length = 255)
    comment_type = models.CharField(max_length = 20)
    comment_parent = models.IntegerField()
    user_id = models.IntegerField()

class links(models.Model):
    link_id = models.IntegerField(primary_key = True)
    link_url = models.CharField(max_length = 255)
    link_name = models.CharField(max_length = 255)
    link_image = models.CharField(max_length = 255)
    link_target = models.CharField(max_length = 255)
    link_description = models.CharField(max_length = 255)
    link_visible = models.CharField(max_length = 255)
    link_owner = models.IntegerField(max_length = 255)
    link_rating = models.IntegerField(max_length = 255)
    link_updated = models.DateTimeField(max_length = 255)
    link_rel = models.CharField(max_length = 255)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length = 255)    

class options(models.Model):
    option_id = models.IntegerField(primary_key = True)
    blog_id = models.IntegerField()
    option_name = models.CharField(max_length = 64)
    option_value = models.TextField()
    autoload = models.CharField(max_length = 20)

class postmeta(models.Model):
    meta_id = models.IntegerField(primary_key = True)
    post_id = models.IntegerField()
    meta_key = models.CharField(max_length = 255)
    meta_value = models.TextField()

class posts(models.Model):
    post_id = models.IntegerField(primary_key = True)
    post_author = models.IntegerField()
    post_date = models.DateTimeField()
    post_date_gmt = models.DateTimeField()
    post_content = models.TextField()
    post_title = models.TextField()
    post_excerpt = models.TextField()
    post_status = models.CharField(max_length = 20)
    comment_status = models.CharField(max_length = 20)
    ping_status = models.CharField(max_length = 20)
    post_password = models.CharField(max_length = 20)
    post_name = models.CharField(max_length = 200)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField()
    post_modified_gmt = models.DateTimeField()
    post_content_filtered = models.TextField()    
    post_parent = models.IntegerField()
    guid = models.CharField(max_length = 255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length = 20)
    post_mime_type = models.CharField(max_length = 100)
    comment_count = models.IntegerField()

class terms(models.Model):
    term_id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 200)
    slug = models.CharField(max_length = 200)
    term_group = models.IntegerField()

class term_relationships(models.Model):
    object_id = models.IntegerField(primary_key = True)
    term_taxonomy_id = models.IntegerField()
    term_order = models.IntegerField()

class usermeta(models.Model):
    umeta_id = models.IntegerField(primary_key = True)
    user_id = models.IntegerField()
    meta_key = models.CharField(max_length = 255)
    meta_value = models.TextField()

class users(models.Model):
    user_id = models.IntegerField(primary_key = True)
    user_login = models.CharField(max_length = 60)
    user_pass = models.CharField(max_length = 64)
    user_nicename = models.CharField(max_length = 50)
    user_email = models.CharField(max_length = 100)
    user_url = models.CharField(max_length = 100)
    user_registered = models.DateTimeField()
    user_activation_key = models.CharField(max_length = 60)
    user_status = models.IntegerField()
    display_name = models.CharField(max_length = 250)

