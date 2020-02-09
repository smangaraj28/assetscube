from . import bp_ologin
from flask import redirect, request, make_response, jsonify
from assetscube.common import dbfunc as db
from assetscube.common import error_logics as errhand


@bp_ologin.route("/")
def hello():
    return jsonify('adfadfadf')


@bp_ologin.route('/ologin1', methods=["GET", "POST"])
def ologins():
    if request.method == "POST":
        print("0login")
        attempted_username = request.get_json(force=True)['username']
        attempted_password = request.get_json(force=True)['password']

        s = 0
        f = None
        t = None  # message to front end
        # attempted_username = 'natrayan'
        # attempted_password = 'natrayan'
        branchid = "test"
        hotelid = "test"
        print(attempted_username, attempted_password)
        print("here")
        if s <= 0:
            con, cur, s1, f1 = db.mydbopncon()
            s, f, t = errhand.get_status(s, s1, f, f1, t, "no")
            s1, f1 = 0, None
            print("DB connection established", s, f, t)

        if s <= 0:
            command = cur.mogrify("""
                                    SELECT json_agg(a) FROM (
                                    SELECT userid,username
                                    FROM unihot.userlogin
                                    WHERE userstatus = 'A' AND uName = %s AND uPassword = %s
                                    AND branchid = %s AND hotelid = %s
                                    ) as a
                                """, (attempted_username, attempted_password, branchid, hotelid,))
            print(command)
            cur, s1, f1 = db.mydbfunc(con, cur, command)
            s, f, t = errhand.get_status(s, s1, f, f1, t, "no")
            s1, f1 = 0, None
            print('----------------')
            print(s)
            print(f)
            print('----------------')
            if s > 0:
                s, f, t = errhand.get_status(s, 200, f, "App Name data fetch failed with DB error", t, "no")
        print(s, f)

        db_rec = None
        if s <= 0:
            db_rec = cur.fetchall()[0][0]
            print(db_rec)
            print(len(db_rec))
            print(db_rec[0])

            if db_rec == None or len(db_rec) > 1:
                s, f, t = errhand.get_status(s, 100, f, "User authentication failed", t, "yes")
            else:
                db_rec = db_rec[0]
                print("auth.py line 136 user auth successfully")
                pass

        print(s, f, t)
        print(db_rec)

        if s <= 0:
            redata = [{"uId": db_rec['uid'], "uName": db_rec['uname']}]
            res = make_response(jsonify(redata), 200)
            return res
        else:
            return jsonify(False)



@bp_ologin.route('/osignup', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print("osignup")
        attempted_username = request.get_json(force=True)['username']
        attempted_password = request.get_json(force=True)['password']

        s = 0
        f = None
        t = None  # message to front end
        # attempted_username = 'natrayan'
        # attempted_password = 'natrayan'
        branchid = "test"
        hotelid = "test"
        print(attempted_username, attempted_password)
        print("here")
        if s <= 0:
            con, cur, s1, f1 = db.mydbopncon()
            s, f, t = errhand.get_status(s, s1, f, f1, t, "no")
            s1, f1 = 0, None
            print("DB connection established", s, f, t)

        if s <= 0:
            command = cur.mogrify("""
                        INSERT INTO ncusr.userlogin (userid, username, useremail, userstatus, userstatlstupdt, octime, lmtime, entityid, countryid) 
                        VALUES (%s,%s,%s,%s,CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,%s,%s);
                        """,(userid, name, sinupemail, userstatus, entityid, countryid,))
                        
            print(command)
            cur, s1, f1 = db.mydbfunc(con, cur, command)
            s, f, t = errhand.get_status(s, s1, f, f1, t, "no")
            s1, f1 = 0, None
            print('----------------')
            print(s)
            print(f)
            print('----------------')
            if s > 0:
                s, f, t = errhand.get_status(s, 200, f, "App Name data fetch failed with DB error", t, "no")
        print(s, f)

        db_rec = None
        if s <= 0:
            db_rec = cur.fetchall()[0][0]
            print(db_rec)
            print(len(db_rec))
            print(db_rec[0])

            if db_rec == None or len(db_rec) > 1:
                s, f, t = errhand.get_status(s, 100, f, "User authentication failed", t, "yes")
            else:
                db_rec = db_rec[0]
                print("auth.py line 136 user auth successfully")
                pass

        print(s, f, t)
        print(db_rec)

        if s <= 0:
            redata = [{"uId": db_rec['uid'], "uName": db_rec['uname']}]
            res = make_response(jsonify(redata), 200)
            return res
        else:
            return jsonify(False)