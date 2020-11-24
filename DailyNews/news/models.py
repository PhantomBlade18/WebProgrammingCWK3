from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 50)
   #member_set is a resulting queryset from the many to many relationship defined in member. Not necessarily needed for now
    # articles is now a set of news articles that have a relationship with a specific category
    def __str__(self):
        x = "Category: "+self.name
        return x

class Member(User): #This is the user, contains the username and password fields by default
    #Member inherits the email field from USER so not needed. call it using member.email
    DOB = models.DateTimeField()
    favouriteCats = models.ManyToManyField(Category)

    def __str__(self):
        x = "Name: "+self.get_username()+" Password:  "+self.get_password()+ "Date of Birth: "+ str(self.DOB)+ " Favourite Categories: " +self.getCats() + "\n"
        return x

    def getCats(self):
       cats = ""
       clist = self.favouriteCats.all()
       for c in clist:
          cats += (c.name + " , ")
       return cats

class Article(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField(max_length = 3000)
    pub_Date = models.DateTimeField()
    category = models.ForeignKey( to=Category,related_name='articles',on_delete=models.CASCADE)

    def __str__(self):
        x = "Title: "+self.title + " Body: "+ self.body+ " Published: "+ str(self.pub_Date)+ " Category: " +self.category.name + "\n"
        return x
