from django.db import models

# Create your models here.

'''
    Table. Question
    ------------------------------------------------------------------------------------
    Column          |   Type            |   Constraints                 |   Remark
    ------------------------------------------------------------------------------------
    id              |   integer         |   NotNull, PK, AutoIncrement    |   Primary Key
    question_test   |   varchar(200)    |   NotNull                     |   질문 문장
    pub_date        |   datetime        |   NotNull                     |   질문 생성 시각

    CREATE TABLE Question (
        id INTEGER NOT NULL PRIMARY KEY AUTO INCREMENT,
        question_test   VARCHAR(200)    NOT NULL,
        pub_date    DATETIME    NOT NULL
    );
'''


class Question(models.Model):
    # question_id : Primary Key, Django 에서 자동 생성
    #   - lowercaseTableName_id
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # v2.x
    #   - object --> string 으로 표현할 때 사용
    #   - Admin site or Django shell 에서 Table name 을 보여줄 때 사용
    def __unicode__(self):
        return self.question_text

    # v3.x
    # def __str__(self):
    #     return self.question_text


'''
    Table. Choice
    ------------------------------------------------------------------------------------
    Column          |   Type            |   Constraints                 |   Remark
    ------------------------------------------------------------------------------------
    id              |   integer         |   NotNull, PK, AutoIncrement        |   Primary Key
    choice_text     |   varchar(200)    |   NotNull                         |   답변 항목 문구
    votes           |   integer         |   NotNull                         |   투표 카운트
    question_id     |   integer         |   NotNull, FK(Question.id), Index   |   Foreign Key

    CREATE TABLE Choice (
        id INTEGER NOT NULL PRIMARY KEY AUTO INCREMENT,
        choice_text   VARCHAR(200)    NOT NULL,
        votes   INTEGER NOT NULL,
        question_id INTEGER NOT NULL FOREIGN KEY
    );
'''


class Choice(models.Model):
    # choice_id : Django 에서 자동 생성
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question_id = models.ForeignKey(Question)

    # v2.x
    def __unicode__(self):
        return self.choice_text

    # v3.x
    # def __str__(self):
    #     return self.choice_text
