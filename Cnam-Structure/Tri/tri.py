import random
def tableau(taille, array):
    for i in range (taille):
        array.append(random.randrange(0,101,1))
    #endfor
#enddef

def tri_minimum(array):
    for i in range (len(array)):
        mini = i
        for j in range (i+1, len(array)):
            if (array[j] < array[mini]):
                mini = j
            #endif
        #endfor
        if (mini != i):
            tmp = array[mini]
            array[mini] = array[i]
            array[i] = tmp
        #endif
    #endfor
#enddef

def tri_insertion(array):
    for i in range (len(array)):
        x = array[i]
        j = i
        while (j > 0 and array[j - 1] > x):
            array[j] = array[j - 1]
            j -= 1
        #endwhile
        array[j] = x
    #endfor
#enddef

def tri_bulle(array):
    i = len(array)-1
    while (i >= 0):
        for j in range (i):
            if (array[j+1] < array[j]):
                tmp = array[j+1]
                array[j+1] = array[j]
                array[j] = tmp
            #endif
        #endfor
        i -=1
    #endwhile
#enddef

def tri_rapide(array):
    print('NIQUE TA MERE')
#endef

array_mini = []
tableau(10, array_mini)
print("Début : " + str(array_mini))
tri_minimum(array_mini)
print("Tri Mini : " + str(array_mini))
print("Tri minimum, complexité de N²")

print()

array_insert = []
tableau(10, array_insert)
print("Début : " + str(array_insert))
tri_insertion(array_insert)
print("Tri Insert : " + str(array_insert))
print("Tri par insertion, complexité de N²")

print()

array_bubble = []
tableau(10, array_bubble)
print("Début : " + str(array_bubble))
tri_bulle(array_bubble)
print("Tri à bulle : " + str(array_bubble))
print("Tri à bulle, complexité de N²")

print()

array_fast = []
tableau(10, array_fast)
print("Début : " + str(array_fast))
tri_rapide(array_fast)
print("Tri rapide : " + str(array_fast))
print("Tri rapide, complexité de n log n")
