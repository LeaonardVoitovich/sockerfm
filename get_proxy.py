import io
import os

#read string from user
def fm_proxychains ():
    path = input('Enter input path : ')

    print('path',path)
    path = './'+path

    pathtype = input('Enter socks type : ')


    with open(path, 'r') as f:
        contents = f.readlines()

    for line in contents:
        print (pathtype+' '+line.replace (':', ' ')) 


    with open("./"+"out.txt", 'w') as f:
        for line in contents:
            f.writelines(pathtype+' '+line.replace (':', ' ')) 


def fm_bot ():
    path = 'out.txt'
    with open(path, 'r') as f:
        contents = f.readlines()
    with open('out_formated.txt', 'w') as f:
        #print ("".join(contents), end='')
        for line in contents:
            f.write('"'+ line.replace ("\n", " ")+'"'+',') 



if __name__ == "__main__":
    #os.system('curl -O https://cdn.uashield.cc/proxies.txt')
    os.system("python3 socker.py -u https://cdn.uashield.cc/proxies.txt -o out.txt")
    fm_bot()