from flask import Flask, flash, redirect, send_file, url_for
from flask import render_template, request
from flask_pymongo import PyMongo
from werkzeug.utils import secure_filename
import os
from os import path
import subprocess
import fileinput
import csv
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from keras import backend as K


app = Flask(__name__)
app.secret_key = "secret key"
app.config["MONGO_URI"] = "mongodb://localhost:27017/cvedb"
mongo = PyMongo(app)
UPLOAD_FOLDER = '/home/php/PycharmProjects/BEProject/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


from app import app


ALLOWED_EXTENSIONS = set(['pcap'])


@app.route('/')
@app.route('/index')
def index():
    # user = {'username': 'Miguel'}
    return render_template('index.html')


@app.route('/module1')
def module1():
    return render_template('module1.html')


def RunModule1(filename):
    os.system(
        " /usr/bin/bro -r " + filename + " /home/php/Desktop/tcpdump2gureKDDCup99-master/darpa2gurekddcup.bro >  npcap.list")
    os.system("sort -n npcap.list > npcap_sort.list")
    subprocess.call(["gcc", "/home/php/Desktop/tcpdump2gureKDDCup99-master/trafAld.c"])  # For Compiling
    subprocess.call(["./a.out", "npcap_sort.list"])
    # --------------------------------------------------------------------------------------------------------
    filename = "trafAld.list"
    text_to_search = " "
    replacement_text = ","
    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(text_to_search, replacement_text), end='')

    # --------------------------------------------------------------------------------------------------------
    os.rename(filename, 'npcap2.csv')

    # --------------------------------------------------------------------------------------------------------
    with open('/home/php/PycharmProjects/BEProject/npcap2.csv', newline='') as f:
        r = csv.reader(f)
        data = [line for line in r]
    with open('/home/php/PycharmProjects/BEProject/npcap3.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(
            ['ColA', 'ColB', 'ColC', 'ColD', 'ColE', 'ColF', 'ColG', 'ColH', 'ColI', 'ColJ', 'ColK', 'ColL', 'ColM',
             'ColN', 'ColO', 'ColP', 'ColQ', 'ColR', 'ColS', 'ColT', 'ColU', 'ColV', 'ColW', 'ColX', 'ColY', 'ColZ',
             'ColAA', 'ColAB', 'ColAC', 'ColAD', 'ColAE', 'ColAF', 'ColAG', 'ColAH', 'ColAI', 'ColAJ', 'ColAK', 'ColAL',
             'ColAM', 'ColAN', 'ColAO', 'ColAP', 'ColAQ', 'ColAR', 'ColAS', 'ColAT', 'ColAU'])
        w.writerows(data)

    # -------------------------------------------------------------------------------
    data = pd.read_csv('/home/php/PycharmProjects/BEProject/npcap3.csv')
    data = data.drop(
        ["ColA", "ColM", "ColN", "ColP", "ColQ", "ColR", "ColS", "ColT", "ColU", "ColV", "ColW", "ColX", "ColY", "ColZ",
         "ColAA", "ColAB", "ColAF", "ColAG", "ColAT", "ColAU"], axis=1)
    data.to_csv("/home/php/PycharmProjects/BEProject/npcap4.csv", index=False, sep=',')

    # --------------------------------------------------------------------------------------------------------
    with open("/home/php/PycharmProjects/BEProject/npcap4.csv", 'r') as f:
        with open("/home/php/PycharmProjects/BEProject/npcap5.csv", 'w') as f1:
            next(f)  # skip header line
            for line in f:
                f1.write(line)

    # --------------------------------------------------------------------------------------------------------
    subprocess.call(["javac", "/home/php/PycharmProjects/BEProject/KDD.java"])  # For Compiling
    print(subprocess.call(["java", "KDD", "/home/php/PycharmProjects/BEProject/npcap5.csv",
                           "/home/php/PycharmProjects/BEProject/npcap_cat.csv"]))
    # --------------------------------------------------------------------------------------------------------

    # --------------------------------------------------------------------------------------------------------
    dataset = pd.read_csv('/home/php/PycharmProjects/BEProject/npcap_cat.csv')
    dataset1 = np.array(dataset)
    X = StandardScaler().fit_transform(dataset1)
    pca = PCA(n_components=0.99, whiten=True)
    X_pca = pca.fit_transform(X)
    np.savetxt("/home/php/PycharmProjects/BEProject/npcap_cat_reduced.csv", X_pca, delimiter=",")
    # Testing
    output_string = Testfor("npcap_cat_reduced.csv")
    return output_string


def Testfor(filename):
    x = pd.read_csv(filename)
    import pickle
    f = open('/home/php/PycharmProjects/BEProject/NN_400_dataset2.sav', 'rb')
    model = pickle.load(f)
    shape = (x.shape[0], 19)
    zeros = np.zeros(shape, dtype=np.int32)
    zeros[:x.shape[0], :x.shape[1]] = x
    y_test_predict = model.predict(zeros)
    #print(y_test_predict)
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i in range(len(y_test_predict)):
        if y_test_predict[i] < 1:
            cnt1 = cnt1 + 1
        elif y_test_predict[i] < 2:
            cnt2 = cnt2 + 1
        elif y_test_predict[i] < 3:
            cnt3 = cnt3 + 1
    max_sc = max(cnt1, cnt2, cnt3)
    if cnt1 == max_sc or cnt1 >= (max_sc/3):
        print("Normal")
        return "No attack detected"
    elif cnt2 == max_sc:
        print("ARP")
        return "ARP attack detected"
    elif cnt3 == max_sc:
        print("DOS")
        return "DOS attack detected"
    K.clear_session()


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded.Please wait while processing...')
            output_string = RunModule1(filename)
        else:
            flash("Please select pcap file only")

    return render_template('module1.html', string=output_string)


@app.route('/module2')
def module2():
    return render_template('module2.html')


@app.route('/cveExtraction', methods=['GET', 'POST'])
def cve_extraction():
    if request.method == 'POST':
        if path.exists("version2.txt"):
            # print(fpath)
            # with open(fpath, mode='r') as file:
            # string = "File already exists.Press Download to download it!"
            string = "File with vulnerable softwares is created. Press Download to download it!"
            #     string += file.read().replace('\n', '')
            # file.close()
            return render_template('module2.html', string=string)
        else:
            os.system("dpkg --get-selections >list.txt")
            file1 = open("SoftWareName.txt", "w")

            with open("list.txt") as fp:
                for line in fp:
                    arr = line.split('	')
                    if arr[0].find(':'):
                        str1 = arr[0].split(':')
                        # str2 = str(os.system("apt-cache policy "+ str1[0]))
                        subprocess.Popen(['apt-cache', 'policy', str1[0]], stdout=file1)
                    # file1.write(str2)
                    # print(str2)
                    else:
                        # str2 = str(os.system("apt-cache policy "+ arr[0]))
                        subprocess.Popen(['apt-cache', 'policy', arr[0]], stdout=file1)
                    # file1.write(str2)
                    # print(str2)

            file1.close()

            file1 = open("version2.txt", "w")

            with open("SoftWareName.txt") as fp:
                prev1 = ""
                for line in fp:
                    if line.find('Installed') != -1 and line.find('none') == -1:
                        # print(line)
                        arr = line.split(': ')

                        if arr[1].find(':') != -1:
                            arr2 = arr[1].split(':')
                            idx1 = idx2 = idx3 = idx4 = idx5 = 1000
                            if arr2[1].find('+') or arr2[1].find('-') or arr2[1].find('~') or arr2[1].find('.dfsg') or \
                                    arr2[1].find('ubun'):
                                if arr2[1].find('+') != -1:
                                    idx1 = arr2[1].index('+')
                                if arr2[1].find('-') != -1:
                                    idx2 = arr2[1].index('-')
                                if arr2[1].find('~') != -1:
                                    idx3 = arr2[1].index('~')
                                if arr2[1].find('.dfsg') != -1:
                                    idx4 = arr2[1].index('.dfsg')
                                if arr2[1].find('ubun') != -1:
                                    idx5 = arr2[1].index('ubun')

                                idx = min(idx1, idx2, idx3, idx4, idx5)
                                # print(idx)
                                if idx == 1000:
                                    file1.write(prev1[0] + arr2[1] + "\n")
                                else:
                                    arr3 = arr2[1].split(arr2[1][idx])
                                    file1.write(prev1[0] + arr3[0] + "\n")


                        else:

                            idx1 = idx2 = idx3 = idx4 = idx5 = 1000
                            if arr[1].find('+') or arr[1].find('-') or arr[1].find('~') or arr[1].find('.dfsg') or arr[
                                1].find('ubun'):
                                if arr[1].find('+') != -1:
                                    idx1 = arr[1].index('+')
                                if arr[1].find('-') != -1:
                                    idx2 = arr[1].index('-')
                                if arr[1].find('~') != -1:
                                    idx3 = arr[1].index('~')
                                if arr[1].find('.dfsg') != -1:
                                    idx4 = arr[1].index('.dfsg')
                                if arr[1].find('ubun') != -1:
                                    idx5 = arr[1].index('ubun')

                                idx = min(idx1, idx2, idx3, idx4, idx5)
                                # print(idx)
                                if idx == 1000:
                                    file1.write(prev1[0] + arr[1] + "\n")
                                else:
                                    arr3 = arr[1].split(arr[1][idx])
                                    file1.write(prev1[0] + arr3[0] + "\n")

                    prev1 = line.split('\n')

            file1.close()

            file1 = open("vulnerableSoftwares.txt", "w")
            string = ""
            with open("version2.txt") as fp:
                for line in fp:
                    if line != "\n":
                        temp = line.split('\n')
                        sname = temp[0].split(':')
                        query = {"vulnerable_product": {"$regex": "cpe:/a.*" + sname[0] + ".*" + sname[1] + ".*"}}
                        mydoc = mongo.db.cves.find(query, {"id": 1})

                        for x in mydoc:
                            string += str(x)
                            file1.write(str(x) + "\n")
            string = "File with vulnerable softwares is created. Press Download to download it!"
            return render_template('module2.html', string=string)


@app.route('/return-files/')
def return_files_tut():
    fpath = os.path.abspath("version2.txt")
    try:
        return send_file(fpath, attachment_filename="version2.txt")
    except Exception as e:
        return str(e)




if __name__ == '__main__':
    app.debug = True
    app.run()
