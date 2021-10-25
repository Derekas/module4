
def menu():
    print("1-Show ful store details")
    print("2-Sales")
    print("3-Replace")
    print("3-Change price of products")
    print("5-Exit")
    opcion=int(input("Introduzca un numero: "))
    return opcion

cash = 129.9
quantProducts = {1: 10, 2: 4, 3: 8, 4: 9}
priceProduct = {1: 9.99, 2: 19.9, 3: 14.99, 4: 4.99}

print(priceProduct[2])


def getPriceProduct(code):
    price=priceProduct[code]
    return price

code2= int(input("Introduce el codigo que desee saber su precio"))
print(getPriceProduct(code2))

def getQuantProducts(code):

    return quantProducts[code]

code2= int(input("Introduce el codigo que desee saber su cantidad"))
print(getQuantProducts(code2))

def getDetailProducts(code):
    result=[]
    result.append(priceProduct[code])
    result.append(priceProduct[code])
    return result

code3= int(input("Introduce el codigo que desee saber su precio y cantidad"))
print(getDetailProducts(code3))

def getCash():
    print(cash)


def addQuantProduct(code,quantity):
    quant =quantProducts[code]
    quantProducts[code]= quant+quantity
    return quantProducts[code]

code=int(input("Introduzca el codigo que desea aumenta su cantidad "))
quant=int(input("Introduzca la cantidad a augmentar "))
print("La cantidad del codigo ",code," es ",addQuantProduct(code,quant))


def opcion4(code,price):
    pricenow =priceProduct[code]
    priceProduct[code]= pricenow+price
    return priceProduct[code]




def opcion2(code):
    if(quantProducts[code]>0):
        quant=quantProducts[code]-1
        cashnow=cash+priceProduct[code]
        return True
    else:
        return False




def opcion3(code,quantity):
    if(code<=4):
        if(quantProducts[code]>=quantity):
            quantProducts[code]-quantity
            return True
        else: 
            return False




def opcion1():
    result=[]
    result.append(("Code-Unit-Price"))
    for i in quantProducts:
        result.append((quantProducts[i],priceProduct[i]))
    return result
def opcion5():
        print("Saliendo..")


while opcion!=5:

    opcion= menu()


    if opcion==1:
        print(opcion1())

    if opcion==2:
        codesaleProduct=int(input("Introduzca el codigo que desea vender "))
        if(opcion2(codesaleProduct)):
            print("Es posible ejecutar la operación")
        else:
            print("No ha sido posible efectuar la operación")

    if opcion==3:
        code=int(input("Introduzca el codigo que desea remplazar"))
        quantity=int(input("Introduzca la cantidad "))  
        if(opcion3(code,quantity)):
            print("Es posible ejecutar la operación")
        else:
            print("No ha sido posible efectuar la operación")

    if opcion==4:
        code=int(input("Introduzca el codigo que desea aumenta su precio "))
        priceincrement=int(input("Introduzca el precio a augmentar "))
        print("El precio del codigo ",code, " es ",addQuantProduct(code,priceincrement))

    if opcion==5:
        opcion5()

    