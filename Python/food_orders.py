from typing import List

def displayTable(orders: List[List[str]]) -> List[List[str]]:
    ht = {}

    for l in orders:
        if l[1] in ht:
            ht[l[1]].append(l[2])
        else:
            ht.update({l[1]: [l[2]]})

    print(ht)

    

if __name__ == "__main__":
	orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
	print(displayTable(orders))