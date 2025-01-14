size=26
main_str=""
for _ in range(96+size,96,-1):
    main_str=main_str+(chr(_)+"-")
center_str=main_str+main_str[len(main_str)-4::-1]


#top cone
list_chr=""
final=[]
for k in range(96+size,97,-1):
    center_chr=chr(k)
    list_chr=list_chr+center_chr
    temp_str=list_chr[0:len(list_chr)-1]+list_chr[::-1]
    printing_str="-".join(c for c in temp_str)
    len_=(len(center_str))
    final.append(printing_str.center(len_,"-"))
print(*final,sep='\n')
#printing the centre cone

print(center_str)

#down cone
print(*final[::-1],sep='\n')
