from django.db import models

class product(models.Model):
    name=models.CharField(max_length=20)
    version=models.CharField(max_length=20)

class version(models.Model):
    number=models.CharField(max_length=20)
    content=models.TextField()
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    status=models.IntegerField()
    include_functions=models.TextField()

class test_cases(models.Model):
    title=models.TextField()
    premise=models.TextField()
    steps=models.TextField()
    expected_result=models.TextField()

class records_test_exec(models.Model):
    case_id=models.ForeignKey(test_cases,on_delete=models.CASCADE)

class records_test(models.Model):
    version_number=models.ForeignKey(version,on_delete=models.CASCADE)
    test_result=models.IntegerField()
    test_cases_records = models.ForeignKey(records_test_exec,on_delete=models.CASCADE)
    fail_desc=models.TextField()

class user(models.Model):
    user=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=40)






