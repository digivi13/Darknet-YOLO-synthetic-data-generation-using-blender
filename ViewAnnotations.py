import os
import cv2

for filename in os.listdir('/Users/thelabratory/documents/renders'):
    if filename.endswith('.jpg'):
        imgpath = os.path.join('/Users/thelabratory/documents/renders', filename)
        basename = os.path.splitext(filename)[0]
        txtfilename = basename + ".txt"
        txtpath = os.path.join('/Users/thelabratory/documents/renders', txtfilename)
        print(txtpath)
        image = cv2.imread(imgpath)
        xdimension = image.shape[1]
        print(xdimension)
        ydimension = image.shape[0]
        print(ydimension)
        array = []
        with open("%s" % txtpath, 'r') as current:
            lines = current.readlines()
            if not lines:
                print('FILE IS EMPTY')
            else:
                for line in lines:
                    print(line)
                    words = line.split(" ")
                    xmin = (float(words[1]) - (float(words[3]) / 2)) * xdimension
                    xmax = (float(words[1]) + (float(words[3]) / 2)) * xdimension
                    ymin = (float(words[2]) - (float(words[4]) / 2)) * ydimension
                    ymax = (float(words[2]) + (float(words[4]) / 2)) * ydimension
                    print(xmin)
                
                    cv2.rectangle(image,(int(xmin),int(ymin)),(int(xmax),int(ymax)),(0,255,0),2)
        #with open("%s" % txtpath) as f:
            #data = f.readlines()
            #f.close()
            #//print("file opened")
            #//if f.closed:
                #print ("file is closed")
            #else:
                #for line in f:
                    #print(str(line))
                    #array.append(line)

        #print(data)
        #for line in lines:
          #  print("executed")
          #  print (i)
          #  words = item.split(" ")
          #  xmin = float(words[1]) * xdimension
          #  print(xmin)
           # ymin = float(words[2]) * ydimension
           # xmax = float(words[3]) * xdimension
          #  ymax = float(words[4]) * ydimension
          #  cv2.rectangle(image,(xmin,ymin),(xmax,ymax),(0,255,0),2)
        
        cv2.imwrite(basename + "bbox.png", image)
        

                


        