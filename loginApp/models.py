from django.db import models

# Create your models here.

# class AdminDetail(models.Model):
#     s_no=models.IntegerField(auto_created=True,primary_key=False)
#     admin_id=models.AutoField(primary_key=True)
#     admin_name=models.CharField(max_length=100)
#     designation=models.CharField(max_length=50)
#     emp_classification=models.CharField(max_length=50)
#     email_id=models.CharField(max_length=100)
#     password=models.CharField(max_length=10)
    
#     def __str__(self):
#         return self.admin_name


# class SchoolDetail(models.Model):
#     school_id=models.AutoField(primary_key=True)
#     school_code=models.CharField(max_length=10, unique=True)
#     school_name=models.CharField(max_length=255, unique=True)

#     def __str__(self):
#         return self.school_name
    
# class DeptDetail(models.Model):
#     dept_id=models.AutoField(primary_key=True)
#     dept_code=models.CharField(max_length=10)
#     dept_name=models.CharField(max_length=200)
#     school_id=models.ForeignKey(SchoolDetail,on_delete=models.CASCADE,db_column='school_id')

#     def __str__(self):
#         return self.dept_name

# class facultyDetails(models.Model):
#     faculty_id=models.CharField()
#     faculty_password=models.CharField(15)
#     faculty_dept=
