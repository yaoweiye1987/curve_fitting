with open("spectrum3.txt","rt") as f:
  for line in f:
    x = line.split() 
    for i in x:
      if i[0] == '{':
        print i[1:]
      elif i[-1] == '}':
        print i[:-1] 
      elif i not in ['\n','\r\n','m','=']:
        print i
