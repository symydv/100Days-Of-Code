#one can of paint can paint 5 feet square of area
#calculate cans of paint needed to paint the given area

length_of_wall = int(input("what is  the length of your wall?"))
width_of_wall = int(input("what is width of wall?"))
ek_dabba_kitni_wall_paint_kar_sakta_hai = 5

def cans_of_paint(lenght=length_of_wall,width=width_of_wall,ek_dabba_kitni_wall_paint_kar_sakta_hai=5):

    area= lenght*width

    cansrequired = int(area/ek_dabba_kitni_wall_paint_kar_sakta_hai) + 1

    print(f"you will require {cansrequired} cans of paint")

cans_of_paint()
