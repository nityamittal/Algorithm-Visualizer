import random
import time
import pygame
import networkx as nx
import matplotlib.pyplot as plt
import sys

def bubbleSortVisual():
    pygame.font.init()
    startTime = time.time()

    screen = pygame.display.set_mode((800, 700))

    pygame.display.set_caption("BUBBLE SORTING VISUALISER")

    run = True

    width = 800
    length = 700
    array = [0] * 151
    arr_clr = [(0, 204, 102)] * 151
    clr_ind = 0
    clr = [(0, 204, 102), (255, 0, 0),
        (0, 0, 153), (255, 102, 0)]
    fnt = pygame.font.SysFont("comicsans", 30)
    fnt1 = pygame.font.SysFont("comicsans", 20)

    def generate_arr():
        for i in range(1, 151):
            arr_clr[i] = clr[0]
            array[i] = random.randrange(1, 100)

    generate_arr()

    def refill():
        screen.fill((255, 255, 255))
        draw()
        pygame.display.update()
        pygame.time.delay(3)

    def bubbleSort(array,check):
        
        for i in range(1, len(array)):
            pygame.event.pump()
            refill()
            for j in range(1, len(array)-i):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        check = 0
                        return
                arr_clr[j] = clr[2]
                if (array[j] > array[j+1]):
                    array[j], array[j+1] = array[j+1], array[j]
                refill()
                arr_clr[j] = clr[0]
                arr_clr[j+1] = clr[2]
            arr_clr[len(array)-i] = clr[3]


    def draw():
        txt = fnt.render("SORT: PRESS 'ENTER'",
                        1, (0, 0, 0))
        screen.blit(txt, (20, 20))
        txt1 = fnt.render("NEW ARRAY: PRESS 'R'",
                        1, (0, 0, 0))
        screen.blit(txt1, (20, 40))
        txt2 = fnt1.render("ALGORITHM USED:"
                        "BUBBLE SORT", 1, (0, 0, 0))
        screen.blit(txt2, (500, 60))
        element_width = (width - 150) // 150
        boundry_arr = 800 / 150
        boundry_grp = 500 / 100
        pygame.draw.line(screen, (0, 0, 0), (0, 95),
                        (800, 95), 6)

        for i in range(1, 151):
            pygame.draw.line(screen, arr_clr[i],
                            (boundry_arr * i - 3, 100),
                            (boundry_arr * i - 3,
                            array[i] * boundry_grp + 100), element_width)

    check = 1
    while run:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    generate_arr()
                if event.key == pygame.K_RETURN:
                    bubbleSort(array,check)
        if(check):
            draw()
            pygame.display.update()

    pygame.quit()
    

def insertionSortVisual():
    pygame.font.init()
    startTime = time.time()

    screen = pygame.display.set_mode((800, 700))

    pygame.display.set_caption("INSERTION SORTING VISUALISER")

    run = True

    width = 800
    length = 800
    array = [0] * 151
    arr_clr = [(0, 204, 102)] * 151
    clr_ind = 0
    clr = [(0, 204, 102), (255, 0, 0), \
        (0, 0, 153), (255, 102, 0)]
    fnt = pygame.font.SysFont("comicsans", 30)
    fnt1 = pygame.font.SysFont("comicsans", 20)


    def generate_arr():
        for i in range(1, 151):
            arr_clr[i] = clr[0]
            array[i] = random.randrange(1, 100)

    generate_arr()

    def refill():
        screen.fill((255, 255, 255))
        draw()
        pygame.display.update()
        pygame.time.delay(3)

    def insertionSort(array,check):
        for i in range(1, len(array)):
            pygame.event.pump()
            refill()
            key = array[i]
            arr_clr[i] = clr[2]
            j = i - 1
            while j >= 0 and key < array[j]:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        check = 0
                        return
                arr_clr[j] = clr[2]
                array[j + 1] = array[j]
                refill()
                arr_clr[j] = clr[3]
                j = j - 1
            array[j + 1] = key
            refill()
            arr_clr[i] = clr[0]


    def draw():
        txt = fnt.render("SORT: PRESS 'ENTER'", \
                        1, (0, 0, 0))
        screen.blit(txt, (20, 20))
        txt1 = fnt.render("NEW ARRAY: PRESS 'R'", \
                        1, (0, 0, 0))
        screen.blit(txt1, (20, 40))
        txt2 = fnt1.render("ALGORITHM USED:" \
                        "INSERTION SORT", 1, (0, 0, 0))
        screen.blit(txt2, (500, 60))
        element_width = (width - 150) // 150
        boundry_arr = 800 / 150
        boundry_grp = 500 / 100
        pygame.draw.line(screen, (0, 0, 0), (0, 95), \
                        (800, 95), 6)

        for i in range(1, 151):
            pygame.draw.line(screen, arr_clr[i], \
                            (boundry_arr * i - 3, 100), \
                            (boundry_arr * i - 3, \
                            array[i] * boundry_grp + 100), element_width)

    check = 1
    while run:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    generate_arr()
                if event.key == pygame.K_RETURN:
                    insertionSort(array,check)
        if(check):
            draw()
            pygame.display.update()

    pygame.quit()

def selectionSortVisual():
    pygame.font.init()

    screen = pygame.display.set_mode((800, 700))

    pygame.display.set_caption("SELECTION SORTING VISUALISER")

    run = True

    width = 800
    length = 700
    array = [0] * 151
    arr_clr = [(0, 204, 102)] * 151
    clr_ind = 0
    clr = [(0, 204, 102), (255, 0, 0),
        (0, 0, 153), (255, 102, 0)]
    fnt = pygame.font.SysFont("comicsans", 30)
    fnt1 = pygame.font.SysFont("comicsans", 20)


    def generate_arr():
        for i in range(1, 151):
            arr_clr[i] = clr[0]
            array[i] = random.randrange(1, 100)

    generate_arr()

    def refill():
        screen.fill((255, 255, 255))
        draw()
        pygame.display.update()
        pygame.time.delay(3)

    def selectionSort(array,check):
        
        for i in range(1, len(array)):
            pygame.event.pump()
            arr_clr[i] = clr[3]
            refill()
            for j in range(i, len(array)):
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        check = 0
                        return
                arr_clr[i] = clr[3]
                arr_clr[j] = clr[0]
                if (j+1 <= len(array)-1):
                    arr_clr[j+1] = clr[2]
                if (array[i] > array[j]):
                    array[j], array[i] = array[i], array[j]
                    refill()


    def draw():
        txt = fnt.render("SORT: PRESS 'ENTER'",
                        1, (0, 0, 0))
        screen.blit(txt, (20, 20))
        txt1 = fnt.render("NEW ARRAY: PRESS 'R'",
                        1, (0, 0, 0))
        screen.blit(txt1, (20, 40))
        txt2 = fnt1.render("ALGORITHM USED:"
                        "SELECTION SORT", 1, (0, 0, 0))
        screen.blit(txt2, (500, 60))
        element_width = (width - 150) // 150
        boundry_arr = 800 / 150
        boundry_grp = 500 / 100
        pygame.draw.line(screen, (0, 0, 0), (0, 95),
                        (800, 95), 6)

        for i in range(1, 151):
            pygame.draw.line(screen, arr_clr[i],
                            (boundry_arr * i - 3, 100),
                            (boundry_arr * i - 3,
                            array[i] * boundry_grp + 100), element_width)

    check = 1
    while run:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    generate_arr()
                if event.key == pygame.K_RETURN:
                    selectionSort(array,check)
        
        if(check):
            draw()
            pygame.display.update()

    pygame.quit()

def binaryVisual():
    pygame.font.init()
    startTime = time.time()

    screen = pygame.display.set_mode((900, 650))

    pygame.display.set_caption("BINARY SEARCH VISUALISER")

    run = True

    width = 900
    length = 900
    array = [0] * 151
    key = 0
    foundkey = False

    arr_clr = [(0, 204, 102)] * 151
    clr_ind = 0

    clr = [(0, 204, 102), (255, 0, 0),
        (0, 0, 153), (255, 102, 0)]

    bigfont = pygame.font.SysFont("comicsans", 70)
    fnt = pygame.font.SysFont("comicsans", 30)
    fnt1 = pygame.font.SysFont("comicsans", 40)

    def heapSort(array):
        n = len(array)

        for i in range(n // 2 - 1, -1, -1):
            heapify(array, i, n)

        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            heapify(array, 0, i)


    def heapify(array, root, size):
        left = root * 2 + 1
        right = root * 2 + 2
        largest = root

        if left < size and array[left] > array[largest]:
            largest = left

        if right < size and array[right] > array[largest]:
            largest = right

        if largest != root:
            array[largest], array[root] = array[root], array[largest]
            heapify(array, largest, size)


    def generate_arr():
        for i in range(1, 151):
            arr_clr[i] = clr[0]
            array[i] = random.randrange(1, 100)
        heapSort(array)

    generate_arr()

    def refill():
        screen.fill((255, 255, 255))
        draw()
        pygame.display.update()
        pygame.time.delay(200)

    def binarySearch(array, key):
        left = 0
        right = len(array) - 1

        while left < right:
            arr_clr[left] = clr[1]
            arr_clr[right] = clr[1]
            refill()
            refill()
            mid = left + (right - left) // 2

            if array[mid] == key:
                arr_clr[left] = clr[0]
                arr_clr[right] = clr[0]
                arr_clr[mid] = clr[2]
                return 1

            elif array[mid] < key:
                arr_clr[left] = clr[0]
                left = mid + 1

            else:
                arr_clr[right] = clr[0]
                right = mid - 1
            refill()
        arr_clr[left] = clr[0]
        arr_clr[right] = clr[0]
        refill()
        return -1

    def draw():
        txt = fnt.render("SEARCH: PRESS 'ENTER'",
                        1, (0, 0, 0))

        screen.blit(txt, (550, 20))
        txt1 = fnt.render("NEW ARRAY: PRESS 'R'",
                        1, (0, 0, 0))
        screen.blit(txt1, (550, 40))
        txt2 = fnt1.render("ENTER NUMBER TO SEARCH:" +
                        str(key), 1, (0, 0, 0))
        screen.blit(txt2, (20, 60))
        element_width = (width - 150) // 150
        boundry_arr = 900 / 150
        boundry_grp = 550 / 100
        pygame.draw.line(screen, (0, 0, 0), (0, 95),
                        (900, 95), 6)

        for i in range(1, 151):
            pygame.draw.line(screen, arr_clr[i],
                            (boundry_arr * i - 3, 100),
                            (boundry_arr * i - 3,
                            array[i] * boundry_grp + 100), element_width)
        if foundkey == 1:
            text4 = bigfont.render("Key Found. Press N to Reset Key", 1, (0, 0, 0))
            screen.blit(text4, (100, 300))

        elif foundkey == -1:
            text4 = bigfont.render(
                "Key Not Found. Press N to Reset Key", 1, (0, 0, 0))
            screen.blit(text4, (30, 300))

    while run:

        screen.fill((255, 255, 255))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    key = 0
                    foundkey = 0
                    generate_arr()
                if event.key == pygame.K_n:
                    foundkey = 0
                    key = 0
                    for i in range(0, len(array)):
                        arr_clr[i] = clr[0]
                if event.key == pygame.K_RETURN and key != 0:
                    foundkey = binarySearch(array, key)
                if event.key == pygame.K_0:
                    key = key * 10
                if event.key == pygame.K_1:
                    key = key * 10 + 1
                if event.key == pygame.K_2:
                    key = key * 10 + 2
                if event.key == pygame.K_3:
                    key = key * 10 + 3
                if event.key == pygame.K_4:
                    key = key * 10 + 4
                if event.key == pygame.K_5:
                    key = key * 10 + 5
                if event.key == pygame.K_6:
                    key = key * 10 + 6
                if event.key == pygame.K_7:
                    key = key * 10 + 7
                if event.key == pygame.K_8:
                    key = key * 10 + 8
                if event.key == pygame.K_9:
                    key = key * 10 + 9
        draw()
        pygame.display.update()

    pygame.quit()

def mergeSortVisual():
    pygame.font.init()

    screen = pygame.display.set_mode((800, 700))

    pygame.display.set_caption("MERGE SORTING VISUALISER")

    run = True

    # Window size
    width = 800
    length = 700
    array = [0] * 151
    arr_clr = [(0, 204, 102)] * 151
    clr_ind = 0
    clr = [(0, 204, 102), (255, 0, 0),(0, 0, 153), (255, 102, 0)]
    fnt = pygame.font.SysFont("comicsans", 30)
    fnt1 = pygame.font.SysFont("comicsans", 20)

    # Generate new Array
    def generate_arr():
        for i in range(1, 151):
            arr_clr[i] = clr[0]
            array[i] = random.randrange(1, 100)

    generate_arr()

    def refill():
        screen.fill((255, 255, 255))
        draw()
        pygame.display.update()
        pygame.time.delay(5)

    def mergesort(array, l, r):
        mid = (l + r) // 2
        if l < r:
            mergesort(array, l, mid)
            mergesort(array, mid + 1, r)
            merge(array, l, mid,
                mid + 1, r)

    def merge(array, x1, y1, x2, y2):
        i = x1
        j = x2
        temp = []
        pygame.event.pump()
        while i <= y1 and j <= y2:
            arr_clr[i] = clr[1]
            arr_clr[j] = clr[1]
            refill()
            arr_clr[i] = clr[0]
            arr_clr[j] = clr[0]
            if array[i] < array[j]:
                temp.append(array[i])
                i += 1
            else:
                temp.append(array[j])
                j += 1
        while i <= y1:
            arr_clr[i] = clr[1]
            refill()
            arr_clr[i] = clr[0]
            temp.append(array[i])
            i += 1
        while j <= y2:
            arr_clr[j] = clr[1]
            refill()
            arr_clr[j] = clr[0]
            temp.append(array[j])
            j += 1
        j = 0
        for i in range(x1, y2 + 1):
            pygame.event.pump()
            array[i] = temp[j]
            j += 1
            arr_clr[i] = clr[2]
            refill()
            if y2 - x1 == len(array) - 2:
                arr_clr[i] = clr[3]
            else:
                arr_clr[i] = clr[0]

            # Draw the array values

    def draw():
        txt = fnt.render("PRESS" \
                        " 'ENTER' TO PERFORM SORTING.", 1, (0, 0, 0))

        screen.blit(txt, (20, 20))
        txt1 = fnt.render("PRESS 'R' FOR NEW ARRAY.",1, (0, 0, 0))
        screen.blit(txt1, (20, 40))
        txt2 = fnt1.render("ALGORITHM USED: " \
                        "MERGE SORT", 1, (0, 0, 0))

        screen.blit(txt2, (500, 60))
        element_width = (width - 150) // 150
        boundry_arr = 800 / 150
        boundry_grp = 550 / 100
        pygame.draw.line(screen, (0, 0, 0),(0, 95), (800, 95), 6)

        for i in range(1, 151):
            pygame.draw.line(screen, arr_clr[i], \
                            (boundry_arr * i - 3, 100), \
                            (boundry_arr * i - 3, array[i] * boundry_grp + 100), \
                            element_width)

    check = 1
    while run:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    generate_arr()
                if event.key == pygame.K_RETURN:
                    mergesort(array, 1, len(array) - 1)
        draw()
        pygame.display.update()

    pygame.quit()

def quickSortVisual():
    pygame.font.init()

    screen = pygame.display.set_mode((800, 700))
    pygame.display.set_caption("QUICK SORTING VISUALISER")

    run = True

    # Window size and some initials
    width = 800
    length = 600
    array = [0] * 151
    arr_clr = [(0, 204, 102)] * 151
    clr_ind = 0
    clr = [(0, 204, 102), (255, 0, 0), \
        (0, 0, 153), (255, 102, 0)]
    fnt = pygame.font.SysFont("comicsans", 30)
    fnt1 = pygame.font.SysFont("comicsans", 20)

    # Function to generate new Array
    def generate_arr():
        for i in range(1, 151):
            arr_clr[i] = clr[0]
            array[i] = random.randrange(1, 100)

        # Intially generate a array

    generate_arr()

    # Function to refill the
    # updates on the window
    def refill():
        screen.fill((255, 255, 255))
        draw()
        pygame.display.update()
        pygame.time.delay(8)

    # Sorting Algo:Quick sort
    def quicksort(array, l, r):
        if l < r:
            pi = partition(array, l, r)
            quicksort(array, l, pi - 1)
            refill()
            for i in range(0, pi + 1):
                arr_clr[i] = clr[3]
            quicksort(array, pi + 1, r)

        # Function to partition the array

    def partition(array, low, high):
        pygame.event.pump()
        pivot = array[high]
        arr_clr[high] = clr[2]
        i = low - 1
        for j in range(low, high):
            arr_clr[j] = clr[1]
            refill()
            arr_clr[high] = clr[2]
            arr_clr[j] = clr[0]
            arr_clr[i] = clr[0]
            if array[j] < pivot:
                i = i + 1
                arr_clr[i] = clr[1]
                array[i], array[j] = array[j], array[i]
        refill()
        arr_clr[i] = clr[0]
        arr_clr[high] = clr[0]
        array[i + 1], array[high] = array[high], array[i + 1]

        return (i + 1)

    # Function to Draw the
    # array values
    def draw():
        # Text should be rendered
        txt = fnt.render("SORT : PRESS 'ENTER'", \
                        1, (0, 0, 0))

        # Position where text is placed
        screen.blit(txt, (20, 20))
        txt1 = fnt.render("NEW ARRAY : PRESS 'R'", \
                        1, (0, 0, 0))
        screen.blit(txt1, (20, 40))
        txt2 = fnt1.render("ALGORITHM USED: QUICK SORT", \
                        1, (0, 0, 0))
        screen.blit(txt2, (500, 60))
        element_width = (width - 150) // 150
        boundry_arr = 800 / 150
        boundry_grp = 550 / 100
        pygame.draw.line(screen, (0, 0, 0), \
                        (0, 95), (800, 95), 6)

        # Drawing the array values as lines
        for i in range(1, 151):
            pygame.draw.line(screen, \
                            arr_clr[i], (boundry_arr * i - 3, 100), \
                            (boundry_arr * i - 3, \
                            array[i] * boundry_grp + 100), \
                            element_width)

        # Program should be run

    # continuously to keep the window open
    while run:
        # background
        screen.fill((255, 255, 255))

        # Event handler stores all event
        for event in pygame.event.get():

            # If we click Close button in window
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    generate_arr()
                if event.key == pygame.K_RETURN:
                    quicksort(array, 1, len(array) - 1)
        draw()
        pygame.display.update()

    pygame.quit()

def heapSortVisual():
    pygame.font.init()
    startTime = time.time()

    screen = pygame.display.set_mode((800, 700))

    pygame.display.set_caption("HEAP SORTING VISUALISER")

    run = True

    width = 800
    length = 700
    array = [0]*151
    arr_clr = [(0, 204, 102)]*151
    clr_ind = 0
    clr = [(0, 204, 102), (255, 0, 0),
        (0, 0, 153), (255, 102, 0)]
    fnt = pygame.font.SysFont("comicsans", 30)
    fnt1 = pygame.font.SysFont("comicsans", 20)

    def generate_arr():
        for i in range(1, 151):
            arr_clr[i] = clr[0]
            array[i] = random.randrange(1, 100)

    generate_arr()

    def refill():
        screen.fill((255, 255, 255))
        draw()
        pygame.display.update()
        pygame.time.delay(10)

    def heapSort(array,check):
        n = len(array)
        for i in range(n//2-1, -1, -1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    check = 0
                    return
            pygame.event.pump()
            heapify(array, i, n)
        for i in range(n-1, 0, -1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    check = 0
                    return
            array[i], array[0] = array[0], array[i]
            arr_clr[i] = clr[1]
            refill()
            heapify(array, 0, i)

    def heapify(array, root, size):
        left = root * 2 + 1
        right = root * 2 + 2
        largest = root
        if left < size and array[left] > array[largest]:
            largest = left
        if right < size and array[right] > array[largest]:
            largest = right
        if largest != root:
            arr_clr[largest] = clr[2]
            arr_clr[root] = clr[2]
            array[largest],\
            array[root] = array[root],\
            array[largest]
            refill()
            arr_clr[largest] = clr[0]
            arr_clr[root] = clr[0]
            heapify(array, largest, size)
            refill()

    def draw():

        txt = fnt.render("SORT: PRESS 'ENTER'",
                        1, (0, 0, 0))
        screen.blit(txt, (20, 20))
        txt1 = fnt.render("NEW ARRAY: PRESS 'R'",
                        1, (0, 0, 0))
        screen.blit(txt1, (20, 40))
        txt2 = fnt1.render("ALGORITHM USED:" +
                        "HEAP SORT", 1, (0, 0, 0))
        screen.blit(txt2, (500, 60))
        element_width = (width-150)//150
        boundry_arr = 800 / 150
        boundry_grp = 500 / 100
        pygame.draw.line(screen, (0, 0, 0), (0, 95),
                        (800, 95), 6)

        # Drawing the array values as lines
        for i in range(1, 151):
            pygame.draw.line(screen, arr_clr[i],
                            (boundry_arr * i-3, 100),
                            (boundry_arr * i-3,
                            array[i]*boundry_grp + 100),\
                            element_width)

    check = 1
    while run:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    generate_arr()
                if event.key == pygame.K_RETURN:
                    heapSort(array,check)
        if(check):
            draw()
            pygame.display.update()

    pygame.quit()


def linearVisual():
    ch = 1
    while(ch >= 1 and ch <= 7):
        print("")
        print("Enter 1 to visualize Bubble Sort")
        print("Enter 2 to visualize Insertion Sort")
        print("Enter 3 to visualize Selection Sort")
        print("Enter 4 to visualize Binary Search")
        print("Enter 5 to visualize Merge Sort")
        print("Enter 6 to visualize Quick Sort")
        print("Enter 7 to visualize Heap Sort")
        print("Any another number for main menu")
        ch = int(input())

        if(ch == 1):
            bubbleSortVisual()
        elif (ch == 2):
            insertionSortVisual()
        elif (ch==3):
            selectionSortVisual()
        elif (ch==4):
            binaryVisual()
        elif (ch==5):
            mergeSortVisual()
        elif (ch==6):
            quickSortVisual()
        elif (ch==7):
            heapSortVisual()
        else:
            break
        
def bfsVisual():
    print("Breadth first traversal")
    # BFS traversal
    def BFS(G, source, pos):
        visited = [False]*(len(G.nodes()))
        queue = []  # a queue for BFS traversal
        queue.append(source)
        visited[source] = True
        while queue:
            curr_node = queue.pop(0)
            for i in G[curr_node]:  # iterates through all the possible vertices adjacent to the curr_node
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    nx.draw_networkx_edges(G, pos, edgelist = [(curr_node,i)], width = 2.5, alpha = 0.6, edge_color = 'r')
        return

    # takes input and creates a weighted graph
    def CreateGraph():
        G = nx.DiGraph()
        print("Enter the no of nodes : ")
        n = int(input())
        wtMatrix = []
        print("Input the adjacency matrix : ")
        for i in range(n):
            list1 = [None]*n
            list1 = [int(x) for x in input().split()]
            # list1.append(input().split)
            wtMatrix.append(list1)
        print("Enter the source vertex : ")
        source = int(input())  # source vertex from where BFS has to start
        # Adds egdes along with their weights to the graph
        for i in range(n):
            for j in range(n):
                if wtMatrix[i][j] > 0:
                    G.add_edge(i, j, length=wtMatrix[i][j])
        return G, source

    # draws the graph and displays the weights on the edges
    def DrawGraph(G):
        pos = nx.spring_layout(G)
        # with_labels=true is to show the node number in the output graph
        nx.draw(G, pos, with_labels=True)
        edge_labels = dict([((u, v,), d['length'])
                            for u, v, d in G.edges(data=True)])
        # prints weight on all the edges
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=11)
        return pos

    G, source = CreateGraph()
    pos = DrawGraph(G)
    BFS(G, source, pos)
    plt.show()

def dfsVisual():
    print("Depth first traversal")
    
    # utility fucntion used by DFS which does recursive depth first search
    def DFSUtil(G, v, visited, sl):
        visited[v] = True
        sl.append(v)
        for i in G[v]:
            if visited[i] == False:
                DFSUtil(G, i, visited, sl)
        return sl

    # DFS traversal
    def DFS(G, source):
        visited = [False]*(len(G.nodes()))
        sl = []  # a list that stores dfs forest starting with source node
        dfs_stk = []  # A nested list that stores all the DFS Forest's
        dfs_stk.append(DFSUtil(G, source, visited, sl))
        for i in range(len(G.nodes())):
            if visited[i] == False:
                sl = []
                dfs_stk.append(DFSUtil(G, i, visited, sl))
        return dfs_stk

    # takes input and creates a weighted graph
    def CreateGraph():
        G = nx.DiGraph()
        print("Enter the no of nodes : ")
        n = int(input())
        wtMatrix = []
        print("Input the adjacency matrix : ")
        for i in range(n):
            list1 = [None]*n
            list1 = [int(x) for x in input().split()]

            wtMatrix.append(list1)
        print("Enter the source vertex : ")
        source = int(input())  # source vertex from where DFS has to start
        # Adds egdes along with their weights to the graph
        for i in range(n):
            for j in range(n):
                if wtMatrix[i][j] > 0:
                    G.add_edge(i, j, length=wtMatrix[i][j])
        return G, source

    # marks all edges traversed through DFS with red
    def DrawDFSPath(G, dfs_stk):
        pos = nx.spring_layout(G)
        # with_labels=true is to show the node number in the output graph
        nx.draw(G, pos, with_labels=True)
        edge_labels = dict([((u, v,), d['length'])
                            for u, v, d in G.edges(data=True)])
        # prints weight on all the edges
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=11)
        for i in dfs_stk:
            # if there is more than one node in the dfs-forest, then print the corresponding edges
            if len(i) > 1:
                for j in i[:(len(i)-1)]:
                    if i[i.index(j)+1] in G[j]:
                        nx.draw_networkx_edges(
                            G, pos, edgelist=[(j, i[i.index(j)+1])], width=2.5, alpha=0.6, edge_color='r')
                    else:
                        # if in case the path was reversed because all the possible neighbours were visited, we need to find the adj node to it.
                        for k in i[1::-1]:
                            if k in G[j]:
                                nx.draw_networkx_edges(
                                    G, pos, edgelist=[(j, k)], width=2.5, alpha=0.6, edge_color='r')
                                break

    G, source = CreateGraph()
    dfs_stk = DFS(G, source)
    DrawDFSPath(G, dfs_stk)
    plt.show()

def kruskalVisual():
    
    print("Kruskal's Algorithm")
    # A utility function that return the smallest unprocessed edge
    def getMin(G, mstFlag):
        min = sys.maxsize  # assigning largest numeric value to min
        for i in [(u, v, edata['length']) for u, v, edata in G.edges( data = True) if 'length' in edata ]:
            if mstFlag[i] == False and i[2] < min:
                min = i[2]
                min_edge = i
        return min_edge

    # A utility function to find root or origin of the node i in MST
    def findRoot(parent, i):
        if parent[i] == i:
            return i
        return findRoot(parent, parent[i])

    # A function that does union of set x and y based on the order
    def union(parent, order, x, y):
        xRoot = findRoot(parent, x)
        yRoot = findRoot(parent, y)
        # Attach smaller order tree under root of high order tree
        if order[xRoot] < order[yRoot]:
            parent[xRoot] = yRoot
        elif order[xRoot] > order[yRoot]:
            parent[yRoot] = xRoot
        # If orders are same, then make any one as root and increment its order by one
        else :
            parent[yRoot] = xRoot
            order[xRoot] += 1

    # function that performs Kruskals algorithm on the graph G
    def kruskals(G, pos):
        eLen = len(G.edges()) # eLen denotes the number of edges in G
        vLen = len(G.nodes()) # vLen denotes the number of vertices in G
        mst = [] # mst contains the MST edges
        mstFlag = {} # mstFlag[i] will hold true if the edge i has been processed for MST
        for i in [ (u, v, edata['length']) for u, v, edata in G.edges(data = True) if 'length' in edata ]:
            mstFlag[i] = False 

        parent = [None] * vLen # parent[i] will hold the vertex connected to i, in the MST
        order = [None] * vLen	# order[i] will hold the order of appearance of the node in the MST
        for v in range(vLen):
            parent[v] = v
            order[v] = 0
        while len(mst) < vLen - 1 :
            curr_edge = getMin(G, mstFlag) # pick the smallest egde from the set of edges
            mstFlag[curr_edge] = True # update the flag for the current edge
            y = findRoot(parent, curr_edge[1])
            x = findRoot(parent, curr_edge[0])
            # adds the edge to MST, if including it doesn't form a cycle
            if x != y:
                mst.append(curr_edge)
                union(parent, order, x, y)
            # Else discard the edge
        # marks the MST edges with red
        for X in mst:
            if (X[0], X[1]) in G.edges():
                nx.draw_networkx_edges(G, pos, edgelist = [(X[0], X[1])], width = 2.5, alpha = 0.6, edge_color = 'r')
        return

    # takes input from the file and creates a weighted graph
    def CreateGraph():
        G = nx.Graph()
        print("Enter the no of nodes : ")
        n = int(input())
        wtMatrix = []
        print("Input the adjacency matrix : ")
        for i in range(n):
            list1 = [None]*n
            list1 = [int(x) for x in input().split()]
            # list1.append(input().split)
            wtMatrix.append(list1)
        # Adds egdes along with their weights to the graph 
        for i in range(n) :
            for j in range(n)[i:] :
                if wtMatrix[i][j] > 0 :
                        G.add_edge(i, j, length = wtMatrix[i][j]) 
        return G

    # draws the graph and displays the weights on the edges
    def DrawGraph(G):
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels = True)  # with_labels=true is to show the node number in the output graph
        edge_labels = nx.get_edge_attributes(G, 'length')
        nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 11) #    prints weight on all the edges
        return pos

    G = CreateGraph()
    pos = DrawGraph(G)
    kruskals(G, pos)
    plt.show()

def dijkstraVisual():
    
    print("Dijkstra's Algorithm")
    #utility function that returns the minimum distance node
    def minDistance(dist, sptSet, V):
        min = sys.maxsize #assigning largest numeric value to min
        for v in range(V):
            if sptSet[v] == False and dist[v] <= min:
                min = dist[v]
                min_index = v
        return min_index

    #function that performs dijsktras algorithm on the graph G,with source vertex as source
    def dijsktras(G, source, pos):
        V = len(G.nodes()) # V denotes the number of vertices in G
        dist = [] # dist[i] will hold the shortest distance from source to i
        parent = [None]*V # parent[i] will hold the node from which i is reached to, in the shortest path from source
        sptSet = [] # sptSet[i] will hold true if vertex i is included in shortest path tree
        #initially, for every node, dist[] is set to maximum value and sptSet[] is set to False
        for i in range(V):
            dist.append(sys.maxsize)
            sptSet.append(False)
        dist[source] = 0
        parent[source]= -1 #source is itself the root, and hence has no parent
        for count in range(V-1):
            u = minDistance(dist, sptSet, V) #pick the minimum distance vectex from the set of vertices
            sptSet[u] = True
            #update the vertices adjacent to the picked vertex
            for v in range(V):
                if (u, v) in G.edges():
                    if sptSet[v] == False and dist[u] != sys.maxsize and dist[u] + G[u][v]['length'] < dist[v]:
                        dist[v] = dist[u] + G[u][v]['length']
                        parent[v] = u
        #marking the shortest path from source to each of the vertex with red, using parent[]
        for X in range(V):
            if parent[X] != -1: #ignore the parent of root node 
                if (parent[X], X) in G.edges():
                    nx.draw_networkx_edges(G, pos, edgelist = [(parent[X], X)], width = 2.5, alpha = 0.6, edge_color = 'r')
        return

    #takes input from the file and creates a weighted graph
    def CreateGraph():
        G = nx.DiGraph()
        print("Enter the no of nodes : ")
        n = int(input())
        wtMatrix = []
        print("Input the adjacency matrix : ")
        for i in range(n):
            list1 = [None]*n
            list1 = [int(x) for x in input().split()]
            # list1.append(input().split)
            wtMatrix.append(list1)
        print("Enter the source vertex : ")
        source = int(input()) #source vertex for dijsktra's algo 
        #Adds egdes along with their weights to the graph 
        for i in range(n) :
            for j in range(n) :
                if wtMatrix[i][j] > 0 :
                        G.add_edge(i, j, length = wtMatrix[i][j]) 
        return G, source

    #draws the graph and displays the weights on the edges
    def DrawGraph(G):
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels = True)  #with_labels=true is to show the node number in the output graph
        edge_labels = dict([((u, v), d['length']) for u, v, d in G.edges(data = True)])
        nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, label_pos = 0.3, font_size = 11) #prints weight on all the edges
        return pos

    G,source = CreateGraph()
    pos = DrawGraph(G)
    dijsktras(G, source, pos)
    plt.show()

def primVisual():
    print("Prim's Algorithm")
    # utility function that returns the minimum egde weight node
    def minDistance(dist, mstSet, V):
        min = sys.maxsize  # assigning largest numeric value to min
        for v in range(V):
            if mstSet[v] == False and dist[v] < min:
                min = dist[v]
                min_index = v
        return min_index

    # function that performs prims algorithm on the graph G
    def prims(G, pos):
        V = len(G.nodes())  # V denotes the number of vertices in G
        dist = []  # dist[i] will hold the minimum weight edge value of node i to be included in MST
        # parent[i] will hold the vertex connected to i, in the MST edge
        parent = [None]*V
        mstSet = []  # mstSet[i] will hold true if vertex i is included in the MST
        # initially, for every node, dist[] is set to maximum value and mstSet[] is set to False
        for i in range(V):
            dist.append(sys.maxsize)
            mstSet.append(False)
        dist[0] = 0
        parent[0] = -1  # starting vertex is itself the root, and hence has no parent
        for count in range(V-1):
            # pick the minimum distance vertex from the set of vertices
            u = minDistance(dist, mstSet, V)
            mstSet[u] = True
            # update the vertices adjacent to the picked vertex
            for v in range(V):
                if (u, v) in G.edges():
                    if mstSet[v] == False and G[u][v]['length'] < dist[v]:
                        dist[v] = G[u][v]['length']
                        parent[v] = u
        for X in range(V):
            if parent[X] != -1:  # ignore the parent of the starting node
                if (parent[X], X) in G.edges():
                    nx.draw_networkx_edges(
                        G, pos, edgelist=[(parent[X], X)], width=2.5, alpha=0.6, edge_color='r')
        return

    # takes input from the file and creates a weighted graph
    def CreateGraph():
        G = nx.Graph()
        print("Enter the no of nodes : ")
        n = int(input())
        wtMatrix = []
        print("Input the adjacency matrix : ")
        for i in range(n):
            list1 = [None]*n
            list1 = [int(x) for x in input().split()]
            wtMatrix.append(list1)
        # Adds egdes along with their weights to the graph
        for i in range(n):
            for j in range(n)[i:]:
                if wtMatrix[i][j] > 0:
                    G.add_edge(i, j, length=wtMatrix[i][j])
        return G

    # draws the graph and displays the weights on the edges
    def DrawGraph(G):
        pos = nx.spring_layout(G)
        # with_labels=true is to show the node number in the output graph
        nx.draw(G, pos, with_labels=True)
        edge_labels = nx.get_edge_attributes(G, 'length')
        # prints weight on all the edges
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=11)
        return pos
        
    G = CreateGraph()
    pos = DrawGraph(G)
    prims(G, pos)
    plt.show()

def topologicalSortVisual():
    print("Topological Sort")

    def topologicalSort(G,pos):
        zero_indeg_list = [] 
        sorted_list = []
        visited = [False]*len(G.nodes())
        while len(G.nodes())!=0:
            for node in G.nodes():
                if visited[node-1] == False:
                    if G.in_degree(node) == 0:
                        visited[node-1] = True
                        zero_indeg_list.append(node)
            for node in zero_indeg_list:
                sorted_list.append(node)
                G.remove_node(node)
                zero_indeg_list.remove(node)
        return sorted_list
            
    #takes input from the file and creates a directed graph
    def CreateResultGraph(sorted_list):
        D = nx.DiGraph()
        for i in range(len(sorted_list)-1): 
            D.add_edge(sorted_list[i], sorted_list[i+1]) 
        pos = nx.spring_layout(D)
        val_map = {}
        val_map[sorted_list[0]] = 'green'
        val_map[sorted_list[len(sorted_list)-1]] = 'red'
        values = [val_map.get(node, 'blue') for node in D.nodes()]
        nx.draw(D, pos, with_labels = True, node_color =values)  

    #takes input from the file and creates a directed graph
    def CreateGraph():
        G = nx.DiGraph()
        print("Enter the no of nodes : ")
        n = int(input())
        wtMatrix = []
        print("Input the Edges : ")

        adj_list = [None]*2
        for i in range(n):
            adj_list = [int(x) for x in input().split()] 
            G.add_edge(adj_list[0], adj_list[1]) 
        return G

    #draws the graph
    def DrawGraph(G):
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels = True, node_color ='blue')  #with_labels=true is to show the node number in the output graph
        return pos

    G = CreateGraph()
    plt.figure(1)
    pos = DrawGraph(G)
    plt.figure(2)
    sorted_list = topologicalSort(G,pos)
    CreateResultGraph(sorted_list)
    plt.show()

def bellmanFordVisual():
    print("Bellman ford's algorithm")
    inf = float('inf')

    #function that performs Bellman-Ford algorithm on the graph G,with source vertex as source
    def bellmanFord(G, source, pos):
        V = len(G.nodes()) # V denotes the number of vertices in G
        dist = [] # dist[i] will hold the shortest distance from source to i
        parent = [None]*V # parent[i] will hold the node from which i is reached to, in the shortest path from source

        for i in range(V):
            dist.append(inf)

        parent[source] = -1; #source is itself the root, and hence has no parent
        dist[source] = 0;

        for i in range(V-1):
            for u, v, d in G.edges(data = True): # Relaxation is the most important step in Bellman-Ford. It is what increases the accuracy of the distance to any given vertex. Relaxation works by continuously shortening the calculated distance between vertices comparing that distance with other known distances.
                if dist[u] + d['length'] < dist[v]: #Relaxation Equation
                    dist[v] = d['length'] + dist[u]
                    parent[v] = u

        #marking the shortest path from source to each of the vertex with red, using parent[]
        for v in range(V):
            if parent[v] != -1: #ignore the parent of root node
                if (parent[v], v) in G.edges():
                    nx.draw_networkx_edges(G, pos, edgelist = [(parent[v], v)], width = 2.5, alpha = 0.6, edge_color = 'r')
        return

    #takes input from the file and creates a weighted graph
    def createGraph():
        G = nx.DiGraph()
        print("Enter the no of nodes : ")
        n = int(input())
        wtMatrix = []
        print("Input the adjacency matrix : ")
        for i in range(n):
            list1 = [None]*n
            list1 = [int(x) for x in input().split()]
            # list1.append(input().split)
            wtMatrix.append(list1)
        print("Enter the source vertex : ")
        source = int(input()) #source vertex for BellmanFord algo
        #Adds egdes along with their weights to the graph
        for i in range(n) :
            for j in range(n) :
                if wtMatrix[i][j] > 0 :
                        G.add_edge(i, j, length = wtMatrix[i][j])
        return G, source

    #draws the graph and displays the weights on the edges
    def DrawGraph(G):
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels = True)  #with_labels=true is to show the node number in the output graph
        edge_labels = dict([((u, v), d['length']) for u, v, d in G.edges(data = True)])
        nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, label_pos = 0.3, font_size = 11) #prints weight on all the edges
        return pos

    G, source = createGraph()
    pos = DrawGraph(G)
    bellmanFord(G, source, pos)
    plt.show()


def graphVisual():
    ch = 1
    while(ch >= 1 and ch <= 7):
        print("")
        print("Enter 1 to visualize Breadth first traversal")
        print("Enter 2 to visualize Depth first traversal")
        print("Enter 3 to visualize Kruskal's Algorithm")
        print("Enter 4 to visualize Dijkstra's Algorithm")
        print("Enter 5 to visualize Prim's Algorithm")
        print("Enter 6 to visualize Topological Sort")
        print("Enter 7 to visualize Bellman ford's algorithm")    
        print("Any another number for main menu")
        ch = int(input())
        if(ch == 1):
            bfsVisual()
        elif (ch == 2):
            dfsVisual()
        elif (ch==3):
            kruskalVisual()
        elif (ch==4):
            dijkstraVisual()
        elif (ch==5):
            primVisual()
        elif (ch==6):
            topologicalSortVisual()
        elif (ch==7):
            bellmanFordVisual()
        else:
            break

    # main function
if __name__ == "__main__":
    print("********** Array and Graph Visualization ***********")
    
    ch = 1
    while(ch == 1 or ch == 2):
        print("")
        print("Enter 1 for Array Visualization")
        print("Enter 2 for Graph Visualization")
        print("Any another number to exit")
        ch = int(input())

        if(ch == 1):
            linearVisual()
        elif (ch == 2):
            graphVisual()
        else:
            break
        

