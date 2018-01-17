
total = 1.0

for den in range(11, 100):
    for num in range(10,den):
        denc = -1
        numc = 0
        fraci = float(num)/float(den)
        nums = str(num)
        dens = str(den)
        if int(dens[1]) ==  0 and int(nums[1]) == 0: continue
        if nums[0] == dens[0]:
            denc = dens[1]
            numc = nums[1]
        if nums[1] == dens[0]:
            denc = dens[1]
            numc = nums[0]
        if nums[0] == dens[1]:
            denc = dens[0]
            numc = nums[1]
        if nums[1] == dens[1]:
            denc = dens[0]
            numc = nums[0]
        numc = float(numc)
        denc = float(denc)
        if denc == 0: continue
        fracc = numc/denc
        if fraci == fracc:
            print "%i/%i and %i/%i equals %f" %(num, den, numc, denc, fracc)
            total *= fracc
print total
