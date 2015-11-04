# encoding=utf-8
from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.


# class ChoiceInline(admin.StackedInline):  # 4.1.6 Question 및 Choice 를 한 화면에서 변경하기
class ChoiceInline(admin.TabularInline):  # 4.1.7 테이블 형식으로 보여주기
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    # 4.1.2 필드 순서 변경하기
    # fields = ['pub_date', 'question_text']  # change the order

    # 4.1.3 각 필드를 분리해서 보여주기
    # fieldsets = [
    #     ('Question Statement', {'fields': ['question_text']}),
    #     ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]

    # 4.1.6 Question 및 Choice 를 한 화면에서 변경하기
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
