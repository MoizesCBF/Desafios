# Proposta por @Like_a_NachozBR#5267

def bissextow(x):
    return (x%400==0 or
            (x%100!=0 and x%4==0 ))


def huluculu(x):
    return (x%15==0)


def bulukulu(x):
    return (bissextow(x) and x%55==0)


y = -1
while True:
    try:
        x = int(input())
        if y!=-1:
            print()
        else:
            y=1

        if (bissextow(x) or huluculu(x)
            or bulukulu(x)):

            if bissextow(x):
                print("This is leap year.")
            if huluculu(x):
                print("This is huluculu "
                      "festival year.")
            if bulukulu(x):
                print("This is bulukulu "
                      "festival year.")
        else:
            print("This is an ordinary"
                  " year.")
    except:
        break