import requests

# функция, которая будет обращаться к сайту 
def Zapros(parNaimSait, parKolZapros): # sssssss
  lcSaite="https://docs.python.org/3/" # сайт по умолчанию
  listZapros=list() # здесь будут храниться все результаты запросов 
  try:
    for i in range(parKolZapros):
      if parNaimSait='': # пустое значение, то использую сайт по умолчанию
        resp=requests.get(lcSaite, verify=False)
      else:
        resp=requests.get(parNaimSait, verify=False) # иначе введенный сайт
      if i % 2==0:  
        listZapros.append(resp.headers)  
      else:
        listZapros.append(resp.text)  
  except requests.exceptions.InvalidURL:
    return -1 
  # возвращаю лист 
  return listZapros 
#######################################################################

strSait=input("Введите адрес сайта, или нажмите Ввод ничего не вводя: ")
lnKol=input("Введите число повторений обращений на сайт: ")

saitResp=Zapros(strSait, 500) if not lnKol else Zapros(strSait, int(lnKol))

# просмотр результатов запроса к сайту
if saitResp != -1:
  print("Количество элементов списка = ", len(saitResp))
  print("################################# Вывод resp.headers #################################")
  # работа с циклом for для словаря
  for key in saitResp[0]: 
    # вывожу данные только из первого элемента списка, кот является множеством, для наглядности
    print(f"Ключ:{key} = {saitResp[0][key]}")
