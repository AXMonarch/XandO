import pygame,sys
pygame.init()

def wingame():

        #Win Conditions for Cross 
        
        #3 ACross (get it lol)
        if (xoneCh == False and xtwoCh == False and xthreeCh == False):
            pygame.exit()
            sys.exit()
        if (xfourCh == False and xfiveCh == False and xsixCh == False):
            pygame.exit()
            sys.exit()
        if (xsevenCh == False and xeightCh == False and xnineCh == False):
            pygame.exit()
            sys.exit()
        
        #3 Down
        if (xoneCh == False and xfourCh == False and xsevenCh == False):
            pygame.exit()
            sys.exit()
        if (xtwoCh == False and xfiveCh == False and xeightCh == False):
            pygame.exit()
            sys.exit()
        if (xthreeCh == False and xsixCh == False and xnineCh == False):
            pygame.exit()
            sys.exit()

        #2 Diagonal
        if (xoneCh == False and xfiveCh == False and xnineCh == False):
            pygame.exit()
            sys.exit()
        if (xthreeCh == False and xfiveCh == False and xsevenCh == False):
            pygame.exit()
            sys.exit()

        #Win Conditions for Nought

        #3 Across 
        if (oneCh == False and twoCh == False and threeCh == False):
            pygame.exit()
            sys.exit()
        if (fourCh == False and fiveCh == False and sixCh == False):
            pygame.exit()
            sys.exit()
        if (sevenCh == False and eightCh == False and nineCh == False):
            pygame.exit()
            sys.exit()
        
        #3 Down
        if (oneCh == False and fourCh == False and sevenCh == False):
            pygame.exit()
            sys.exit()
        if (twoCh == False and fiveCh == False and eightCh == False):
            pygame.exit()
            sys.exit()
        if (threeCh == False and sixCh == False and nineCh == False):
            pygame.exit()
            sys.exit()

        #2 Diagonal
        if (oneCh == False and fiveCh == False and nineCh == False):
            pygame.time.delay(5000)
            pygame.exit()
            sys.exit()
        if (threeCh == False and fiveCh == False and sevenCh == False):
            pygame.exit()
            sys.exit()

#Screen creation
pygame.display.set_caption('X and O')
screen = pygame.display.set_mode((400,400))

#Game assets
grid = pygame.image.load("Grid.jpg")
grid = pygame.transform.scale(grid, (400,400))

cross = pygame.image.load("Cross.png")
cross = pygame.transform.scale(cross,(55,55))

nought = pygame.image.load("Nought.png")
nought = pygame.transform.scale(nought,(55,55))

#Screen Update
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 100)

#Position Tuples
one = (40,40)
two = (175,40)
three = (300,40)
four = (40,175)
five = (175,175)
six = (300,175)
seven = (40,300)
eight = (175,300)
nine = (300,300)

#Turn Counter 
k = 0 

#checker for whether box is full (nought)
oneCh = True
twoCh = True
threeCh = True
fourCh = True
fiveCh = True
sixCh = True
sevenCh = True
eightCh = True
nineCh = True

#checker for whether box is full (cross)
xoneCh = True
xtwoCh = True
xthreeCh = True
xfourCh = True
xfiveCh = True
xsixCh = True
xsevenCh = True
xeightCh = True
xnineCh = True

#Win Checker 

#List of box "states"
boxstatelst = []

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.exit()
            sys.exit()

        #Key events for placing Xs and Os
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.blit(grid,(0,0))
            if event.key == pygame.K_1 and oneCh == True and xoneCh == True:
                if k % 2 == 0:
                    screen.blit(nought,one)
                    k += 1
                    oneCh = False
                    boxstatelst.append(oneCh)
                else:
                    screen.blit(cross,one)
                    k += 1
                    xoneCh = False
                    boxstatelst.append(xoneCh)
            if event.key == pygame.K_2 and twoCh == True and xtwoCh == True:
                if k % 2 == 0:
                    screen.blit(nought,two)
                    k += 1
                    twoCh = False
                    boxstatelst.append(twoCh)
                else:
                    screen.blit(cross,two)
                    k += 1
                    xtwoCh = False
                    boxstatelst.append(xtwoCh)
            if event.key == pygame.K_3 and threeCh == True and xthreeCh == True:
                if k % 2 == 0:
                    screen.blit(nought,three)
                    k += 1
                    threeCh = False
                    boxstatelst.append(threeCh)
                else:
                    screen.blit(cross,three)
                    k += 1
                    xthreeCh = False
                    boxstatelst.append(xthreeCh)
            if event.key == pygame.K_4 and fourCh == True and xfourCh == True:
                if k % 2 == 0:
                    screen.blit(nought,four)
                    k += 1
                    fourCh = False
                    boxstatelst.append(fourCh)
                else:
                    screen.blit(cross,four)
                    k += 1
                    xfourCh = False
                    boxstatelst.append(xfourCh)
            if event.key == pygame.K_5 and fiveCh == True and xfiveCh == True:
                if k % 2 == 0:
                    screen.blit(nought,five)
                    k += 1
                    fiveCh = False
                    boxstatelst.append(fiveCh)
                else:
                    screen.blit(cross,five)
                    k += 1
                    xfiveCh = False
                    boxstatelst.append(xfiveCh)
            if event.key == pygame.K_6 and sixCh == True and xsixCh == True:
                if k % 2 == 0:
                    screen.blit(nought,six)
                    k += 1
                    sixCh = False
                    boxstatelst.append(sixCh)
                else:
                    screen.blit(cross,six)
                    k += 1
                    xsixCh = False
                    boxstatelst.append(xsixCh)
            if event.key == pygame.K_7 and sevenCh == True and xsevenCh == True:
                if k % 2 == 0:
                    screen.blit(nought,seven)
                    k += 1
                    sevenCh = False
                    boxstatelst.append(sevenCh)
                else:
                    screen.blit(cross,seven)
                    k += 1
                    xsevenCh = False
                    boxstatelst.append(xsevenCh)
            if event.key == pygame.K_8 and eightCh == True and xeightCh == True:
                if k % 2 == 0:
                    screen.blit(nought,eight)
                    k += 1
                    eightCh = False
                    boxstatelst.append(eightCh)
                else:
                    screen.blit(cross,eight)
                    k += 1
                    xeightCh = False
                    boxstatelst.append(xeightCh)
            if event.key == pygame.K_9 and nineCh == True and xnineCh == True:
                if k % 2 == 0:
                    screen.blit(nought,nine)
                    k += 1
                    nineCh = False
                    boxstatelst.append(nineCh)
                else:
                    screen.blit(cross,nine)
                    k += 1
                    xnineCh = False
                    boxstatelst.append(xnineCh)
        

    pygame.display.update()
