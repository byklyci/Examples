# import mongoengine as me
#
# me.connect("userss")
#
# class User(me.Document):
#     id = me.IntField()
#     name = me.StringField(max_length=200, unique=True)
#     year = me.IntField()
#     study = me.StringField(min_length=3, required=True)
#
# ali = User(name="Ali")
# ali = User(year=1995)
# ali = User(study="doctor")
# ali.save()
import mongoengine as me
from mongoengine import *
import datetime

me.connect("examples")

# class User(Document):
#     name = StringField()
#
# class Page(Document):
#     content = StringField()
#     authors = ListField(ReferenceField(User))
#
# bob = User(name="Bob Jones").save()
# john = User(name="John Smith").save()
#
# Page(content="Test Page", authors=[bob, john]).save()
# Page(content="Another Page", authors=[john]).save()

# class Comment(EmbeddedDocument):
#     content = StringField()
# class Block(Document):
#     comments = ListField(EmbeddedDocumentField(Comment))
#
# comment1= Comment(content ='Good work!')
# comment2 = Comment(content = 'Nice article!')
#
# block= Block(comments=[comment1,comment2]).save()

#
# class Name(Document):
#     name= StringField()
#
# class Surname(Document):
#     content = StringField()
#     author = ReferenceField(Name)
#
# johm = Name(name='Yusuf')
# johm.save()
#
# post = Surname(content= 'klyci')
# post.author = johm
# post.save()

# class Employee(Document):
#     name = StringField()
#     boss = ReferenceField('self')
#     profile_page = ReferenceField('ProfilePage')
#
# class ProfilePage(Document):
#     content = StringField()
#
# ali = Employee(name= 'alican',boss= 'selfi')
# ali.save()
# # p= ProfilePage(content='alican2')
# # p.profile_page =ali
# # p.save()

class User(Document):
    name = StringField()

class Page(Document):
    content = StringField()
    authors = ListField(ReferenceField(User))


bob = User(name="Bob Jones").save()
john = User(name="John Smith").save()

Page(content="Test Page", authors=[bob, john]).save()
Page(content="Another Page", authors=[john]).save()

# Find all pages Bob authored


# user_name = User.objects(name='ysf')
# Page.objects(authors__in=[bob])
# for user in User.objects:
#     print(user.name)


# Find all pages that both Bob and John have authored
p= Page.objects(authors__all=[bob, john])
print(p)
# # Remove Bob from the authors for a page.
# Page.objects(id='...').update_one(pull__authors=bob)
#
# # Add John to the authors for a page.
# Page.objects(id='...').update_one(push__authors=john)
#
