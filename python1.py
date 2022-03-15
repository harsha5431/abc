dictOfWords = {
	"hello" : 50, "at" : 23, "test" : 56, "this" : 77, "here" : 43, "now" : 55}
def getKeysByValue(dictOfElements, valueToFind):
	listofKeys = list()
	listOfItems =  dictOfElements.items()
	for item in listOfItems:
		if item[1] == valueToFind:
			listofKeys.append(item[0])
	return listofKeys

listOfKeys = getKeysByValue(dictOfWords, 43)
print("Keys with value equal to 45")
for key in listOfKeys: 
	print(key)
