string="BANANA"
vowels = 'AEIOU'
score_kevin = 0
score_stuart = 0
n = len(string)
for i in range(n):
    if string[i] in vowels:
        score_kevin += n - i
        print(f"{score_kevin} += {n} - {i}  ")  
    else:
        score_stuart += n - i 
        print(f"{score_stuart} += {n} - {i}  ")
if score_kevin > score_stuart:
    print('Kevin', score_kevin)
elif score_stuart > score_kevin:
    print('Stuart', score_stuart)
else:
    print('Draw')

