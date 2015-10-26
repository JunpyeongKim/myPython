# encoding=utf-8

# 3.3.2 Model - 데이터베이스 설계
#   - (*) Person 테이블 / 모델 클래스 정의
#   - TableName = ApplicationName_ClassName <-- 다른 이름으로 직접 지정 가능
#   - Primary Key : Django 에서 자동으로 부여
#   - (*) https://docs.djangoproject.com/en/1.7/topics/db/models


from django.db import models

'''
CREATE TABLE myapp_person (
  id serial NOT NULL PRIMARY KEY,
  first_name varchar(30) NOT NULL,
  last_name varchar(30) NOT NULL
);
'''


class Person(models.Model):
    """
    Person class.

        CREATE TABLE myapp_person (
            id serial NOT NULL PRIMARY KEY,
            first_name varchar(30) NOT NULL,
            last_name varchar(30) NOT NULL
        );
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
