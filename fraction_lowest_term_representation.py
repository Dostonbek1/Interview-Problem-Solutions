#######################################################################
# Author: Dostonbek Toirov
#######################################################################

def EKUB(surat, maxraj):
    while surat % maxraj != 0:
        eski_surat = surat
        eski_maxraj = maxraj
        surat = eski_maxraj
        maxraj = eski_surat%eski_maxraj
    return maxraj

def main():
    surat = 8
    maxraj = 256
    ekub = EKUB(surat, maxraj)
    yangi_surat = int(surat / ekub)
    yangi_maxraj = int(maxraj / ekub)
    print(str(yangi_surat)+'/'+str(yangi_maxraj))

main()
