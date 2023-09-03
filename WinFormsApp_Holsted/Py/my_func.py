
#///////////////////////////////////////////////////////////////////////////
#№1. Имеется текстовый файл. Сформировать новый файл, содержащий слова, сформированные из первых букв слов каждой строки исходного файла. 
#Результат работы программы поместить в отдельный текстовый файл, продублировав на экране.
def NewFileFromSymbols():
  lContinue=True
  while lContinue==True:
    print('Введите полное имя файла: ')
    nameFile=input()
    #f = open('Untitled-1.py', 'r', encoding='utf-8')
    try:
      f = open(nameFile, 'r', encoding='utf-8')
      file = f.read()
      f.close()
      aFile=file.split()
      print(aFile)
      newData=[i[0] for i in aFile]
      print(newData)
      print()
      ff=open(nameFile.split('.')[0]+'_copy.txt','w')
      for line in newData:
        ff.write(line)
      ff.close()  
    except FileNotFoundError:
      print('Данного файла или дериктории не существует!')
    # повторяем?
    print('Желаете попробовать еще? (Y-Да; N-Нет)')  
    lYN=input()
    if lYN!='Y' or lYN!='Да':
      lContinue=False    

#////////////////////////////////////////////////////////////////////////////////
#№2. Требуется вычислить входное выражение в котором есть скобки, пробельные символы и знаки умножения, 
#деления, сложения, вычитания. Пример: 1*(2+3)-(7+(5-2*2)*2). 
#Программа должна по очереди выводить действия с выражением, 
#например: 1) 2*2=4, 2) (5-4)=1, 3) 1*2=2, 4) (7+2)=9, 5) (2+3)=5, 6) 1*5=5, 7) 5-9=-4.
#////////////////////////////////////////////////////////////////////////////////
def EvalReg():
  import re
  lContinue=True
  while lContinue==True:
    print('Введите выражение: ')
    lcReg='1*(2+3)-(7+(5-2*2)*2)'#input()вапрва
    #print(lcReg)
    # повторяем?
    print('Желаете попробовать еще? (Y-Да; N-Нет)')  
    lYN=input()
    if lYN!='Y' or lYN!='Да':
      lContinue=False
#////////////////////////////////////////////////////////////////////////////////
def printer_error(s):
  alfabet='abcdefghijklm'
  S=set(s)
  V=set(alfabet)
  V_S=S-V
  kol=0
  #print(V_S)
  for i in V_S:
    kol+=s.count(str(i))
    #print(kol)
  return str(kol)+'/'+str(len(s))
#////////////////////////////////////////////////////////////////////////////////
def unlucky_days(year):
  import datetime
  sum=0 
  for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
    if  datetime.date(year, i, 13).isoweekday() == 5:
      sum+=1
  return sum
#////////////////////////////////////////////////////////////////////////////////  
def gps(s, x):
  if len(x)<=1:
    return 0  
  else:
    i=0
    myList=[]
    while i<len(x)-1:
      myList.append((3600*(x[i+1]-x[i]))/s)
      i+=1  
    print(max(myList))  
    print(int(max(myList)//1))  
    return myList
#////////////////////////////////////////////////////////////////////////////////  
def nb_dig(n, d):
  i=0
  kol=0
  while i<=n:
    i2=i**2
    print('Квадрат числа:', i2)
    kol+=len([k for k in str(i2) if int(k)==d])
    print('Кол-во:', kol)
    i+=1
  return kol
#////////////////////////////////////////////////////////////////////////////////  
#Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали, 
# выходящей из левого верхнего угла и закрученной по часовой стрелке
def matrix_spiral(n):
  matrix=[[0 for j in range(n)] for i in range(n)]
  spChisla=[i for i in range(1, n**2+1)]
  #print(matrix)
  #print(spChisla)
  lnKolChiselInLine=n-1 # кол-во чисел в линии спирали
  lnNomLine=1 # номер линии витка спирали, например 0-это самая внешняя линия
  lnNomVitka=0
  lnCh=0
  while lnCh<=n**2: # проход по списку чисел; lnCh - число, которое записано в спираль
    if lnCh==n**2:
      break
    spSrezChisel=spChisla[lnCh:lnCh+lnKolChiselInLine] # получаю срез чисел из списка
    #print(spSrezChisel)
    # смотрю какой номер линии и, в зависимости от этого, записываю в список matrix 
    if lnNomLine==1:
      k=lnNomVitka
      for i in spSrezChisel:
        matrix[lnNomVitka][k]=i
        k+=1
      lnNomLine+=1  
    elif lnNomLine==2:
      k=lnNomVitka
      for i in spSrezChisel:
        matrix[k][lnKolChiselInLine+lnNomVitka]=i
        k+=1
      lnNomLine+=1  
    elif lnNomLine==3:
      k=n-1-lnNomVitka #lnKolChiselInLine
      for i in spSrezChisel:
        matrix[lnKolChiselInLine+lnNomVitka][k]=i
        k-=1
      lnNomLine+=1  
    elif lnNomLine==4:
      k=n-1-lnNomVitka #lnKolChiselInLine
      for i in spSrezChisel:
        matrix[k][lnNomVitka]=i
        k-=1
      # на последнем витке переменные обновляю
      lnNomVitka+=1
      lnKolChiselInLine=lnKolChiselInLine-2 # уменьшаю кол-во чисел в линии спирали на 2 на след витке
      lnNomLine=1    
      # вывод матрицы, закрученной по спирали  
      #for i in range(0,5):
      #  print(matrix[i:i+1])  
    # проверяю на четность, ибо если четное число n, то оно закрывается данными по спирали, а 
    # если нечетное, то последнее число будет посередине в таблице  
    if n%2!=0 and lnCh+1==n**2:  
      k=int((n-1)/2)
      #print(lnCh)
      #print(k)
      #print(matrix[k][k])
      matrix[k][k]=lnCh+1
      break
    else:  
      lnCh=max(spSrezChisel)  
  # вывод матрицы, закрученной по спирали  
  s=''
  for i in range(0,n):
    for k in matrix[i:i+1][0]:
      s+=str(k)+' '
    print(s) 
    s=''
#////////////////////////////////////////////////////////////////////////////////  
#Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j 
# равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). 
# У крайних символов соседний элемент находится с противоположной стороны матрицы.
#В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
def matrix_new():
  matrix=[]
  matrixNew=[]
  while True:
    lcStr=input()
    if lcStr=="end":
      break  
    matrix=matrix+[[int(s) for s in lcStr.split()]]
    # новая матрица для измененных чисел
    matrixNew=matrixNew+[[int(s) for s in lcStr.split()]]
  print(matrix)  
  lnLenEl=len(matrix)   
  print("Кол-во эл-в матрицы:", lnLenEl)
  for i in range(0,lnLenEl): 
    lnLen=len(matrix[i])
    print("i=",i)
    for j in range(0,lnLen):
      lnSum=0
      print("Число =", matrix[i][j])
      # смотрю по строке влево-вправо
      if j-1<0:
        lnSum+=matrix[i][j-1+lnLen]
      else:
        lnSum+=matrix[i][j-1]
      print(lnSum)  
      ###
      if j+1>=lnLen:
        lnSum+=matrix[i][j+1-lnLen]
      else:
        lnSum+=matrix[i][j+1]  
      print(lnSum)  
      # смотрю по столбцу вверх-вниз9
      if i-1<0:
        print("i, j=", i, j)
        if lnLen/len(matrix[i-1+lnLenEl])>1: # текущая строка больше следующей
          lnSum+=matrix[i-2+lnLenEl][j]
        else:
          lnSum+=matrix[i-1+lnLenEl][j]
      else:
        lnSum+=matrix[i-1][j]  
      print(lnSum)  
      ###
      if i+1>=lnLenEl:
        if lnLen/len(matrix[i+1-lnLenEl])>1: # текущая строка больше предыдущей
          lnSum+=matrix[i+2-lnLenEl][j]
        else:  
          lnSum+=matrix[i+1-lnLenEl][j]
      else:
        if lnLen/len(matrix[i+1])>1 and j==len(matrix[i+1]): 
          lnSum+=matrix[i][j]
        else:
          lnSum+=matrix[i+1][j]
      print(lnSum)  
      # заношу в матрицу новое значение  
      matrixNew[i][j]=lnSum
  # вывод на экран    
  s=''
  for i in range(0,len(matrixNew)):
    for j in matrixNew[i]:
      s+=str(j)+' '
    print(s) 
    s=''
  #print(matrixNew)  
#////////////////////////////////////////////////////////////////////////////////  
#123 ->  321
#-456 -> -654
#1000 ->    1
def reverse_number(n):
  listN=[n for n in str(n) if n!="-"]
  listN.reverse()
  s=""
  for el in listN:
    s+=el
  if n<0: s="-"+s  
  return int(s)
#//////////////////////////////////////////////////////////////////////////////// 
def modify_list(l):
  print(l)
  i=0
  while i<len(l):
    if l[i]%2>0:
      l.pop(i)
      i-=1
    i+=1  
  print(l)    
  for i in range(len(l)):
    l[i]=l[i]//2
  print(l)     
#//////////////////////////////////////////////////////////////////////////////// 
def solve(s):
  listGlas=list('aeiuo')
  listAlphabet=list("abcdefghijklmnopqrstuvwxyz")
  listNomer=[n+1 for n in range(len(listAlphabet))]
  dictDD = dict(zip(listAlphabet, listNomer))
  lnMax=0
  lnTek=0
  for i in s:
    if listGlas.count(i)>0:
      if lnTek>=lnMax:
        lnMax=lnTek
      lnTek=0
    else:
      if listAlphabet.count(i)>0:
        lnTek+=dictDD[i]  
  return lnMax
#//////////////////////////////////////////////////////////////////////////////// 
def comp(array1, array2):
  if array1==None or array2==None:
    return False
  else:
    arr3=[]
    for arr2 in array2:
      for arr1 in array1:
        if arr1**2==arr2:
          arr3.append(True)
          break
      else:
        arr3.append(False)    
    print(arr3)           
    if False in arr3:
      return False
    return True
#//////////////////////////////////////////////////////////////////////////////// 
def comp_1(array1, array2):
  if array1==None or array2==None:
    return False
  else:
    arr3=[]
    for arr2 in array2:
      print(len(array1))
      for arr1 in range(len(array1)):
        if array1[arr1]**2==arr2:
          arr3.append(True)
          array1.pop(arr1)
          arr1-=1
          break
      else:
        arr3.append(False)    
    print(arr3)           
    if False in arr3:
      return False
    return True    
#/////Kata Simple Simple Simple String Expansion ///////////////////////////////////////////////////////////////////////////     
#test.assert_equals(string_expansion('3abc'),'aaabbbccc')
#test.assert_equals(string_expansion('3D2a5d2f'),'DDDaadddddff')
#test.assert_equals(string_expansion('0d0a0v0t0y'),'')
#test.assert_equals(string_expansion('3d332f2a'),'dddffaa')
#test.assert_equals(string_expansion('abcde'),'abcde')
def string_expansion(s):    
  listChisla=list('1234567890')
  dictCh = {i: int(s[i]) for i in range(len(s)) if s[i] in list('1234567890')}
  if dictCh=={}:
    return s
  else:  
    listDelKey=[]
    listKeys=list(dictCh.keys())
    # определяю ключи к удалению, если несколько цифр подряд идет
    for i in range(len(listKeys)-1,0,-1):
      if listKeys[i]!=0:
        if listKeys[i]-listKeys[i-1]==1:
          listDelKey.append(listKeys[i-1])
    #print(listDelKey)      
    # удаляю лишние ключи
    if len(listDelKey)>0:
      for i in listDelKey:
        dictCh.pop(i)
    print(dictCh)  
    #формирую строку
    listKeys=list(dictCh.keys())
    strNew=""
    if listKeys[0]!=0:
      for sss in s:
        if sss.isdigit()==False:
          strNew+=sss
        else:
          break  
    for key in range(len(listKeys)):
      print(listKeys[key], dictCh[listKeys[key]])
      if key==len(listKeys)-1:
        sl=s[listKeys[key]+1:]
      else:
        sl=s[listKeys[key]+1:listKeys[key+1]]  
      print("подстрока:",sl)
      for sss in sl:
        if sss.isdigit()==False:
          strNew+=(dictCh[listKeys[key]]*sss)
        print(strNew)
    return strNew    
#//////////////////////////////////////////////////////////////////////////////// 
def update_dictionary(d, key, value):
  sp=[]
  sp.append(value)
  if key in d:
    d.get(key).append(value)
  elif 2*key in d:
    d.get(2*key).append(value)
  elif d.get(2*key)==None:
    d[2*key]=sp
#//////////////////////////////////////////////////////////////////////////////// 
def bouncingBall(h, bounce, window):
  if h<=0 or (bounce>=1 or bounce<=0) or window>=h:
    return -1
  else:
    lnKol=0 # один раз видит точно, когда вниз летит
    while h>=window:
      lnKol+=1
      h=h*bounce
      if h>=window:
        lnKol+=1
    return lnKol
#//////////////////////////////////////////////////////////////////////////////// 
def StrokaRestore():
  # i5d18W8K15e6L2V1L19l7H5B16s1Y15q7Y4u20o10K19Z15G15n9o14u16m16p6n14i11w13P15v15E11z7S5Q14m13k4g5m15t7P13p16
  for line in open("d:\\1\\dataset_3363_2.txt"):
    strNew=""
    i=0
    k=1
    while k<len(line):
      if line[k].isalpha() or k+1==len(line):
        strNew+=(line[i]*int(line[i+1:k]))
        i=k
        print(strNew)
      k+=1  
    print("Длина строки={} : i={} : k={}:".format(len(line), i, k))  
    #strNew+=(line[i]*int(line[i+1:k]))  
    F = open("d:\\1\\dataset_3363_output.txt", "w") # Создает файл для записи  
    F.write(strNew)
    F.close
#//////////////////////////////////////////////////////////////////////////////// 
def ChastorSlovo():
  #Sample Input: abc a bCd bC AbC BC BCD bcd ABC  #Sample Output: abc 3
  lnKol=0
  strS=""
  input = open(r"d:\1\dataset_3363_2.txt")
  aList = input.readlines()
  for line in aList:
    strS+=line[0:len(line)-1].lower()+" "
  sp=list(strS.split(" "))  
  strS=""
  for elSp in sp:
    if sp.count(elSp)>lnKol:
      lnKol=sp.count(elSp)
      strS=elSp
  F = open("d:\\1\\dataset_3363_output.txt", "w") # Создает файл для записи  
  F.write(strS+" "+str(lnKol))
  F.close    
  print(aList)
  print(sp)      
  print("Строка:кол-во={}:{}".format(strS,lnKol))
#//////////////////////////////////////////////////////////////////////////////// 
def OcenkiUch():
  listSR=[]
  lnKol=0
  strNew=""
  lnSumMat=lnSumFiz=lnSumRus=0
  F = open("d:\\1\\dataset_3363_output.txt", "w") # Создает файл для записи  
  for line in open("d:\\1\\dataset_3363_2.txt", encoding='utf-8'):
    listLLL=list(line[0:len(line)-1].split(";"))
    lnSumMat+=int(listLLL[1])
    lnSumFiz+=int(listLLL[2])
    lnSumRus+=int(listLLL[3])
    F.write(str((int(listLLL[1])+int(listLLL[2])+int(listLLL[3]))/3)+"\n")
    lnKol+=1 # кол-во учеников
  F.write(str(lnSumMat/lnKol)+" "+str(lnSumFiz/lnKol)+" "+str(lnSumRus/lnKol))  
  print(listLLL)
  F.close
#////////////////////////////////////////////////////////////////////////////////   
def next_version(version):
    if int(version[-1])<9:
        return version[:-1]+str(int(version[-1])+1)  
    else:
        strNew=""
        n=1
        listSp=[int(s) for s in version.split(".")]
        print(listSp)
        for ss in range(len(listSp)-1,-1,-1):
            if n==1:
                if ss>0:
                    lnss=listSp[ss]
                    listSp[ss]=(listSp[ss]+n)%10
                    n=int((lnss+n)/10)
                else:
                    listSp[ss]=(listSp[ss]+n)%10 if listSp[ss]<9 else listSp[ss]+1
            else:
              break        
        print(listSp)        
        for ss in listSp:
            strNew+=str(ss)+"."
        return strNew[:-1]    
#////////////////////////////////////////////////////////////////////////////////   
def My_requests(lcAdres):
  import urllib.request
  listAd=[s for s in lcAdres.split("/")]
  lcAdresPP=lcAdres[:lcAdres.find(listAd[-1])]
  while True:
    response = urllib.request.urlopen(lcAdres)
    res=response.readlines()
    sss=res[0].decode('utf-8')
    print(sss)
    if sss[:2].upper() =='WE':
      for i in res:
        print(i.decode('utf-8'))
      break
    else:  
     lcAdres=lcAdresPP+sss
     print(lcAdres)
#////////////////////////////////////////////////////////////////////////////////
def FootballStat():
  spisResult=['3',
              'Зенит;3;Спартак;1',
              'Спартак;1;ЦСКА;1',
              'ЦСКА;0;Зенит;2'
             ]
  dictResult={}
  for i in range(1,len(spisResult)):
    # получаю в виде списка i-ю строку
    spisGame=[m for m in spisResult[i].split(";")]
    #print(spisGame)
    listDict_1=dictResult.setdefault(spisGame[0], [0,0,0,0,0])
    listDict_2=dictResult.setdefault(spisGame[2], [0,0,0,0,0])
    #print('Ключ=', listDict_1, '| Ключ=', listDict_2)
    if int(spisGame[1])>int(spisGame[3]):
      listDict_1[0]+=1; listDict_2[0]+=1
      listDict_1[1]+=1; listDict_2[3]+=1
      listDict_1[4]+=3; listDict_2[4]+=0
    elif int(spisGame[1])==int(spisGame[3]): 
      listDict_1[0]+=1; listDict_2[0]+=1
      listDict_1[2]+=1; listDict_2[2]+=1
      listDict_1[4]+=1; listDict_2[4]+=1
    else:
      listDict_1[0]+=1; listDict_2[0]+=1
      listDict_1[3]+=1; listDict_2[1]+=1
      listDict_1[4]+=0; listDict_2[4]+=3
    #print(dictResult[spisGame[0]])
  #print(spisResult)
  # вывод результатов
  strNew=""
  for lnKey in dictResult.keys():
    #print(lnKey, " => ", dictResult[lnKey])
    strNew+=lnKey+":"
    for lnValue in dictResult[lnKey]:
      strNew+=str(lnValue)+" "
    print(strNew)
    strNew=""
#////////////////////////////////////////////////////////////////////////////////
def Orfograf():    
  print("Введите кол-во записей в списке")
  d=input()
  listWord=[]
  for i in range(int(d)):
    listWord.append(input().upper())
  print("Введите кол-во строк текста")  
  l=input()
  listText=[]
  for i in range(int(l)):
    listText.append(input())
  # поиск слов не встречающихся в словаре
  listSl=[] # слова, которые уже были
  for i in range(len(listText)): 
    listStroka=[sss for sss in listText[i].split(" ")]
    for k in listStroka:
      if listWord.count(k.upper())==0 and listSl.count(k.upper())==0:
        print(k)
        listSl.append(k.upper()) 
#////////////////////////////////////////////////////////////////////////////////        
def Cherepaha():    
  print("Введите кол-во записей")
  d=input()
  listKoord=[0,0]
  for i in range(int(d)):
    listWord=[sss for sss in input().lower().split(" ")]
    if listWord[0]=="восток":
      listKoord[0]+=int(listWord[1])
    elif listWord[0]=="север":
      listKoord[1]+=int(listWord[1])  
    elif listWord[0]=="запад":
      listKoord[0]+=-1*int(listWord[1])
    elif listWord[0]=="юг":
      listKoord[1]+=-1*int(listWord[1])    
  print(listKoord[0],listKoord[1])    
#//////////////////////////////////////////////////////////////////////////////// 
def KlassStat():
  input = open(r"c:\Users\a.denisov\Downloads\dataset_3380_5.txt")
  aList = [line.strip().split('\t') for line in input]
  print(aList)
  print(aList[0][0])
  dictResult={}
  for i in range(len(aList)):
    listDict=dictResult.setdefault(int(aList[i][0]),[0,0])
    #print(listDict)
    listDict[0]+=int(aList[i][2]) 
    listDict[1]+=1
  print(dictResult)
  for i in range(1,12):
    if dictResult.get(i, '-')=='-':
      print(i,'-') 
    else:
      print(i,round(dictResult[i][0]/dictResult[i][1],5))  
#////////////////////////////////////////////////////////////////////////////////        
def ShifrInformatiks():
  listVvod=[]
  for i in range(4):
    listVvod.append(input())
  print(listVvod)
  # шифрую первое слово
  strStr=""
  print("Кодировка:")
  for i in range(len(listVvod[2])):
    strStr+=listVvod[1][listVvod[0].index(listVvod[2][i])]
    print(strStr)
  print("Расшифровка:")
  strStr=""
  for i in range(len(listVvod[3])):
    strStr+=listVvod[0][listVvod[1].index(listVvod[3][i])]
    print(strStr)
#////////////////////////////////////////////////////////////////////////////////  
def ProdTree(l, r):
  if l > r:
    return 1
  if l == r:
    return l
  if r - l == 1:
    return l * r
  m = (l + r) // 2
  return ProdTree(l, m) * ProdTree(m + 1, r)
#///
def FactTree(n):
  if n < 0:
    return 0
  if n == 0:
    return 1
  if n == 1 or n == 2:
    return n
  return ProdTree(2, n)
#///
def DiagonalPaskal(n, p):
  # n-номер строки; р-номер диагонали
  if n >= p >= 0:
    lnSum=0
    dictFactorial={} # словарь значений вычисленных факториалов
    # нахожу факториалы до последнего числа и записываю в словарь
    lnFact=1
    for i in range(1, n+1):
      lnFact*=i
      dictFactorial[i]=lnFact
      #dictFactorial[i]=FactTree(i)
    dictFactorial[0]=1
    print("последнее число=",lnSum)
    # нахожу самое последнее число в диагонали используя формулу n!/(p!*(n-p)!)
    for i in range(n,1,-1):
      if i>p:
        lnSum+=dictFactorial[i]//(dictFactorial[p]*dictFactorial[(i-p)]) 
        print("i=", i, "fact=",dictFactorial[i]/(dictFactorial[p]*dictFactorial[(i-p)]), "Sum=",lnSum)
    lnSum+=1  # последний факториал 1!=1
    print("сумма =",lnSum)  
#///
def DiagonalPaskal_1(n, p):
  # n-номер строки; р-номер диагонали
  lnSum=0
  if n >= p >= 0:
    lnSum=FactTree(n+1)//(FactTree(p+1)*FactTree((n+1)-(p+1))) 
  print("сумма =",lnSum)
#////////////////////////////////////////////////////////////////////////////////    
'''ls = [0, 1, 3, 6, 10]
Its following parts:
ls = [0, 1, 3, 6, 10]
ls = [1, 3, 6, 10]
ls = [3, 6, 10]
ls = [6, 10]
ls = [10]
ls = []'''
def parts_sums(ls):
  listSum=[]
  print("listSum=", listSum)
  lnSum=sum(ls)
  listSum.append(lnSum)
  lnRazn=0
  for i in range(0, len(ls)):
    lnRazn+=ls[i]
    listSum.append(lnSum-lnRazn)
    #listSum.append(sum(ls))
    #ls=ls[1:] 
    print("listSum=", listSum) 
  #listSum.append(0)  
  print("listSum=", listSum) 
#////////////////////////////////////////////////////////////////////////////////      
def duplicate_count(text):  
  text=text.upper()
  setText=set(text)
  print("setText=",setText)
  kol=0
  #print(V_S)
  for i in setText:
    if text.count(str(i))>1:
      kol+=1
  print(kol)
  #return kol
#////////////////////////////////////////////////////////////////////////////////      
def alphabet_position(text):
  text=text.lower()
  alphabet='abcdefghijklmnopqrstuvwxyz'
  textNew=""
  for i in text:
    if alphabet.find(i)!=-1:
      textNew+=str(alphabet.find(i)+1)+" "
  print(textNew)
#////////////////////////////////////////////////////////////////////////////////        
def validPhoneNumber(phoneNumber):
  if len(phoneNumber)==14 and phoneNumber[0]=='(' and phoneNumber[4]==')' and phoneNumber[5]==' ' and phoneNumber[9]=='-':
    print(True)
  else:
    print(False)  
#////////////////////////////////////////////////////////////////////////////////            
def data_reverse(data):  
  listRev=[data[i:i+8] for i in range(0,len(data),8)]
  print(listRev)
  listRev.reverse()
  print(listRev)
  listReverse=[listRev[i][k] for i in range(0,len(listRev)) for k in range(0,len(listRev[i]))]
  print(listReverse)
#////////////////////////////////////////////////////////////////////////////////              
def solution(s):  
  listRev=[s[i:i+2] for i in range(0,len(s),2)]
  print(listRev)
  if len(s)%2!=0:
    listRev[len(listRev)-1]=listRev[len(listRev)-1]+"_"
    print(listRev)
#////////////////////////////////////////////////////////////////////////////////                  
def sum_consecutives(s):    
  listSum=[]
  i=0
  lnEnd=0
  while i<len(s):
  #for i in range(0,len(s)):
    p=s[i]
    print('i=', i, 'p=',p)
    for k in range(i+1,len(s)):
      if s[i]!=s[k]:
        listSum.append(p)
        i=k-1
        break
      else:
        p+=s[k]
        print('  i=', i, 'k=', k, 'p=',p)
      if k==len(s)-1:
        lnEnd=1    
    else:
      listSum.append(p)    
    if lnEnd==1:
      break 
    i+=1  
  print(listSum)
#////////////////////////////////////////////////////////////////////////////////  
def alphabetized(s):    
  print('s=', s)
  alphabet='abcdefghijklmnopqrstuvwxyz'
  lcSortStr=""
  lnPos=0
  #listS=[i for i in s if alphabet.count(i.lower())>0]
  for i in s:
    if alphabet.count(i.lower())>0:
      lcSortStr+=i
  s=lcSortStr    
  lcSortStr=""    
  print(lcSortStr)
  for lcSymb in alphabet:
    #print("lcSymb=",lcSymb)
    while lnPos!=-1:
      lnPos=s.lower().find(lcSymb)
      print(lnPos)
      if lnPos!=-1: # т.е. найден символ
        lcSortStr+=s[lnPos]
        if lnPos>0:
          s=s[:lnPos]+s[lnPos+1:]
        else:
          s=s[lnPos+1:]
      else:
        lnPos=0
        break
      print(lcSortStr)  
      print(s)
  print(lcSortStr)
#////////////////////////////////////////////////////////////////////////////////  
def pascal(p):
  listP=[]
  for k in range(p):
    listSp=[1]
    if k==0:
      listP.append([1]) 
    elif k==1: 
      listP.append([1,1])
    else:
      for p in range(1,k):
        listSp.append(listP[k-1][p-1]+listP[k-1][p])
      listSp.append(1)  
      listP.append(listSp)
  print(listP)  
#////////////////////////////////////////////////////////////////////////////////
def narcissistic(value):  
  listP=[int(k)**len(str(value)) for k in str(value)]
  print(listP)
  print("sum=",sum(listP))
#////////////////////////////////////////////////////////////////////////////////  
# https://www.codewars.com/kata/reducing-a-pyramid/train/python
def reduce_pyramid(base):
  if len(base)==1 or len(base)==2:
    print(sum(base))
  else:  
    while len(base)>2:
      base=[base[p]+base[p+1] for p in range(0,len(base)-1)]
      print("listP=", base)  
    else:
      print("sum=", sum(base)) 
#////////////////////////////////////////////////////////////////////////////////        
def matrix_addition():
  a=[ [1, 2, 3],
    [3, 2, 1],
    [1, 1, 1] ]
  b=[ [2, 2, 1],
    [3, 2, 3],
    [1, 1, 3] ]  
  #listP=[[a[i][k]+b[i][k]] for i in range(len(a)) for k in range(len(a[i]))]
  listC=[]
  for i in range(len(a)):
    listP=[]
    for k in range(len(a[i])):
      listP.append(a[i][k]+b[i][k])
    print(listP)  
    listC.append(listP)
  print(listC) 
#////////////////////////////////////////////////////////////////////////////////          
def unique_in_order(iterable):     
  listP=[]
  I = iter(iterable) # Ручной способ итераций: имитация цикла for
  i=0
  while True:
    try: # Инструкция try обрабатывает исключения
      X = next(I) # Или I.__next__
      if len(listP)==0 or listP[i-1]!=X:
        listP.append(X)
        i+=1
      #elif listP[i-1]!=X:
      #  listP.append(X)
      #  i+=1
      print(listP)  
      
    except StopIteration:
      break
    print(X)
  print(listP)  

  '''listP=list(iterable[0])
  for i in iterable:
    if i!=listP[len(listP)-1]:
      listP.append(i)
  print(listP)    '''
#////////////////////////////////////////////////////////////////////////////////
def is_balanced(source, caps):
  listP=[s for s in source if caps.count(s)>0 ]
  print(listP)
  lnLenList=len(listP)
  if lnLenList % 2 != 0:
    print(False)
    return False
  else:
    dictCaps={caps[x]: caps[x+1] for x in range(0,len(caps),2)}
    print(dictCaps)
    for x in range(0,len(listP),2):
      if caps.find(listP[x]+listP[x+1]) == -1:
        break
    else:
      print(True)
      return True    
    for i in range(int(lnLenList/2)):
      if list(dictCaps.keys()).count(listP[i])>0 and dictCaps[listP[i]]!=listP[lnLenList-1-i]:
        break
    else: 
      print(True)
      return True
    print(False)  
    return False
#////////////////////////////////////////////////////////////////////////////////
"""
tree = [" o o o  ",
        " \\    \\ ",
        "   \\    ",
        "  \\  \\  ",
        "   ||   ",
        "   ||   ",
        "   ||   "]
expected = [0,0,0,1,1,0,1,0]        
"""
def shake_tree():
  # дерево
  tree = [" o o o  ",
        " /    / ",
        "   /    ",
        "  /  /  ",
        "   ||   ",
        "   ||   ",
        "   ||   "]
  expected = [1,1,0,0,1,0,0,0]      
  # высчитываю упавшие орехи по позициям
  listRes=[0 for i in range(len(tree[0]))]
  print(listRes)
  dictO={x: tree[0][x] for x in range(len(tree[0])) if tree[0][x]=='o'}
  print(dictO)
  for i_o in dictO.keys():
    posIO=i_o # позиция текущего ореха
    for k in range(1, len(tree)): # начинаю со 2-й строки
      if tree[k][posIO]=="\\": 
        posIO+=1 # отскок вправо
      elif tree[k][posIO]=="/": 
        posIO-=1 # отскок влево
      elif tree[k][posIO]=="_":
        break # застрял на ветке орех, значит его не учитываю
    else: # обрабатываю дохождение до земли
      listRes[posIO]+=1
    # вывод промежуточного результата  
    print(listRes)  
#////////////////////////////////////////////////////////////////////////////////
"""
tree = [" o      ",
        " / o o/ ",
        " ///    ",
        "   ///  ",
        "   ||   ",
        "   ||   ",
        "   ||   "]
expected = [2,0,1,0,0,0,0,0]        
"""
def shake_tree_1():
  # дерево
  tree = [' o        ', 
          ' \\\\\\\\\\\\\\  ', 
          '  /////// ', 
          ' \\\\\\\\\\\\/  ', 
          '    ||    ', 
          '    ||    ', 
          '    ||    ']
  # should equal [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  # высчитываю упавшие орехи по позициям
  listRes=[0 for i in range(len(tree[0]))]
  print(listRes)
  # строки, где есть 'o' в list
  list_withO=[x for x in range(len(tree)) if tree[x].count('o')>0]
  print("номера веток с орехами: ", list_withO)
  for w in list_withO: # проход по всем уровням дерева
    # список с определением на каких позициях орехи на данном уровне дерева
    listO=[x for x in range(len(tree[w])) if tree[w][x]=='o']
    print("позиции орехов на ветви {w}: ", listO)
    for i_o in listO:
      posIO=i_o # позиция текущего ореха
      for k in range(w+1, len(tree)): # начинаю со 2-й строки
        # гоняю отскоки, или определяю застрявание
        print([x for x in tree[k]])
        while tree[k][posIO]=="\\" or tree[k][posIO]=="/" or tree[k][posIO]=="_":
          print("позиция posIO=", posIO)
          if tree[k][posIO]=="\\": 
            if tree[k][posIO+1]=="/":
              posIO=-1
              break # отскок вправо влево, или влево вправо, т.е. орех застрял на дереве
            posIO+=1 # отскок вправо
          elif tree[k][posIO]=="/": 
            if tree[k][posIO-1]=="\\":
              posIO=-1
              break # отскок вправо влево, или влево вправо, т.е. орех застрял на дереве
            posIO-=1 # отскок влево
          elif tree[k][posIO]=="_":
            break # застрял на ветке орех, значит его не учитываю
        if posIO==-1:
          break
      else: # обрабатываю дохождение до земли
        listRes[posIO]+=1
    # вывод промежуточного результата  
    print("кол-во орехов на земле по позициям: ",listRes)     
#////////////////////////////////////////////////////////////////////////////////    
def make_password(length, flagUpper, flagLower, flagDigit):
  import random
  sAlphabetAll=list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
  strS=""; s=""
  while len(strS)<length:
    for x in range(len(strS),length):
      if flagUpper==False and flagLower==False and flagDigit==True:
        s=str(random.choice(list(set(sAlphabetAll[52:]).difference(set(list(strS))))))
      else:
        s=str(random.choice(list(set(sAlphabetAll).difference(set(list(strS))))))
      if flagDigit==False:
        if s.isdigit():
          s=str(random.choice(list(set(sAlphabetAll[:52]).difference(set(list(strS))))))
      strS+=s
    if flagUpper==False and flagLower==True:
      strS=strS.lower()
    elif flagLower==False and flagUpper==True:
      strS=strS.upper()
    strS=''.join(set(strS))
  print(strS)   
  if any(map(str.isdigit, strS))==False and flagDigit==True: # не содержит цифр в строке 
    strS=strS[: length-1]+str(random.choice(sAlphabetAll[52:]))
  if any(map(str.islower, strS))==False and flagLower==True: # не содержит букв в нижнем регистре
    strS=str(random.choice(sAlphabetAll[:27]))+strS[1:length+1]
  if any(map(str.isupper, strS))==False and flagUpper==True: # не содержит букв в верхнем регистре
    strS=str(random.choice(sAlphabetAll[27:52]))+strS[1:length+1]
  print(strS, set(strS))
#////////////////////////////////////////////////////////////////////////////////
def alphanumeric(password):
  sAlphabetAll=set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
  return print(False) if len(set(password).difference(sAlphabetAll))>0 or password=="" else print(True)
#////////////////////////////////////////////////////////////////////////////////
def deliteli(n):
  factoriz=[] #числа после факторизации числа n
  nn=n
  while True:
    for i in range(2,nn+1):
      if nn % i==0:
        factoriz.append(i)
        nn=int(nn / i)
        break
    if nn==1:
      break
  print("Факторизация: ", factoriz)  
  return factoriz

def sol_equa(n):
  import math
  # все делители числа
  listResult=[]
  listMnoj=[int(n/i) for i in range(1,int(math.sqrt(n) + 1)) if n % i==0] # все делители числа n
  lnLen=len(listMnoj)
  for i in range(lnLen-1,-1,-1):
    listMnoj.append(int(n/listMnoj[i]))
  listMnoj.reverse()  
  ###
  print("Делители: ",listMnoj)
  print("Кол-во делителей: ",len(listMnoj))
  ind=-1 # индекс 
  lnLenList=len(listMnoj)/2
  for i in range(len(listMnoj)):
    if i < lnLenList:
      if (listMnoj[ind]-listMnoj[i]) % 4 ==0:
        y=(listMnoj[ind]-listMnoj[i])/4
        x=listMnoj[i]+2*y
        listResult.append([int(x),int(y)])
    else:
      break    
    ind-=1  
  print(listResult)

  #for i in range(1, n+1):
  #  if n % i==0:
  #    print('i=', i)

### ВЫПОЛНЕНИЕ ФУНКЦИЙ ###
sol_equa(12)
#print(printer_error('aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxxyz'))
#print('\nКол-во пятниц 13-го в :', unlucky_days(1986))
#x = [0.0, 0.01, 0.36, 0.6, 0.84, 1.05, 1.26, 1.47, 1.68, 1.89, 2.1, 2.31, 2.52, 2.73, 2.94, 3.15]
#s = 14
#print(gps(s,x))
#print(nb_dig(5750, 0))
#matrix_spiral(10)
#matrix_new()
#print(reverse_number(1000))
#modify_list([1, 2, 3, 4, 5, 6])
#print(solve("aaadd"))
#a1 = [2,2,3]
#a2 = [4,9,9]
#print(comp_1(a1, a2))
#print(string_expansion('DG30EFCfF9c064f5'))
#d = {}
##print(update_dictionary(d, 1, -1))  # None
#print(d)                            # {2: [-1]}
#update_dictionary(d, 2, -2)
#print(d)                            # {2: [-1, -2]}
#update_dictionary(d, 1, -3)
#print(d)                            # {2: [-1, -2, -3]}
#print(bouncingBall(3, 0.66, 1.5))
#StrokaRestore()4
#ChastorSlovo()
#OcenkiUch()
#print(next_version("10.9.9.9.9.9"))
#My_requests("https://stepic.org/media/attachments/course67/3.6.3/699991.txt")
#FootballStat()
#Orfograf()
#Cherepaha()
#KlassStat()
#ShifrInformatiks()
#DiagonalPaskal_1(20,5)
#parts_sums([0, 1, 3, 6, 10])
#duplicate_count("indivisibility")
#alphabet_position("The sunset sets at twelve o' clock.")
#validPhoneNumber("(123) 456-7890")
#data_reverse([0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1])
#solution("asdfads")
#sum_consecutives([1,4,4,4,0,4,3,3,1,1])
#alphabetized(" a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
#pascal(6)
#narcissistic(371)
#reduce_pyramid([8, 2, 17, 14, 14, 17, 10, 13, 7, 17, 1, 14, 10, 18, 11, 6, 15, 4, 12, 5])
#matrix_addition()
#unique_in_order('AAAABBBCCDAABBB')
#is_balanced("((()Hello()))", "()")
#shake_tree()
#shake_tree_1()
#make_password(5, True, True, True)
#alphanumeric("      ")
