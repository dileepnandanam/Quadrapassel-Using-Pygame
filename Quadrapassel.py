
import time,pygame,random,threading

class tetrix(threading.Thread) :
	def __init__(self) :
		
		super(tetrix, self).__init__()
		self.over=False
		self.score=0
		self.bricksize=20
		self.shape=-1
		self.lowspeed=0.5
		self.hispeed=0.05
		self.cspeed=self.lowspeed
		self.fall=False
		self.over=False
		self.score=0
		self.c=((10,10,10),(200,0,0),(0,200,0),(0,0,200),(200,200,0),(0,200,200),(200,200,200))
		self.row=25
		self.column=18
		
		self.raws= [ [ 0 for i in range(self.column) ] for j in range(self.row) ]
		self.b=[[0 for j in range(6)]for i in range(6)]
		pygame.init()
		self.screen=pygame.display.set_mode((self.bricksize*self.column-6*self.bricksize,self.bricksize*self.row))
		pygame.display.set_caption("Quadrapassel")
		pygame.display.flip()
		self.start()
		
	def speedup(self) :
		self.cspeed=self.hispeed
	def speeddown(self)	:
		self.cspeed=self.lowspeed			
	def  ckeckfilled(self) :
		filled=True
		i=0
		while i<self.row :
			filled=True
			j=3
			while j<self.column-3 :
				if self.raws[i][j]==0 :
					filled=False
				j=j+1
			if filled :
				self.score=self.score+10
				print "score:",self.score 
				p=i
				while p>0 :
					j=1
					while j<self.column-1 :
						self.raws[p][j]=self.raws[p-1][j]
						j=j+1
					p=p-1
			
			i=i+1
		
	
	
	def enterbrick(self) :
		self.bi=0
		self.bj=5
		self.shape=random.randint(1,6)
	
		i=0
		while i<6 :
			j=0
			while j<6 :
				self.b[i][j]=0
				j=j+1
			i=i+1
		if self.shape==1 :
		
			self.raws[2][6]=self.shape
			self.b[2][1]=1
			self.raws[2][7]=self.shape
			self.b[2][2]=1
			self.raws[2][8]=self.shape
			self.b[2][3]=1
			self.raws[2][9]=self.shape
			self.b[2][4]=1
		
		elif self.shape==2 :
		
			self.raws[3][6]=self.shape
			self.b[3][1]=1
			self.raws[3][7]=self.shape
			self.b[3][2]=1
			self.raws[3][8]=self.shape
			self.b[3][3]=1
			self.raws[2][8]=self.shape
			self.b[2][3]=1
		
		elif self.shape==3 :
		
			self.raws[2][6]=self.shape
			self.b[2][1]=1
			self.raws[2][7]=self.shape
			self.b[2][2]=1
			self.raws[2][8]=self.shape
			self.b[2][3]=1
			self.raws[1][7]=self.shape
			self.b[1][2]=1
		
		elif self.shape==4 :
		
			self.raws[2][6]=self.shape
			self.b[2][1]=1
			self.raws[2][7]=self.shape
			self.b[2][2]=1
			self.raws[3][7]=self.shape
			self.b[3][2]=1
			self.raws[3][8]=self.shape
			self.b[3][3]=1
		
		elif self.shape==5 :
		
			self.raws[2][7]=self.shape
			self.b[2][2]=1
			self.raws[2][8]=self.shape
			self.b[2][3]=1
			self.raws[3][7]=self.shape
			self.b[3][2]=1
			self.raws[3][8]=self.shape
			self.b[3][3]=1

		
		elif self.shape==6 :
		
			self.raws[3][6]=self.shape
			self.b[3][1]=1
			self.raws[3][7]=self.shape
			self.b[3][2]=1
			self.raws[3][8]=self.shape
			self.b[3][3]=1
			self.raws[2][6]=self.shape
			self.b[2][1]=1
		
		elif self.shape==7 :
		
			self.raws[2][7]=self.shape
			self.b[2][2]=1
			self.raws[2][8]=self.shape
			self.b[2][3]=1
			self.raws[3][6]=self.shape
			self.b[3][1]=1
			self.raws[3][7]=self.shape
			self.b[3][2]=1
		
		
	
	def downward(self) :
		
		i=1
		while i<=4 :
			j=1
			while j<=4 :
			
				if self.b[i][j]==1 :
				
					if i+self.bi==self.row-1 :
						self.fall=False
						return
					if self.b[i+1][j]==0 and self.raws[i+self.bi+1][j+self.bj]>0 :
						self.fall=False
						
						if self.bi==0 :
							self.over=True
							print "Game Over"
						return
				j=j+1		
			i=i+1
		i=5
		while i>=0 :
			j=0
			while j<=5 :
				if self.b[i][j]==1 :
					t=self.raws[i+self.bi][j+self.bj]
					self.raws[i+self.bi][j+self.bj]=self.raws[i+self.bi+1][j+self.bj]
					self.raws[i+self.bi+1][j+self.bj]=t
				j=j+1
			i=i-1
		self.bi=self.bi+1
	def move(self,direction) :
		allowm=True
		i=1
		while i<5 :
			j=1
			while j<5 :
				if self.b[i][j]==1 :
				
					if direction==-1 and j+self.bj==3 :
						allowm=False
						return
					
					elif direction==1 and j+self.bj==14 :
					
						allowm=False
						return
					
					elif self.b[i][j-1]==0 and self.raws[i+self.bi][j+self.bj-1]>0 and direction==-1 :
						allowm=False
						return
					elif self.b[i][j+1]==0 and self.raws[i+self.bi][j+self.bj+1]>0 and direction==1 :
						allowm=False
						return	
				
				j=j+1
			i=i+1
		if allowm==True :
			i=0
			while i<=5 :
				if direction==1 :
					j=5
					while j>=0 :
						if self.b[i][j]==1 :

							t=self.raws[i+self.bi][j+self.bj]
							self.raws[i+self.bi][j+self.bj]=self.raws[i+self.bi][j+1+self.bj]
							self.raws[i+self.bi][j+1+self.bj]=t
						j=j-1
				else :
					j=0
					while j<=5 :					
						if self.b[i][j]==1 :						
							t=self.raws[i+self.bi][j+self.bj]
							self.raws[i+self.bi][j+self.bj]=self.raws[i+self.bi][j-1+self.bj]
							self.raws[i+self.bi][j-1+self.bj]=t						
						j=j+1
				i=i+1
			if direction==1 :
				self.bj=self.bj+1
			elif direction==-1 :
				self.bj=self.bj-1
	
	def adjust(self) :
		i=0
		while i<6 :
			j=0
			while j<6 :
				if self.b[i][j]==1 :
					if j+self.bj==self.column-4 :
						direction=-1
						self.move(direction)
						i=0
						j=0
					elif j+self.bj==2 :
						direction=1
						self.move(direction)
						i=0
						j=0
				j=j+1
			i=i+1
	def rotate(self) :
		
		bt=[[self.b[5-j][i] for j in range(6)] for i in range(6)]
		
		
		allowr=True
		i=0
		while i<6 :
			j=0
			while j<6 :
				if bt[i][j]==1 and (self.raws[i+self.bi][j+self.bj]>0 and self.b[i][j]==0 or i+self.bi>self.row-1) :
					allowr=False
					break
				j=j+1
			i=i+1
		
		if allowr :
			
			i=0
			while i<6 :
				j=0
				while j<6 :
				
					if self.b[i][j]==1 or bt[i][j]==1 :
						self.raws[i+self.bi][j+self.bj]=self.shape*bt[i][j]
					self.b[i][j]=bt[i][j]
					j=j+1
				i=i+1
	
	
	def printscreen(self) :
		self.screen.fill((0,0,0))
		i=0
		
		while i<self.row :
			j=3
			while j<self.column-3 :
				pygame.draw.circle(self.screen,self.c[self.raws[i][j]],(j*self.bricksize-3*self.bricksize+self.bricksize/2,i*self.bricksize),self.bricksize/2,0)
				j=j+1
			i=i+1	
		pygame.display.flip()
		
				
	def run(self) :
		self.enterbrick()
		self.fall=True
		while not self.over :
			time.sleep(self.cspeed)
			if self.fall :	
				self.downward()	
			else :	
				self.ckeckfilled()
				self.enterbrick()
				self.fall=True
				self.speeddown()
			self.printscreen();
			

class eng(threading.Thread) :
	def run(self) :
		tet = tetrix()
		direction=0;	
		
		while not tet.over :
			
			time.sleep(0.1)
			for e in pygame.event.get() :
				if e.type==pygame.QUIT :
					pygame.display.quit()
					
					
				if tet.fall :
					if e.type==pygame.KEYDOWN :
						if e.key==pygame.K_DOWN :
							tet.speedup()
						
						if e.key==pygame.K_LEFT :
							tet.move(-1)
						
						
						if e.key==pygame.K_RIGHT :
							tet.move(1)
					
						if e.key==pygame.K_UP :
							tet.rotate()
							tet.adjust()
					
				
				
		

en= eng()
en.start()



