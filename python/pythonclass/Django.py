from Python.file import A

obj=A()
print obj.add(10,20)
#package is nothing but a folder
#which is mainly used to create packages in python.assume that we are having a folder on desktop with the nameABC.andwhich contain data XYZ.we have __init__.py to make ABC file.if you want to aceess XYZ file from the file which is on desk top use below syntax.
#instaling 3rd party module:to install any package or modile or library.use ethier source code instalation or set up tools.
#using source code to install 3rdparty:download source code zip file from internet.exctract the zip file.locate and run setup.py file by using below command(python setup.py install)
#using setup tools:thepackages can be downloded below tools 1)pip 2)apt-get 3)easy_install 4)wget 5)dpkg
#pip:universal setup tool(install by running get_pip.py)
#apt-get:available in ubuntu or linux
#easy_install:available in ubuntu or linux
#note:pip is universal package installer and will work on all the operating systems or prefer to use pip.
#syntax:pip install package_name==version,apt-get install package_name.
#Django:it is a frame work which is used or devolped for web application it is a package.
#features of Django:1)Django is a well format architerures .that contain saparate phenomenon for each section in an appliction.
#2)Django is light weight and open source.
#by using Django we can connect to any db or any type on server
#Django comes with it's won db named as SQLite
#Django having an advanced orm tool which is used to work with any db in single line of coding.
#MVC design pattern:every frame work follows particular design pattern which make application to be properly allin.Django follow the oldest design pattern MVC.in MVC M stands for model which is known as data abstraction layer and it holds complete data required for project.
#V stands for views which is the combination of bussiness logic layer and prasentation layer.views contains the logical code which was return based on customer requirement and also all front end related files.C stands for controler which is known as heart of the application and it will takecare of request and response.
#followchart of MVC
#browser<........>controler<.........>views<........>modules
#MVT design :Django uses MVT design pattern because of its saparated allinment for each section front end, backend and logic.in MVT M stands for data archetecture layer.V stands for bussiness logic layer and controller.T stand for template which is known as presentation layer.
#creation of Django project:to create a Django project we need to run Django administration file.(file is located in :\)
#open terminal........>go to destination directory where to create file.......>run the below command......>django-admin startproject proect_name(for ubuntu&abovewindows 7)python c;\python27\script\django-admin.py startproject project_name
#after the success ful exicustion above django will create a folder with project name and the folder structer loks like below
#file explanaton:1)mange.py:this file is known as django utility file or managment file which is used to perform any kind of operation related to django.we can create db creation,application creation,running the server.
#setting.py:this file contains all the settings which are related to project,application,db...etc.
#url.py file:this file is also known as url mapping file which contains group of url patterns and there appropiate function.
#wsgi.py file:wsgi file stands for web server guided interface.this file is integrated webservices with project.
#running server or project:to run django server will use utility file(mange.py)and follow he below step
#open terminal....>locate and redirect mange.py...>run the below command (python manage.py runserver ip:port).
#all:this method will return all the records from given db tables.The o\p format is always list of objects
#syntax:table_name.objects.all()
#note:objects is known as model manager which is used to perform db operations of given table.
#filter:it is used to perform conditoinal data retreving on db table. the o/p of filter is always list of objects.
#syntax:ob=table_name.objects.filter(condition)
#filter method accepts only one parameter i.e conditoinal
#ex:obj=stockdetails.objects.filter(quantity=20),.......(quantity__gt=20)........__lt,__lte,__gte,__starts,__ends,__contains
#Qmodels:it is used to work with multiple conditions on db table.we should also use dango logical operator(&,|).Q models are available at django.db.modelsimport Q. while using Qmodels each condition should enclosed by Qmethod 
#ex:table_name.objects.filter(Q(quantity__lt=20)&Q(price(quantity__lt=100))
#note:filter method can be used on both unique and non unique
#get:this method will also works like filter method but the major difference is this will work only on unique fields.if the ORM quare returns more than one record than Django return exception like multiple objects returned.
#to update the data in tablerow:get the perticular record.do the required changes.finally save
#ex:obj=StockDetails.get(price=20),obj.price=30.obj.save()
#html tags:head,body,h1,h2........h6,b.i.u,br,hr,ing,a,,link,script,table,tr,th,td,form,dir
#http response:this method is used to load a static string in browser.this method is available in django.http.HttpResponse.use below statement to import this method.(from django.http import HttpResponse).allthe rendaring functions will work along with return statement in a view function.
#every view function should contain request as a mandatory  of first parameter.(def function_name(request,**kwargs):.......return HttpResponse('display string')).
#render:this method is used to load a static html page in the browser.this method is available at django.shortcuts.render.we can import this method in views.py command.this method takes exactly 2parameters first parameter is always request keyword.2 parameter as string to pass.(fromdango.shortcuts importrender).(def function_name(request,**kw args):.......return render(request,'login page')).
#Http ResponseRedirect:thismethod is used to redirect the users from one page to another page.this method takes exactly one parameter i.e endurl as a string.this method is available at dango.http.HttpResponseRedirect and we can import like below (from dango.http import HttpResponseRedirect).
#syntax:(def function_name(request,**kwarws):......return HRR('end url'))
#render _to _response:this method is used to load a dynamic html page along with data.this method takes exactly 2 parameters first paramers is html page name as string 2 parameter represent data in the formate of dictnary.this method is available at django.shortcuts.render_to_response.we can import likebelow
#(from django.shortcuts import render-to -response)
#syntax:def function_name(request,**kwargs):........return render-to response('show.html',{'username':'brahma'})
#creating urls:the entry point for every django application is always and url.to create the urls and their appropriate functions use url mapping file(urls.py).in urls.py all the url pattrens will enclosed by a list named as url patterens.use a method named as url(). to create an url pattern.
#every url pattern contains 2 parameters there are 1)regular expresion pattern 2)function in view.while creating regular expresion pattern the below symbols will play a major role.^:start of the url expresion pattern,$:end of the url epresion patternwith out extension,/:end of the url pattern with etension,/d:single number,/d+:multiple numbers,/w:single character,/w+:multiple characters,[]:range of values,{}:no:of elements.
#template tags:to manipulate the db data in front end we will use django template tags.
#tag to display the data:use '{{}}'' brackets in html page to display the content of variable.syntax:{{field_name}}.ex:{{data.emp_id}}.here data is an obect.
#conditions:django html condition will look similar to python condotions.in python ex:if (condition)........in html ex:{% if (condition)%}.......{%endif%}
#looping:in python ex:for variable in group of list.............in html{%for ele in group of ele%}........{%endfor%} 
# manage.py:djangoutility,urls.py:accessing the parent class data from child object.to put the condition on parent class fields we will use foregn key field along with parent field name joined by '__'ex:obj=Employe.objects.get(person_details__name='hari') ex2:obj=employe.objectsfilter(person_details__age__lt=25)
