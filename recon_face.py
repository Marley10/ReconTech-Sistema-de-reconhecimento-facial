import cv2, sys, numpy, os, subprocess, time, MySQLdb

con = MySQLdb.connect('localhost', 'root', 'equiped')
con.select_db('equipeD')

cursor = con.cursor()
cursor.execute('SELECT * FROM dadosuser')
dados = cursor.fetchall()


processo1 = subprocess.call([ "echo 35 > /sys/class/gpio/export",""], shell = True)
processo2 = subprocess.call(["echo out > /sys/class/gpio/gpio35/direction",""], shell = True)
processo3 = subprocess.call(["echo 24 > /sys/class/gpio/export",""],shell = True)
processo4 = subprocess.call(["echo out > /sys/class/gpio/gpio24/direction",""], shell = True)
processo5 = subprocess.call(["echo 36 > /sys/class/gpio/export",""], shell = True)
processo6 = subprocess.call(["echo out > /sys/class/gpio/gpio36/direction",""], shell = True)
size = 4
haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'datasets'
print('Processando...')
(images, labels, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(datasets):
    for subdir in dirs:
        
	names[id] = subdir
        subjectpath = os.path.join(datasets, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            label = id
            images.append(cv2.imread(path, 0))
            labels.append(int(label))
        id += 1
(width, height) = (130, 100)
(images, labels) = [numpy.array(lis) for lis in [images, labels]]

model = cv2.createFisherFaceRecognizer()
model.train(images, labels)

face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)
while True:
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        prediction = model.predict(face_resize)
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)

        if prediction[1]<500:

	       cv2.putText(im,'%s - %.0f' % (names[prediction[0]],prediction[1]),(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))

	       nome2 = (names[prediction[0]])

	       for i in dados:
		    if i[1]==(names[prediction[0]],prediction[1]):
			print (i[2])

	       cursor.execute("SELECT CPF FROM dadosuser WHERE Nome='%s'"% nome2)
	       cpfprin = cursor.fetchone()

	       processo10 = subprocess.call(["echo 1 > /sys/class/gpio/gpio24/value",""], shell = True)
	       processo11 = subprocess.call(["echo 1 > /sys/class/gpio/gpio36/value",""], shell = True)
	       processo13 = subprocess.call(["echo 0 > /sys/class/gpio/gpio35/value",""], shell = True)
	       time.sleep(1)
	       processo14 = subprocess.call(["echo 0 > /sys/class/gpio/gpio24/value",""], shell = True)
	       processo15 = subprocess.call(["echo 0 > /sys/class/gpio/gpio36/value",""], shell = True)
	       processo16 = subprocess.call(["echo 1 > /sys/class/gpio/gpio35/value",""], shell = True)
	       print nome2
	       print cpfprin
	       break
		 
    	else:
    	  cv2.putText(im,'Desconhecido',(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
	  processo17 = subprocess.call(["echo 1 > /sys/class/gpio/gpio35/value",""], shell = True)
    
    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(10)
    if key == 27:
        break
