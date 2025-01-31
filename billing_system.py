name=input('enter your name: ')
item={1:'tea',2:'poha',3:'misal',4:'shev-bhaji',5:'pav-bhaji',6:'chole-bhature',7:'paneer-bhaji',8:'rajma-chawal',9:'vage-kolhapuri',10:'bhendi-fry'}
price={1:12,2:20,3:130,4:80,5:70,6:80,7:100,8:50,9:80,10:85}
l=[]
z=[]

print('-'*107)
print(' '*40,'HOTEL IRA')
print('-'*107)

print(" "*30,'Coustomer Name:',name.title())
while True:
    print("""
                                            MENU
                                1.tea               2.poha
                                3.misal             4.shev-bhaji
                                5.pav-bhaji         6.chole-bhature
                                7.paneer-bhaji      8.rajma-chawal
                                9.vage-kolhapuri    10.bhendi-fry

    """)


    p=int(input('enter a item: '))
    q=int(input('enter a quantity: '))
    ch=input('enter a choice(y/n): ')
    l.append(p)
    z.append(q)
    if ch=="n":
        print('-'*107)
        print('{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format('SR.NO','item','quantity','price','amount'))
        print('-'*107)
        sum=0

        for i in range(len(l)):
            print('-'*107)
            print('{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format(i+1,item[l[i]],z[i],price[l[i]],price[l[i]]*z[i]))
            print('-'*107)
            

            sum=sum+price[l[i]]*z[i]
        print(" "*30,"Total Pyable Amount is:",sum)
        print(" "*30,'thank you')


        break