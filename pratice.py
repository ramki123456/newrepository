class A:
	x=10
	y=20
	l=[1,2,3,4]
obj=A()
print obj.x
print obj.y
print obj.l
class Emp:
	x=10
	y=20
	def add(self,a,b):
		return a+b
obj=Emp()
print obj.x
print obj.add(20,30)
print obj.y
class A:
	x=20
	y=30
	def add(self,a,b):
		return a+b
		print self.x+self.y
obj=A()
print obj.x
print obj.y
print obj.add(10,40)
class A:
	x=20
	def xxx(self):
		print 'iam in A'
class B(A):
	y=200
	def yyy(self):
		print 'iam in B'
obj=B()
obj.xxx()
print obj.x
print obj.y
obj.yyy()
class A():
	x=10
	def xxx(self):
		print 'iam in A'
class B():
	y=20
	def yyy(self):
		print 'iam in B'
class C(A,B):
	z=30
	def zzz(self):
		print 'iam in C'
obj=C()
print obj.x
obj.xxx()
obj.zzz()
obj.yyy()
class A(object):
	def xyz(self):
		print 'iam in A'
class B(A):
	def xyz(self):
		super (B,self).xyz()
obj=B()
obj.xyz()
class A:
	def add(self,a,b):
		return a+b
	def __sub(self,a,b):
		return a-b
	x=10
	__y=20
obj=A()
print obj.add(10,20)
print obj._A__sub(20,10)
print obj.x
print obj._A__y