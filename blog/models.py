from django.conf import settings
from django.db import models
from django.utils import timezone

# post가 model을 상속받는다
# 상속
# Model의 속성이나 메서드를 Post에서 그대로 쓸 수 있다
# Model이 부모 클래스
class Post(models.Model):
    # 속성
    # 포린키==외래키==다른 모델을 가리키는 속성
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # charfield 제목이 200자까지 길이가 정해진 문자열을 담을 때
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    # 매서드
    def publish(self):
        # self== 자기 자신의 오블젝트를 가리키는 약속
        self.published_date = timezone.now()
        # Post가 실제로 데이터베이스에 저장이 됨
        self.save()

    # 매서드
    # __str__ == Post라는 객체를 문자로 바꿔줄 때 __str__을 쓴다
    def __str__(self):
        return self.title