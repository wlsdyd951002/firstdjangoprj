from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    # author는 사용자의 createsuperuser 혹은 superuser가 만든 계정자료와
    # 연동, 글쓴이는 자동으로 로그인한 사용자의 정보가 가입된다.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # CharField는 글자수 제한이 있는 칼럼을 의미, max_length 길이 제한
    title = models.CharField(max_length=200)
    # TextFiedl는 글자구 제한이없는 칼럼을 의미
    text = models.TextField()
    # DdateTimeField는 시간 저장을 위한 컬럼을 의미, default는 입력하지 않을때
    # 자동으로 기입할 자료를 정해줌, timezone.now는 등록 당시의 서버시간
    created_date = models.DateTimeField(
            default=timezone.now)
    # blank=True일 경우 칼럼이 비어있어도 됨, null=True는 null값을 넣기 허용
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title