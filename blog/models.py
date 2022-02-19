from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


# Create your models here.
class Post(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    Date = models.DateField(_("Date of Post"), auto_now=True)
    Title = models.CharField(_("Title of Post"), max_length=60)
    Story = models.TextField(_("Post Detail"))
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"slug": self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)