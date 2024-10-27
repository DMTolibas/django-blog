from django.db import models

# Create your models here.

'''
Objects
-Author
    -last name, first name, birthday, profession
-Article
    -content, date created

Please be remind that django_blog is your project folder, but the root project is blog.

'''

class Author(models.Model):
    #Class representing author 
    last_name = models.CharField(max_length=100)
    given_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    date_of_birth = models.DateField(verbose_name="Date of Birth",
                                     blank=True, null=True)

    class Meta:
        #for how the query result is displayed
        ordering = ["given_name", "last_name"]
    
        #Direct how can they be displayed in admin interface
    def __str__(self):
        #To make the object human-readable, not memory loc.
        return f'{self.last_name}, {self.given_name}'



class Article(models.Model):
    #class representing article
    title = models.CharField(max_length=100, help_text="Make your title concise.")
    content = models.TextField(help_text="Start writing in this field")
    date_created = models.DateField(blank=True, null=True)
    
    LANGUAGE = (
        ("ENG", "ENGLISH"),
        ("TAG", "TAGALOG"),
        ("TAGLISH", "TAGALOG-ENGLISH"),
        ("SPA", "SPANISH"),
        ("GER", "GERMAN")
        )
    language = models.CharField(max_length=20, choices=LANGUAGE, default="ENG") 
    
    STATUS = (
        ("Publish", "PUBLISH"),
        ("Draft", "DRAFT")
        )
       
    status = models.CharField(max_length=20, choices=STATUS, default="DRAFT") 

    
    #Author can wrote multiple article, but an article can be written only by one author (in this case only)
    #Foreign key allow us to associate article with author
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="article", null=True, blank=True)
    
    def __str__(self):
        #To make the object human-readable, not memory loc.
        return f'{self.title}'
    
#Feedback
class Feedback(models.Model):
    username = models.CharField(max_length=100, help_text="Input your name", null = True, blank = True) #TO ADD: allow anonymous submission
    feedback = models.TextField(help_text="Enter your suggestions or report a bug.") 
