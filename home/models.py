from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.



class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField('Created Time', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('Updated Time', auto_now_add=True, null=True)

    class Meta:
        abstract = True


class Blog(BaseModel):
    user = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            related_name="blogs" )
    
    title = models.CharField(max_length=100)
    blog_text = models.TextField()
    main_img = models.ImageField(upload_to="blogs")

    def __str__(self) -> str:
        return self.title

