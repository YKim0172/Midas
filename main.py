import math
import statistics
####work on P/E and DIVIDEND YIELD ANALYSIS
def correlationCalculator(mins, prices, finalRating, marCap, lastLetter,pricesOfSAP, minutesofSAP, VolumeOfSAP,peRatio, divYield):
  listSent = prices
  meanOfTimes = sum(mins)/len(mins)
  meanOfPrices = sum(prices)/len(prices)

  listStanDevX = []
  for value in mins:
    a = (value-meanOfTimes)**2
    listStanDevX.append(float(a))
  stanDevX = math.sqrt((sum(listStanDevX))/(len(listStanDevX)-1))
  ##print(stanDevX)
  
  listStanDevY = []
  for value in prices:
    a = (value-meanOfPrices)**2
    listStanDevY.append(float(a))
  stanDevY = math.sqrt((sum(listStanDevY))/(len(listStanDevY)-1))
  ##print(stanDevY)

  listAB = []
  for i in (0, len(mins)-1):
    a = float(mins[i]) - float(meanOfTimes)
    b = float(prices[i]) - float(meanOfPrices)
    products = a*b
    listAB.append(products)
  correlation = (sum(listAB) / (stanDevX*stanDevY)) / (len(mins))
  ##print(correlation)
  if correlation < .8:
    finalRating += 0
  else:
    finalRating += 2
  slopeRegLine = correlation*(stanDevY/stanDevX)
  ##print(slopeRegLine)
  yIntRegLine = meanOfPrices - (slopeRegLine*meanOfTimes)
  ##print(yIntRegLine)
  if slopeRegLine < 0:
    ##print("The least-squares regression line: "+ str(yIntRegLine) + " - " + str(-1*slopeRegLine) + "x")
    interpreter(slopeRegLine, mins, prices, correlation, finalRating, marCap, lastLetter, listSent,pricesOfSAP, minutesofSAP, VolumeOfSAP, peRatio, divYield)
  else:
    interpreter(slopeRegLine, mins, prices, correlation, finalRating, marCap, lastLetter, listSent,pricesOfSAP, minutesofSAP, VolumeOfSAP, peRatio, divYield)
  #volatilityCalculator(listSent)

def interpreter(val,mins,prices,cor,finalRating, marCap, lastLetter, sentList,pricesOfSAP, minutesofSAP, VolumeOfSAP, peRatio, divYield):
  listSent = sentList
  xOne = int(mins[0])
  xTwo = int(mins[-1])
  yOne = int(prices[0])
  yTwo = int(prices[-1])
  roughSlope = (yTwo - yOne) / (xTwo - xOne)
  ##print(roughSlope)
  if (abs(roughSlope)) > (abs(val*1.25)):
    print("-There is a lot of buying happening. Overbuying is current occuring. Please refrain from buying.")
  else:
    print("-No overbuying or overselling.")
    finalRating += 2
  volatilityCalculator(listSent, finalRating, marCap, peRatio, divYield, lastLetter,pricesOfSAP, minutesofSAP, VolumeOfSAP)

def volatilityCalculator(listOfPrices,finalRating, marCap, peRatio, divYield, lastLetter,pricesOfSAP, minutesofSAP, VolumeOfSAP):
  standardDeviation = statistics.stdev(listOfPrices)
  #print(standardDeviation)
  if abs(standardDeviation > 0) and (standardDeviation < 5):
    print("-There is not that much volatility")
    finalRating += 2
  elif abs(standardDeviation > 5) and (standardDeviation < 10):
    print("-There is quite a lot of volatility")
    finalRating += 0
  else:
    print("-There is too much volatility. Not safe for buying") 
    finalRating -= 1
  stockInfoInterpreter(marCap, lastLetter, finalRating , peRatio, divYield, pricesOfSAP, minutesofSAP, VolumeOfSAP)

#do mean of price standard dev as well
def stockInfoInterpreter(marCap, lastLetter, finalRating, peRatio, divYield ,pricesOfSAP, minutesofSAP, VolumeOfSAP):
  final = finalRating
  flag = 0
  while flag < 1:
    print("")
    flag += 1
  print("-------------------------------------------")
  print("Summaries \n")
  numMarketCap = float(marCap[0: len(marCap) - 2])
  if lastLetter == "M":
    if numMarketCap < (300):
      print("-You should probably not invest in this company. It isn't heavily traded in the markets as of right now.")
    elif numMarketCap >= (300):
      print("-This company has a small market cap. It's not a big company.")
  elif lastLetter == "B":
    if numMarketCap < (2):
      print("-This company has a small market cap. It's not a big company.")
    elif numMarketCap >= (2) and numMarketCap < (10):
      print("-This company is a mid-cap company. Size of company is medium.")
      final += 1
    elif numMarketCap >= (10):
      print("-This company is a large-cap company. The company is pretty big.")
      final += 2
  elif lastLetter == "T":
    print("-The company is huge. A blue chip stock is great for investing, in general.")
    final += 2
  else:
    print("-The market-cap is too small-You should focus on big companies that are trustworthy.")
    final -= 2
  peAndDivInterpreter(peRatio, divYield, final, pricesOfSAP, minutesofSAP, VolumeOfSAP)


#PE ratio/dividend yield calculations
def peAndDivInterpreter(peRatio, divYield, finalRating, pricesOfSAP, minutesofSAP, VolumeOfSAP):
  peRatio = float(peRatio)
  divYield = float(divYield)
  if peRatio < 10:
    print("-The stock might currently be undervalued. There is potential currently to buy a stock for a cheaper price.")
  elif peRatio >= 10:
    print("-The stock might currently be overvalued. A price pullback might occur, so it's best to wait.")
    finalRating += 3
  if divYield <= 2:
    print("-The dividend yield seems to be low. That means you won't be getting as much profit by being a part owner in that company.")
  elif divYield >2:
    print("-There's a high dividend yield. More profit for you.")
    finalRating += 3
  sandpCalculator(pricesOfSAP, minutesofSAP, VolumeOfSAP, finalRating)
#------------------------------------------------------------------------------------
#SANDP Price management
def sandpCalculator(pricesOfSAP, minutesOfSAP, VolumeOfSAP,finalRating):
  standardDeviation = statistics.stdev(pricesOfSAP)
  #print(standardDeviation)
  if abs(standardDeviation > 0) and (standardDeviation < 5):
    print("-There is not that much volatility in the overall market")
    finalRating += 2
  elif abs(standardDeviation > 5) and (standardDeviation < 10):
    print("-There is quite a lot of volatility in the overall market")
    finalRating += 3
  else:
    print("-There is too much volatility in the overall market.")
  #regLine of SANDP Volume
  minListSent = minutesOfSAP
  volListSent = VolumeOfSAP
  meanOfTimes = sum(minutesOfSAP)/len(minutesOfSAP)
  meanOfVolumes = sum(VolumeOfSAP)/len(VolumeOfSAP)

  listStanDevX = []
  for value in minutesOfSAP:
    a = (value-meanOfTimes)**2
    listStanDevX.append(float(a))
  stanDevX = math.sqrt((sum(listStanDevX))/(len(listStanDevX)-1))
  ##print(stanDevX)
  
  listStanDevY = []
  for value in VolumeOfSAP:
    a = (value-meanOfVolumes)**2
    listStanDevY.append(float(a))
  stanDevY = math.sqrt((sum(listStanDevY))/(len(listStanDevY)-1))
  ##print(stanDevY)

  listAB = []
  for i in (0, len(minutesOfSAP)-1):
    a = float(minutesOfSAP[i]) - float(meanOfTimes)
    b = float(VolumeOfSAP[i]) - float(meanOfVolumes)
    products = a*b
    listAB.append(products)
  correlation = (sum(listAB) / (stanDevX*stanDevY)) / (len(minutesOfSAP))
  ##print(correlation)

  slopeRegLine = correlation*(stanDevY/stanDevX)
  ##print(slopeRegLine)
  interpreterSAP(slopeRegLine, minListSent, volListSent, finalRating)

def interpreterSAP(val, minutesOfSAP, VolumeOfSAP, finalRating):
  xOne = int(minutesOfSAP[0])
  xTwo = int(minutesOfSAP[-1])
  yOne = int(VolumeOfSAP[0])
  yTwo = int(VolumeOfSAP[-1])
  roughSlope = (yTwo - yOne) / (xTwo - xOne)
  ##print(roughSlope)
  if (abs(roughSlope)) > (abs(val*2.5)):
    print("-There is an increasing amount of market participation - there is good liquidity. You can exit positions very easily.")
    finalRating += 2
  elif val == roughSlope:
    print("-There is not increase in liquidity.")
  else:
    print("-Liquidity change is increasing insignificantly. Maybe wait for a different time to enter position.")
  finalDecision(finalRating)

def finalDecision(finalRating):
  print("\n\n********************************************************************")
  print("\nWhat should you do?")
  if finalRating < 5:
    print("-->This stock isn't a good investment.")
  elif finalRating >= 5 and finalRating < 7:
    print("-->This stock isn't a great choice.")
  elif finalRating >= 7 and finalRating < 9:
    print("-->Stock is a good buy.")
  else:
    print("-->Stock is a great choice. Invest now!")

#-----------------------------------------------------------------
#For demo, we are going to us MSFT (Microsoft stock) MAIN METHOD
print("MIDAS Financial Technologies TM")
print("This software tracks the performance of the top 10 companies currently listed on the S&P 500.")
print("Tickers:")
print("1: MSFT")
print("2: AAPL")
print("3: AMZN")
print("4: GOOG")
print("5: GOOGL")
print("6: FB")
print("7: BRK.B")
print("8: JNJ")
print("9: V")
print("10: PG")
userInput = input("\nPlease tell us a stock of your choice (Ticker Symbol with all caps): ")
#-----------------------------------------------------------------
finalRating = 0

listInfo = []
tickerName = None
marketCap = None
lastLetCap = None
pe_Ratio = None
dividendYield = None 

if userInput == "MSFT":
  infile = open("MSFT.txt", 'r')
  info = [line.rstrip() for line in infile]
  for i in info:
    listInfo.append(i)
  tickerName = listInfo[0]
  marketCap = listInfo [1]
  lastLetCap = marketCap[-1]
  pe_Ratio = listInfo [2]
  dividendYield = listInfo [3]
elif userInput == "AAPL":
  infile = open("AAPL.txt", 'r')
  info = [line.rstrip() for line in infile]
  for i in info:
    listInfo.append(i)
  tickerName = listInfo[0]
  marketCap = listInfo [1]
  lastLetCap = marketCap[-1]
  pe_Ratio = listInfo [2]
  dividendYield = listInfo [3]
elif userInput == "AMZN":
  infile = open("AMZN.txt", 'r')
  info = [line.rstrip() for line in infile]
  for i in info:
    listInfo.append(i)
  tickerName = listInfo[0]
  marketCap = listInfo [1]
  lastLetCap = marketCap[-1]
  pe_Ratio = listInfo [2]
  dividendYield = listInfo [3]
elif userInput == "BRK.B":
  infile = open("BRK.B.txt", 'r')
  info = [line.rstrip() for line in infile]
  for i in info:
    listInfo.append(i)
  tickerName = listInfo[0]
  marketCap = listInfo [1]
  lastLetCap = marketCap[-1]
  pe_Ratio = listInfo [2]
  dividendYield = listInfo [3]
elif userInput == "FB":
  infile = open("FB.txt", 'r')
  info = [line.rstrip() for line in infile]
  for i in info:
    listInfo.append(i)
  tickerName = listInfo[0]
  marketCap = listInfo [1]
  lastLetCap = marketCap[-1]
  pe_Ratio = listInfo [2]
  dividendYield = listInfo [3]
elif userInput == "GOOG":
  infile = open("GOOG.txt", 'r')
  info = [line.rstrip() for line in infile]
  for i in info:
    listInfo.append(i)
  tickerName = listInfo[0]
  marketCap = listInfo [1]
  lastLetCap = marketCap[-1]
  pe_Ratio = listInfo [2]
  dividendYield = listInfo [3]
elif userInput == "GOOGL":
  infile = open("GOOGL.txt", 'r')
  info = [line.rstrip() for line in infile]
  for i in info:
    listInfo.append(i)
  tickerName = listInfo[0]
  marketCap = listInfo [1]
  lastLetCap = marketCap[-1]
  pe_Ratio = listInfo [2]
  dividendYield = listInfo [3]
elif userInput == "JNJ":
  infile = open("JNJ.txt", 'r')
  info = [line.rstrip() for line in infile]
  for i in info:
    listInfo.append(i)
  tickerName = listInfo[0]
  marketCap = listInfo [1]
  lastLetCap = marketCap[-1]
  pe_Ratio = listInfo [2]
  dividendYield = listInfo [3]
elif userInput == "PG":
  infile = open("PG.txt", 'r')
  info = [line.rstrip() for line in infile]
  for i in info:
    listInfo.append(i)
  tickerName = listInfo[0]
  marketCap = listInfo [1]
  lastLetCap = marketCap[-1]
  pe_Ratio = listInfo [2]
  dividendYield = listInfo [3]
elif userInput == "V":
  infile = open("V.txt", 'r')
  info = [line.rstrip() for line in infile]
  for i in info:
    listInfo.append(i)
  tickerName = listInfo[0]
  marketCap = listInfo [1]
  lastLetCap = marketCap[-1]
  pe_Ratio = listInfo [2]
  dividendYield = listInfo [3]
else:
  exit("Error: Please try running program and entering a valid ticker")
#---------------------------------------------------------------

#tickerName = listInfo[0]
#marketCap = listInfo [1]
#lastLetCap = marketCap[-1]
#pe_Ratio = listInfo [2]
#dividendYield = listInfo [3]

print("Your selected stock: "+userInput+ "("+tickerName+")")
print("-------------------------------------------")
print("Important metrics")
flag = 0
while flag < 2:
  print("")
  flag += 1

print("Market Cap: "+marketCap)
print("P/E ratio: "+pe_Ratio)
print("Dividend yield(in %): "+dividendYield)

#-----------------------------------------------------------------
newList = []
minutes = []
finalPrices = []

a = open("prices.txt", 'r')
price = [line.rstrip() for line in a]
for i in price:
  newList.append(i)
for nums in price:
  finalPrices.append(float(nums))

##print(finalPrices)
for thePrice in range(0, len(price)):
  #print(price.index(price[thePrice]))
  minutes.append(float(thePrice))

##print(minutes)
##print(finalPrices)


#-------------------------------------------------------------------
#S&P 500 
newList2 = []
minutesSAP = []
finalPrices2 = []
print("-------------------------------------------")
print("\nOverall Market Summary\n")
b = open("S&P500Prices.txt", 'r')
sap = [line.rstrip() for line in b]
for i in sap:
  newList2.append(i)
for nums in sap:
  finalPrices2.append(float(nums))
for thePrice2 in range(0, len(sap)):
  minutesSAP.append(float(thePrice2))

#print(minutesSAP)
#print(finalPrices2)
##Volume of S&P500 
newList3 = []
minutesSAPVol = []
finalVolume = []
c = open("S&P500Volume.txt", 'r')
sapVol = [line.rstrip() for line in c]
for i in sapVol:
  newList3.append(i)
for nums in sapVol:
  finalVolume.append(float(nums))
for theVolume in range(0, len(sapVol)):
  minutesSAPVol.append(float(theVolume))

correlationCalculator(minutes, finalPrices, finalRating, marketCap, lastLetCap, finalPrices2, minutesSAPVol, finalVolume,pe_Ratio, dividendYield)

