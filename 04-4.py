num=23
pvs_prime_not_found=True
while pvs_prime_not_found:
    num=num-1
    fact=0
    for i in range(2,num):
        if num%i==0:
            fact=1
            break
    if fact==0:
        print(f"pvs_prime_not_found={num}")
        pvs_prime_not_found=False