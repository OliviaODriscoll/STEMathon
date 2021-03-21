import pandas

noviceData = pandas.read_csv("novice.csv")
expertData = pandas.read_csv("expert.csv")

if int(noviceData["Dtot"][-1:]) <= int(expertData["Dtot"][-1:]):
  print("pass")
else:
  print("fail")

  