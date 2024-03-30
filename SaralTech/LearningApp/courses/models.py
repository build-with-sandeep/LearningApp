from django.db import models

class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Course(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Module(BaseModel):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Section(BaseModel):
    module = models.ForeignKey(Module, related_name='sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Video(BaseModel):
    section = models.ForeignKey(Section, related_name='videos', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_url = models.URLField()

    def __str__(self):
        return self.title

class Assignment(BaseModel):
    section = models.ForeignKey(Section, related_name='assignments', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Question(BaseModel):
    assignment = models.ForeignKey(Assignment, related_name='questions', null=True, blank=True, on_delete=models.SET_NULL)
    text = models.TextField()

    def __str__(self):
        return self.text

class Test(BaseModel):
    course = models.ForeignKey(Course, related_name='tests', null = True , blank = True,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class TestQuestion(BaseModel):
    test = models.ForeignKey(Test, related_name='test_questions', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='test_questions', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.test.title} - {self.question.text}"



class Answer(BaseModel):
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)

    def __str__(self):
        correctness_indicator = '(Correct)' if self.is_correct else ''
        return f"{self.question.text}: {self.text} {correctness_indicator}"