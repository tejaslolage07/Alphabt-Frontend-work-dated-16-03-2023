from crypt import methods
from flask import *
import mysql.connector as c
import xlsxwriter
from flask_cors import CORS, cross_origin

# app = Flask(__name__)
app = Flask(__name__, template_folder='./templates')
CORS(app)

@app.route('/')
def hello():
    return {
        "Hello world": "Hello bro",
        "Hello man": "Hello woman",
        "Hello boy": "Hello girl",
    }

#change connection values as per pc
# con = c.connect(host="127.0.0.1", user="phpmyadmin", passwd="tvsm123!", database="axle_inspection")
# start_time = input("Enter start time: ") #'2021-08-12T10:57:26'
# end_time = input("Enter end time: ") #'2021-08-12T15:04:28'
# camera_id = 'rhs_axle'
# @app.route('/check/<start_time>/<end_time>')
@app.route('/excel',methods=["POST", "GET"])
@cross_origin()
def values(camera_id= 'rhs_axle'):
    if request.method == "POST":
        # start_time = f"{request.form['startD']}T{request.form['startT']}"
        # end_time = f"{request.form['endD']}T{request.form['endT']}"
        print("Start date in the form is: ", request.form['startD'])
        start_time = f"{request.form['startD']}"
        end_time = f"{request.form['endD']}"
        print(start_time, end_time)
        data = []
        count_axle = 0
        good = 0
        f = 0
        con = c.connect(host="127.0.0.1", user="phpmyadmin", passwd="tvsm123!", database="axle_inspection")
        if con.is_connected():
            print("Successfully Connected")
            workbook = xlsxwriter.Workbook('axle_data.xlsx')
            worksheet = workbook.add_worksheet()
            # resize cells
            worksheet.set_column('A1:M1',15)
            worksheet.set_column('C1:C5',34)
            #worksheet.set_column('D1:D2',34)
            #worksheet.set_column('J1:J2',20)
            #worksheet.set_column('G:G',20)
            worksheet.set_column('D:L',23)
            worksheet.set_row(0,25)
            worksheet.set_default_row(105)

            bold = workbook.add_format({'bold': True, 'font_size':14,'border':1,'align':'center'})
            bottom = workbook.add_format({'bold': True, 'font_size':16,'border':1,'align':'center'})
            red = workbook.add_format({'bold': True, 'font_size':16,'border':1,'align':'center','font_color':'red'})
            ok = workbook.add_format({'font_size':14,'border':1,'align':'center','font_color':'green'})
            not_ok = workbook.add_format({'font_size':14,'border':1,'align':'center','font_color':'red'})
            border = workbook.add_format({'font_size':12,'border':1,'align':'center'})
            worksheet.write('A1', 'Row ID', bold)
            worksheet.write('B1', 'Axle ID', bold)
            worksheet.write('C1', 'Processed Image', bold)
            worksheet.write('D1', 'Camera ID', bold)
            worksheet.write('E1', 'Scan Time', bold)
            worksheet.write('F1', 'Barcode', bold)
            worksheet.write('G1', 'Oil Seal', bold)
            worksheet.write('H1', 'Castle Nut',bold)
            worksheet.write('I1', 'T Pin',bold)
            worksheet.write('J1', 'Lock Nut',bold)
            worksheet.write('K1', 'Circle Clip',bold)
            worksheet.write('L1', 'Status',bold)

            db_cursor = con.cursor()
            db_cursor.execute(
                "SELECT `id`, `axle_id` , `inference_image_path`, `camera_id`, `timestamp` FROM `axle_data` WHERE "
                "axle_data.timestamp BETWEEN '{}' AND '{}'".format(start_time, end_time))
            lst = db_cursor.fetchall()

            if lst:
                for j in range(len(lst)):
                    main_dict = {
                        "row_id": None,
                        "axle_id": None,
                        "inference_image": None,
                        "camera_id": None,
                        "scan_time": None,
                        "barcode": "Absent",
                        "oil_seal_type": "Absent",
                        "castle_nut_presence": False,
                        "t_pin_presence": False,
                        "lock_nut_presence": False,
                        "circle_clip_presence": False

                    }
                    if lst[j][3]==camera_id:
                        key = lst[j][0]
                        main_dict["row_id"] = key
                        main_dict["axle_id"] = lst[j][1]
                        main_dict["inference_image"] = lst[j][2]
                        main_dict["camera_id"] = lst[j][3]
                        formatted_datetime = lst[j][4].isoformat()
                        main_dict["scan_time"] = formatted_datetime

                        db_cursor.execute(
                            "SELECT `barcode_value` FROM `axle_barcode_mapping` WHERE axle_id = {}".format(lst[j][1]))
                        samp = db_cursor.fetchall()
                        for i in range(len(samp)):
                            if samp:
                                main_dict["barcode"] = samp[0][0]

                        db_cursor.execute("SELECT axle_component_data.axle_data_id, all_component_list.model_name FROM "
                                        "axle_component_data INNER JOIN all_component_list ON "
                                        "axle_component_data.axle_component_id = all_component_list.model_id WHERE "
                                        "axle_component_data.axle_data_id = {}".format(key))
                        lstx = db_cursor.fetchall()

                        if lstx:
                            iterate = len(lstx)
                            for i in range(iterate):
                                if lstx[i][1] == 'castle_nut':
                                    main_dict["castle_nut_presence"] = True
                                elif lstx[i][1] == 't_pin':
                                    main_dict["t_pin_presence"] = True
                                elif lstx[i][1] == 'lock_nut':
                                    main_dict["lock_nut_presence"] = True
                                elif lstx[i][1] == 'circle_clip':
                                    main_dict["circle_clip_presence"] = True
                                elif lstx[i][1] == 'oil_seal_b':
                                    main_dict["oil_seal_type"] = 'Blue'
                                elif lstx[i][1] == 'oil_seal_g':
                                    main_dict["oil_seal_type"] = 'Grey'
                        # print(main_dict)
                        data.append(main_dict)

        if data:
            for row in range(1,len(data)+1):
                count_axle = count_axle+1
                inference_image_url = data[row-1]['inference_image']

                worksheet.write(row, 0, data[row-1]['row_id'],border)
                worksheet.write(row, 1, data[row-1]['axle_id'],border)
                if inference_image_url:
                    worksheet.insert_image(row, 2, inference_image_url, {'x_scale':0.117345,'y_scale':0.121,'x_offset':5,'y_offset':5,'positioning':1})
                    worksheet.write(row, 2, '',border)
                if data[row-1]['camera_id'] == 'rhs_axle':
                    worksheet.write(row, 3, 'RHS Axle',border)
                worksheet.write(row, 4, data[row-1]['scan_time'],border)
                worksheet.write(row, 5, data[row-1]['barcode'],border)
                worksheet.write(row, 6, data[row-1]['oil_seal_type'],border)
                if data[row-1]['castle_nut_presence'] == True:
                    worksheet.write(row, 7, 'Present',border)
                else:
                    worksheet.write(row, 7, 'Absent',border)
                if data[row-1]['t_pin_presence'] == True:
                    worksheet.write(row, 8, 'Present',border)
                else:
                    worksheet.write(row, 8, 'Absent',border)
                if data[row-1]['lock_nut_presence'] ==True:
                    worksheet.write(row, 9, 'Present',border)
                else:
                    worksheet.write(row, 9, 'Absent',border)
                if data[row-1]['circle_clip_presence'] == True:
                    worksheet.write(row,10, 'Present',border)
                else:
                    worksheet.write(row,10, 'Absent',border)

                if data[row-1]['castle_nut_presence'] and data[row-1]['t_pin_presence'] and data[row-1]['lock_nut_presence']:
                    good = good + 1
                    worksheet.write(row,11, 'OK',ok)
                else:
                    if data[row-1]['oil_seal_type'] != 'Absent' and data[row-1]['circle_clip_presence']:
                        good = good + 1
                        worksheet.write(row,11, 'OK',ok)
                    else:
                        worksheet.write(row,11, 'NOT OK',not_ok)
                f=row

        # Hide all rows without data.
        if f:
            ro1 = f+2
            ro2 = f+3
            print(count_axle)
            print(count_axle-good)
            worksheet.set_row(f+1,25)
            worksheet.set_row(f+2,25)
            co1 = str(ro1)
            co2 = str(ro2)
            worksheet.merge_range('A{}:C{}'.format(co1,co1), 'Total No. of Axle Scanned:', bottom)
            #worksheet.merge_range('B12:C12', 'Total Number of Axle Scanned:', bottom)
            worksheet.merge_range('A{}:C{}'.format(co2,co2), 'Total No. of Defective Axle:', bottom)
            #worksheet.write(f+1,2, 'Total Number of Axle Scanned:',bottom)
            #worksheet.write(f+2,2, 'Total Number of Defective Axle:',bottom)
            worksheet.write(f+1,3, count_axle,bottom)
            worksheet.write(f+2,3, count_axle-good,red)

        worksheet.set_default_row(hide_unused_rows=True)
        worksheet.set_column('M:XFD', None, None, {'hidden': True})


        while True:
            try:
                workbook.close()
            except xlsxwriter.exceptions.FileCreateError as e:
                decision = input("Exception caught in workbook.close(): %s\n"
                            "Please close the file if it is open in Excel.\n"
                            "Try to write file again? [y/n]: " % e)
                if decision != 'n':
                    continue
            break
        print(data)
        return jsonify(data)
    else:
        # return render_template("generate_excel_aug_21.html")
        return redirect("http://localhost:3001/dashboard", code=302)


# values(start_time,end_time,camera_id)
if __name__=="__main__":
	app.run(port=8081,debug=True)
