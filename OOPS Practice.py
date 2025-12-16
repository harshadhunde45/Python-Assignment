#!/usr/bin/env python
# coding: utf-8

# In[1]:


class test:
    pass


# In[ ]:


class course :
    def course_details(self , course_name):
        print(course_name)


# In[5]:


class course:
    def course_details(self,course_name):
        print(course_name)


# In[6]:


c = course()


# In[7]:


c.course_details("data science")


# In[ ]:


class course1 :
    def course_details(sudh , course_name):
        print(course_name)


# In[8]:


class course1:
    def course_details(sudh,course_name):
         print(course_name)


# In[9]:


d = course1()


# In[11]:


d.course_details("python")


# In[12]:


e = course1()


# In[13]:


f = course1()


# In[19]:


i =10


# In[27]:


class course :
    def __init__(self,name,mentor):
        self.name1 = name
        self.mentor1 = mentor
    


# In[28]:


a = course("python","sudh")


# In[29]:


a.mentor1


# In[31]:


a.name1


# In[ ]:


b = course("data science" ,"sudhanshu")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[2]:


class course :
    def course_details(self , course_name):
        print(course_name)


# In[3]:


c = course()


# In[4]:


c.course_details("data science")


# In[6]:


class course1 :
    def course_details(sudh , course_name):
        print(course_name)


# In[7]:


d = course1()


# In[9]:


d.course_details("python")


# In[10]:


e = course1()


# In[11]:


f = course1()


# In[12]:


i =10


# In[13]:


class course :
    def __init__(self,name,mentor):
        self.name1 = name
        self.mentor1 = mentor


# In[15]:


a = course("python","sudh")


# In[16]:


a.mentor1


# In[18]:


a.name


# In[19]:


b = course("data science" ,"sudhanshu")


# In[20]:


b.mentor1


# In[26]:


b.name1


# In[27]:


class course :
    def __init__(self,name,mentor):
        self.name1 = name
        self.mentor1 = mentor
        
    def dispaly(self):
        print(self.mentor1 , self.name1)


# In[28]:


class course:
    def__init__(self,name,mentor):
        self.name1= name
        self.mentor1 =mentor
        
    def display(self):
        print(self.mentor1 ,self.name1)


# In[25]:


a = course("python","xyz")


# In[29]:


a.dispaly()


# In[30]:


b = course("big data" , "sudh")


# In[31]:


b.dispaly()


# In[32]:


c = course("generative ai" , "sudh")


# In[33]:


em.assign_course("python with dsa")


# In[35]:


class mentor:
    def intro(self):
        print("i am a mentor")


# In[36]:


class euronmentor(mentor):
    def intro(self):
        super().intro()
        return "this is euron mentor intro"


# In[37]:


em= euronmentor()


# In[38]:


em.intro()


# In[39]:


class course:
    def __init__(self,title):
        self.title = title
        print(f"{self.title}")


# In[40]:


class euroncourse(course):
    def __init__(self, title,mentor):
        super().__init__(title)
        self.mentor = mentor
        print(f"{self.mentor} and {self.title}")


# In[41]:


ec = euroncourse("python","sudhanshu")


# In[42]:


class plateform:
    def show(self):
        print("this is euron plateform")


# In[43]:


class cousre1(plateform):
    def display_course(self):
        print("course available")


# In[44]:


class dsa(cousre1):
    def intro(self):
        print("its a dsa cousre")


# In[45]:


ds =dsa()


# In[46]:


ds.show()


# In[47]:


ds.intro()


# In[50]:


ds.display_course()


# In[51]:


class design:
    def ui(self):
        print("design system ready")
    
class curriculam:
    def syllabus(self):
        print("curriculam loaded")
        
class euronsystem(design,curriculam):
    pass


# In[52]:


es = euronsystem()


# In[53]:


es.syllabus()


# In[60]:


es.ui()


# In[61]:


class a :
    def show(self):
        print("a")

class b(a):
    def show(self):
        print("b")
        super().show()
        
class c(a):
    def show(self):
        print("c")
        super().show()
        
class d(b,c):
    def show(self):
        print("d")
        super().show()


# In[62]:


d_obj = d()
d_obj.show()


# In[63]:


d.mro()


# In[64]:


c.mro()


# In[59]:


b.mro()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




