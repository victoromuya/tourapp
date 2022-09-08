from flask import Flask, render_template, request, url_for, redirect
import pandas as pd
import pred
import convert
import numpy as np
from os import listdir
from os.path import isfile, join
import pickle

from collections import Counter

app = Flask(__name__, static_url_path="/static", static_folder="static")


@app.route('/', methods=['GET'])
def hello():

    return render_template('index.html')


@app.route('/home', methods=['GET'])
def home():

    return render_template('register.html')


@app.route("/", methods=['POST'])
def predict():
    imagefile = request.files.get('imagefile')
    imagepath = "./images/"+imagefile.filename
    imagefile.save(imagepath)

    return render_template('index.html')


@app.route('/admin', methods=['POST', 'GET'])
def admins():

    if request.method == 'POST':
        # return render_template('user.html', result = result)
        result = request.form
        reader = pd.read_csv(r'tour.csv', encoding='unicode_escape')

        dfreader = reader.copy()
        region = result['region']
        city = result['city']
        category = result['category']
        name = result['name']
        biaography = result['biaography']
        location = result['location']
        cordinates = result['cordinates']
        worktime = result['worktime']
        link = result['link']
        tourist_info = name + ';' + worktime + ';' + \
            location + ';' + cordinates + ';' + biaography + ';' + link

        if name == "" or region == "" or city == "" or biaography == "" or location == "" or cordinates == ""\
                or worktime == "" or link == "":
            message1 = "kindly fill all fields before submiting"
            return render_template('admin.html', mess1=message1)
        else:
            diction = [[region, city, category, name, biaography,
                        location, cordinates,  worktime, link, tourist_info]]
            df = pd.DataFrame(diction, columns=[
                'Region', 'City', 'Category', 'Name of the tourist site ', 'Biaography', 'Location', 'Cordinates ', 'Worktime', 'Website link', 'tourist_info'])

            dataf = pd.concat(
                [dfreader, df], ignore_index=True, sort=False)
            dataf.to_csv('tour.csv', index=False)

            imagefile = request.files.get('imagefile')
            imagefile.filename = name+" 2 .jpg"
            imagepath = "./static/Photos/"+imagefile.filename
            imagefile.save(imagepath)
            message2 = "Successfully added"
            return render_template('admin.html', mess2=message2)

    return render_template('admin.html')


@app.route('/reg', methods=['POST', 'GET'])
def reg():

    if request.method == 'POST':
        # return render_template('user.html', result = result)
        result = request.form
        reader = pd.read_csv(r'tourist.csv')

        dfreader = reader.copy()

        username = result['username']
        age = result['age']
        gender = result['gender']
        degree = result['degree']
        status = result['status']
        ethnicity = result['ethnicity']
        job_title = result['job_title']
        Job_Industry = result['job_industry']

        if username == "" or gender == "Gender" or degree == "Interest" or status == ""\
                or ethnicity == "" or job_title == "" or Job_Industry == "Job Industry":
            message1 = "kindly fill all fields before submiting"
            return render_template('register.html', mess1=message1)
        else:
            diction = [[username, age, gender, degree,
                        status, ethnicity, job_title, Job_Industry]]
            df = pd.DataFrame(diction, columns=[
                              'username', 'age', 'gender', 'degree', 'status', 'ethnicity', 'job_title', 'Job_Industry'])

            listname = []
            for items in reader['username']:
                listname.append(items)
            ele = df['username'].values
            if ele in listname:
                message = "username already exist, choose another one"
                return render_template('register.html', mess=message)
            else:
                dataf = pd.concat(
                    [dfreader, df], ignore_index=True, sort=False)
                dataf.to_csv('tourist.csv', index=False)

    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        result = request.form
        uname = result['username']
        # Region = result['city']
        # diction = [[Region, Category]]

        dfread = pd.read_csv(r"tour.csv", encoding='unicode_escape')
        log = pd.read_csv(r"tourist.csv")  # data for predicting

        dataf = log.loc[log['username'] == uname]
        age = dataf['age'].values
        print(age)
        gender = dataf['gender'].values
        degree = dataf['degree'].values
        status = dataf['status'].values
        ethnicity = dataf['ethnicity'].values
        Job_Industry = dataf['Job_Industry'].values

        ages = convert.age(age)
        genders = convert.sex(gender)
        degrees = convert.deg(degree)
        statuss = convert.status(status)
        ethnicitys = convert.eth(ethnicity)
        Job_Industrys = convert.job(Job_Industry)

        mydata = [[ages, genders, ethnicitys, degrees, Job_Industrys, statuss]]
        df = pd.DataFrame(
            mydata, columns=['Age', 'Sex', 'Ethnic', 'Qualification', 'career', 'Status'])

        # importing the model
        model = 'model/tourist_model1.sav'
        with open(model, 'rb') as file:
            the_model = pickle.load(file)

        predicted = the_model.predict(df)
        if predicted[-1] == 0:
            inter = 'Historical'
        elif predicted[-1] == 1:
            inter = 'Tourist'
        elif predicted[-1] == 2:
            inter = 'Islamic'
        elif predicted[-1] == 3:
            inter = 'Tourist and Historical'

        interest = inter  # should come from model

        """
        age = dataf['age'].values[0]
        gender = dataf['gender'].values[0]
        city = dataf['city'].values[0]
        nation = dataf['nationality'].values[0]
            """

        dff = dfread.loc[dfread['Category'] == interest]

        # import the function
        res = pred.recommend(interest, dff['tourist_info'].values[0])

        num = np.arange(len(res))
        num = num[0:]+1
        data = {'Number': num, 'tourist_info': res}
        rec = pd.DataFrame(data)

        new_df = pd.merge(dff, rec, on=['tourist_info'], how='inner')
        needed = new_df[['Region', 'Category', 'Name of the tourist site ', 'Biaography',
                         'Location', 'Cordinates ', 'Worktime', 'Website link']]
        needed2 = needed.loc[1:]
        lenght2 = len(needed2)

        lenght = len(needed)
        img = needed.loc[0][2]

        """
        mypath = "static"
        new_a = []
        new_img = []
        onlyfile = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for a in onlyfile:
            a = (a[0:-6])
            a = ([a])
            new_a.append(a)

        flatlist = [element for sublist in new_a for element in sublist]
        a = list(set(flatlist))
        """
        jpeg = []
        val = needed['Name of the tourist site '].values
        img_names = val+" 2.jpg"

        for items in img_names:
            ig_jpg = r"static/Photos/%s" % items
            jpeg.append(ig_jpg)

        ig = jpeg
        ig2 = ig[1:]

    return render_template('recon.html', uname=uname, age=age, gender=gender, inter=interest, lent=lenght, lent2=lenght2, content=needed, content2=needed2, imgg=ig, imgg2=ig2)


@ app.errorhandler(404)
def page_not_found(e):
    return render_template('errorpage.html')


if __name__ == '__main__':
    app.run(port=3002, debug=True)
