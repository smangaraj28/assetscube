from . import bp_nawg
from flask import redirect, request,make_response, jsonify

from assetscube.authentication import auth as a
from assetscube.common import dbfunc as db
from assetscube.common import processdb as dbquery
from assetscube.common import error_logics as errhand

@bp_nawg.route('/bullionprice', methods=["GET"])
def bullionprice():
    if request.method=="GET":
        s = 0
        f = []  # logs for tech guys
        t = None  # message to front end
        f1 = None
        con, cur, s1, f1 = db.mydbopncon()
        s, f, t = errhand.get_status(s, s1, f, f1, t, "no")
        s1, f1 = 0, None
        cur, s,  f1 = dbquery.get_bullion_price(con, cur)
        print(s)
        print(f1)
        if s <= 0:
            if s <= 0:
                f.append(f1)
                print('fetch is successful')
            else:
                f.append(f1)
                t = errhand.set_t(s)
                redata = [{"f": f, "t": t}]
                res = make_response(jsonify(redata), 200)
                return res
            f.append('warning 1 : testing')

        print('here 2 s,f,t', s, f, t)
        print(cur)
        db_rec = None
        if s <= 0:
            db_rec = cur.fetchall()[0][0]
            print(db_rec)
            # print(db_rec[0])

            if db_rec is None:
                print('do something over here')
                t = 'data couldnt be extracted from fetch results'
                redata = [{"t": t}]
                res = make_response(jsonify(redata), 200)
                return res

            else:
                # db_rec = db_rec[0]
                print("fetch results extracted")
                pass

        print(s, f, t)
        print(db_rec)

        if s <= 0:
            # redata = [{"uId": db_rec['userid'], "uName": db_rec['username']}]
            redata = db_rec
            res = make_response(jsonify(redata), 200)
            return res
        else:
            return jsonify(False)

        return 'flow'