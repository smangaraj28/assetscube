from . import bp_entity
from flask import redirect, request, make_response, jsonify
from assetscube.common import dbfunc as db
from assetscube.common import error_logics as errhand
from assetscube.common import processdb
from assetscube.common import jwtfuncs as jwtf


@bp_entity.route('/entity', methods=["GET", "POST", "PUT", "DELETE"])
def entity():
    """ This method will handle GET, POST, UPDATE, DELETE request made from the frontend for an entity.
        GET : It will return all the related entities of a provided userid.
        POST : It will insert a new entity details in entity table as well as it will assign that entity to
        the given useriid in useraccess table, if an entry exists for entityid in
        useraccess table for tha same userid and it is't dummy then a new record will be inserted otherwise
        the entityid field will be updated
    """
    if request.method == "GET":
        print("oentity GET Call For Listing ALl Entities Except 'PUBLIC' Entity ")
        print(request.headers.get("thirdparty", None))
        print(request.headers.get("usertype", None))
        abc = dict(request.headers)
        print(abc)
        dtkn = jwtf.decodetoken(request, needtkn=False)
        userid = dtkn.get("user_id", None)
        entityid = request.headers.get("entityid", None)
        cntryid = request.headers.get("countryid", None)
        print(userid)
        print(entityid)
        print(cntryid)
        # attempted_username = request.get_json(force=True)['username']
        attempted_username = userid
        s = 0
        f = []  # logs for tech guys
        t = None  # message to front end
        f1 = None
        # attempted_username = 'natrayan'
        # attempted_password = 'natrayan'
        branchid = "test"
        hotelid = "test"
        print(attempted_username)
        print("here")
        # if s <= 0:
        #     con, cur, s1, f1 = db.mydbopncon()
        #     s, f, t = errhand.get_status(s, s1, f, f1, t, "no")
        #     s1, f1 = 0, None
        #     print("DB connection established", s, f, t)

        if s <= 0:
            con, cur, s, f1 = db.mydbopncon()
            if s <= 0:
                if s < 0:
                    f.append(f1)
                print("DB connection established", s, f, t)
            else:
                print("DB connection not established", s, f, t)
                f.append(f1)
                t = errhand.set_t(s)
                redata = [{"f": f, "t": t}]
                res = make_response(jsonify(redata), 200)
                return res
            f.append('warning 1 : testing')

        entitystatus = 'A'
        getuserentities = {}
        getuserentities['keys'] = {}
        getuserentities['keys']['userid'] = attempted_username
        getuserentities['keys']['entitystatus'] = entitystatus

        if s <= 0:
            cur, s, f1 = processdb.get_user_entities(con, cur, getuserentities)
            if s <= 0:
                if s < 0:
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
    elif request.method == "POST":
        print("oentity POST Call For Insert New Entity")

        attempted_username = request.get_json(force=True)['username']
        attempted_entityaddline1 = request.get_json(force=True)['entityaddline1']
        attempted_entityaddline2 = request.get_json(force=True)['entityaddline2']
        attempted_entitycategory = request.get_json(force=True)['entitycategory']
        attempted_entitycity = request.get_json(force=True)['entitycity']
        attempted_entitycountry = request.get_json(force=True)['entitycountry']
        attempted_entitydescription = request.get_json(force=True)['entitydescription']
        attempted_entityemail = request.get_json(force=True)['entityemail']
        attempted_entityfax = request.get_json(force=True)['entityfax']
        attempted_entityfiscalyear = request.get_json(force=True)['entityfiscalyear']
        attempted_entityimageurl = request.get_json(force=True)['entityimageurl']
        attempted_entityindustry = request.get_json(force=True)['entityindustry']
        attempted_entitylogo = request.get_json(force=True)['entitylogo']
        attempted_entitymobile = request.get_json(force=True)['entitymobile']
        attempted_entityname = request.get_json(force=True)['entityname']
        attempted_entityphone = request.get_json(force=True)['entityphone']
        attempted_entitypincode = request.get_json(force=True)['entitypincode']
        attempted_entityshortname = request.get_json(force=True)['entityshortname']
        attempted_entitystartdate = request.get_json(force=True)['entitystartdate']
        attempted_entitystate = request.get_json(force=True)['entitystate']
        attempted_entitystatus = request.get_json(force=True)['entitystatus']
        attempted_entitytaxid = request.get_json(force=True)['entitytaxid']
        attempted_entitytimezone = request.get_json(force=True)['entitytimezone']
        attempted_entitywebsite = request.get_json(force=True)['entitywebsite']
        attempted_muserid = request.get_json(force=True)['muserid']

        attempted_roleid = request.get_json(force=True)['roleid']
        attempted_logintype = request.get_json(force=True)['logintype']
        attempted_usertype = request.get_json(force=True)['usertype']

        s = 0
        f = []  # logs for tech guys
        t = None  # message to front end
        f1 = None
        # attempted_username = 'natrayan'
        # attempted_password = 'natrayan'
        branchid = "test"
        hotelid = "test"
        print(attempted_username)
        print("here")
        # if s <= 0:
        #     con, cur, s1, f1 = db.mydbopncon()
        #     s, f, t = errhand.get_status(s, s1, f, f1, t, "no")
        #     s1, f1 = 0, None
        #     print("DB connection established", s, f, t)

        if s <= 0:
            con, cur, s, f1 = db.mydbopncon()
            if s <= 0:
                if s < 0:
                    f.append(f1)
                print("DB connection established", s, f, t)
            else:
                print("DB connection not established", s, f, t)
                f.append(f1)
                t = errhand.set_t(s)
                redata = [{"f": f, "t": t}]
                res = make_response(jsonify(redata), 200)
                return res
            f.append('warning 1 : testing')

        userid = attempted_username
        name = 'mangu'
        signupemail = 'mangu@gmail.com'
        userstatus = 'A'
        entityid = 'bansss'
        countryid = '473874'

        insertentity = {}
        insertentity['values'] = {}
        insertentity['values']['entityaddline1'] = attempted_entityaddline1
        insertentity['values']['entityaddline2'] = attempted_entityaddline2
        insertentity['values']['entitycategory'] = attempted_entitycategory
        insertentity['values']['entitycity'] = attempted_entitycity
        insertentity['values']['entitycountry'] = attempted_entitycountry
        insertentity['values']['entitydescription'] = attempted_entitydescription
        insertentity['values']['entityemail'] = attempted_entityemail
        insertentity['values']['entityfax'] = attempted_entityfax
        insertentity['values']['entityfiscalyear'] = attempted_entityfiscalyear
        insertentity['values']['entityimageurl'] = attempted_entityimageurl
        insertentity['values']['entityindustry'] = attempted_entityindustry
        insertentity['values']['entitylogo'] = attempted_entitylogo
        insertentity['values']['entitymobile'] = attempted_entitymobile
        insertentity['values']['entityname'] = attempted_entityname
        insertentity['values']['entityphone'] = attempted_entityphone
        insertentity['values']['entitypincode'] = attempted_entitypincode
        insertentity['values']['entityshortname'] = attempted_entityshortname
        insertentity['values']['entitystartdate'] = attempted_entitystartdate
        insertentity['values']['entitystate'] = attempted_entitystate
        insertentity['values']['entitystatus'] = attempted_entitystatus
        insertentity['values']['entitytaxid'] = attempted_entitytaxid
        insertentity['values']['entitytimezone'] = attempted_entitytimezone
        insertentity['values']['entitywebsite'] = attempted_entitywebsite
        insertentity['values']['userid'] = attempted_muserid
        if s <= 0:

            cur, s, f1 = processdb.insert_entity(con, cur, insertentity)

            if s <= 0:
                if s < 0:
                    f.append(f1)
                entityid = cur.fetchone()[0]
                print('last entity id =', entityid)
                print('entity database insert results:', s, f, t)

                getuserentities = {}
                getuserentities['keys'] = {}
                getuserentities['keys']['userid'] = attempted_username
                getuserentities['keys']['entitystatus'] = 'A'

                if s <= 0:
                    cur, s, f1 = processdb.get_user_entities(con, cur, getuserentities)
                    if s <= 0:
                        if s < 0:
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
                    insertuseraccess = dict()
                    insertuseraccess['values'] = dict()
                    insertuseraccess['values']['userid'] = attempted_username
                    insertuseraccess['values']['logintype'] = attempted_logintype
                    insertuseraccess['values']['usertype'] = attempted_usertype
                    insertuseraccess['values']['entityid'] = entityid
                    insertuseraccess['values']['entitybranchid'] = 'dummy'
                    insertuseraccess['values']['defaultindicator'] = 'N'
                    insertuseraccess['values']['roleid'] = attempted_roleid
                    insertuseraccess['values']['entitywebsite'] = attempted_entitywebsite
                    insertuseraccess['values']['accessstatus'] = 'A'

                    if db_rec is None:
                        print('do something over here')
                        insertuseraccess['action'] = 'update entity'
                        cur, s, f1 = processdb.insert_update_useraccess(con, cur, insertuseraccess)
                        print('useraccess database insert results:', f, t)
                        if s <= 0:
                            if s < 0:
                                f.append(f1)
                            con.commit()
                            print('update is successful')
                            redata = [{"userid": userid, "entityid": entityid}]
                            res = make_response(jsonify(redata), 200)
                            return res
                        else:
                            f.append(f1)
                            t = errhand.set_t(s)
                            redata = [{"f": f, "t": t}]
                            res = make_response(jsonify(redata), 200)
                            return res
                    else:
                        print("fetch results extracted")
                        insertuseraccess['action'] = 'insert'
                        cur, s, f1 = processdb.insert_update_useraccess(con, cur, insertuseraccess)
                        print('useraccess database insert results:', f, t)
                        if s <= 0:
                            if s < 0:
                                f.append(f1)
                            con.commit()
                            print('Insert is successful')
                            redata = [{"userid": userid, "entityid": entityid}]
                            res = make_response(jsonify(redata), 200)
                            return res
                        else:
                            f.append(f1)
                            t = errhand.set_t(s)
                            redata = [{"f": f, "t": t}]
                            res = make_response(jsonify(redata), 200)
                            return res
                else:
                    f.append(f1)
                    t = errhand.set_t(s)
                    redata = [{"f": f, "t": t}]
                    res = make_response(jsonify(redata), 200)
                    return res
            else:
                f.append(f1)
                t = errhand.set_t(s)
                redata = [{"f": f, "t": t}]
                res = make_response(jsonify(redata), 200)
                return res
            f.append('warning 1 : testing')

        print('here 2 s,f,t', s, f, t)
        print(cur)
    elif request.method == "PUT":
        print("oentity PUT Call For Modify Existing Entity")

        attempted_username = request.get_json(force=True)['username']
        attempted_entityaddline1 = request.get_json(force=True)['entityaddline1']
        attempted_entityaddline2 = request.get_json(force=True)['entityaddline2']
        attempted_entitycategory = request.get_json(force=True)['entitycategory']
        attempted_entitycity = request.get_json(force=True)['entitycity']
        attempted_entitycountry = request.get_json(force=True)['entitycountry']
        attempted_entitydescription = request.get_json(force=True)['entitydescription']
        attempted_entityemail = request.get_json(force=True)['entityemail']
        attempted_entityfax = request.get_json(force=True)['entityfax']
        attempted_entityfiscalyear = request.get_json(force=True)['entityfiscalyear']
        attempted_entityimageurl = request.get_json(force=True)['entityimageurl']
        attempted_entityindustry = request.get_json(force=True)['entityindustry']
        attempted_entitylogo = request.get_json(force=True)['entitylogo']
        attempted_entitymobile = request.get_json(force=True)['entitymobile']
        attempted_entityname = request.get_json(force=True)['entityname']
        attempted_entityphone = request.get_json(force=True)['entityphone']
        attempted_entitypincode = request.get_json(force=True)['entitypincode']
        attempted_entityshortname = request.get_json(force=True)['entityshortname']
        attempted_entitystartdate = request.get_json(force=True)['entitystartdate']
        attempted_entitystate = request.get_json(force=True)['entitystate']
        attempted_entitystatus = request.get_json(force=True)['entitystatus']
        attempted_entitytaxid = request.get_json(force=True)['entitytaxid']
        attempted_entitytimezone = request.get_json(force=True)['entitytimezone']
        attempted_entitywebsite = request.get_json(force=True)['entitywebsite']
        attempted_muserid = request.get_json(force=True)['muserid']

        attempted_roleid = request.get_json(force=True)['roleid']
        attempted_logintype = request.get_json(force=True)['logintype']
        attempted_usertype = request.get_json(force=True)['usertype']

        s = 0
        f = []  # logs for tech guys
        t = None  # message to front end
        f1 = None
        # attempted_username = 'natrayan'
        # attempted_password = 'natrayan'
        branchid = "test"
        hotelid = "test"
        print(attempted_username)
        print("here")
        # if s <= 0:
        #     con, cur, s1, f1 = db.mydbopncon()
        #     s, f, t = errhand.get_status(s, s1, f, f1, t, "no")
        #     s1, f1 = 0, None
        #     print("DB connection established", s, f, t)

        if s <= 0:
            con, cur, s, f1 = db.mydbopncon()
            if s <= 0:
                if s < 0:
                    f.append(f1)
                print("DB connection established", s, f, t)
            else:
                print("DB connection not established", s, f, t)
                f.append(f1)
                t = errhand.set_t(s)
                redata = [{"f": f, "t": t}]
                res = make_response(jsonify(redata), 200)
                return res
            f.append('warning 1 : testing')

        userid = attempted_username
        name = 'mangu'
        signupemail = 'mangu@gmail.com'
        userstatus = 'A'
        entityid = 'bansss'
        countryid = '473874'

        modifyentity = {}
        modifyentity['values'] = {}
        modifyentity['values']['entityaddline1'] = attempted_entityaddline1
        modifyentity['values']['entityaddline2'] = attempted_entityaddline2
        modifyentity['values']['entitycategory'] = attempted_entitycategory
        modifyentity['values']['entitycity'] = attempted_entitycity
        modifyentity['values']['entitycountry'] = attempted_entitycountry
        modifyentity['values']['entitydescription'] = attempted_entitydescription
        modifyentity['values']['entityemail'] = attempted_entityemail
        modifyentity['values']['entityfax'] = attempted_entityfax
        modifyentity['values']['entityfiscalyear'] = attempted_entityfiscalyear
        modifyentity['values']['entityimageurl'] = attempted_entityimageurl
        modifyentity['values']['entityindustry'] = attempted_entityindustry
        modifyentity['values']['entitylogo'] = attempted_entitylogo
        modifyentity['values']['entitymobile'] = attempted_entitymobile
        modifyentity['values']['entityname'] = attempted_entityname
        modifyentity['values']['entityphone'] = attempted_entityphone
        modifyentity['values']['entitypincode'] = attempted_entitypincode
        modifyentity['values']['entityshortname'] = attempted_entityshortname
        modifyentity['values']['entitystartdate'] = attempted_entitystartdate
        modifyentity['values']['entitystate'] = attempted_entitystate
        modifyentity['values']['entitystatus'] = attempted_entitystatus
        modifyentity['values']['entitytaxid'] = attempted_entitytaxid
        modifyentity['values']['entitytimezone'] = attempted_entitytimezone
        modifyentity['values']['entitywebsite'] = attempted_entitywebsite
        modifyentity['values']['muserid'] = attempted_muserid
        if s <= 0:

            cur, s, f1 = processdb.modify_entity(con, cur, modifyentity)

            if s <= 0:
                if s < 0:
                    f.append(f1)
                entityid = cur.fetchone()[0]
                print('last entity id =', entityid)
                print('entity database modify results:', s, f, t)

                getuserentities = {}
                getuserentities['keys'] = {}
                getuserentities['keys']['userid'] = attempted_username
                getuserentities['keys']['entitystatus'] = 'A'

                if s <= 0:
                    cur, s, f1 = processdb.get_user_entities(con, cur, getuserentities)
                    if s <= 0:
                        if s < 0:
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
                    insertuseraccess = dict()
                    insertuseraccess['values'] = dict()
                    insertuseraccess['values']['userid'] = attempted_username
                    insertuseraccess['values']['logintype'] = attempted_logintype
                    insertuseraccess['values']['usertype'] = attempted_usertype
                    insertuseraccess['values']['entityid'] = entityid
                    insertuseraccess['values']['entitybranchid'] = 'dummy'
                    insertuseraccess['values']['defaultindicator'] = 'N'
                    insertuseraccess['values']['roleid'] = attempted_roleid
                    insertuseraccess['values']['entitywebsite'] = attempted_entitywebsite
                    insertuseraccess['values']['accessstatus'] = 'A'

                    if db_rec is None:
                        print('do something over here')
                        insertuseraccess['action'] = 'update entity'
                        cur, s, f1 = processdb.insert_update_useraccess(con, cur, insertuseraccess)
                        print('useraccess database insert results:', f, t)
                        if s <= 0:
                            if s < 0:
                                f.append(f1)
                            con.commit()
                            print('update is successful')
                            redata = [{"userid": userid, "entityid": entityid}]
                            res = make_response(jsonify(redata), 200)
                            return res
                        else:
                            f.append(f1)
                            t = errhand.set_t(s)
                            redata = [{"f": f, "t": t}]
                            res = make_response(jsonify(redata), 200)
                            return res
                    else:
                        print("fetch results extracted")
                        insertuseraccess['action'] = 'insert'
                        cur, s, f1 = processdb.insert_update_useraccess(con, cur, insertuseraccess)
                        print('useraccess database insert results:', f, t)
                        if s <= 0:
                            if s < 0:
                                f.append(f1)
                            con.commit()
                            print('Insert is successful')
                            redata = [{"userid": userid, "entityid": entityid}]
                            res = make_response(jsonify(redata), 200)
                            return res
                        else:
                            f.append(f1)
                            t = errhand.set_t(s)
                            redata = [{"f": f, "t": t}]
                            res = make_response(jsonify(redata), 200)
                            return res
                else:
                    f.append(f1)
                    t = errhand.set_t(s)
                    redata = [{"f": f, "t": t}]
                    res = make_response(jsonify(redata), 200)
                    return res
            else:
                f.append(f1)
                t = errhand.set_t(s)
                redata = [{"f": f, "t": t}]
                res = make_response(jsonify(redata), 200)
                return res
            f.append('warning 1 : testing')

        print('here 2 s,f,t', s, f, t)
        print(cur)
    elif request.method == "DELETE":
        print("oentity DELETE Call For Deleting Existing Entity")
        attempted_entityId = request.args.get('entityid')
        print(attempted_entityId)
        s = 0
        f = []  # logs for tech guys
        t = None  # message to front end
        f1 = None
        # attempted_username = 'natrayan'
        # attempted_password = 'natrayan'
        branchid = "test"
        hotelid = "test"
        print(attempted_username)
        print("here")
        # if s <= 0:
        #     con, cur, s1, f1 = db.mydbopncon()
        #     s, f, t = errhand.get_status(s, s1, f, f1, t, "no")
        #     s1, f1 = 0, None
        #     print("DB connection established", s, f, t)

        if s <= 0:
            con, cur, s, f1 = db.mydbopncon()
            if s <= 0:
                if s < 0:
                    f.append(f1)
                print("DB connection established", s, f, t)
            else:
                print("DB connection not established", s, f, t)
                f.append(f1)
                t = errhand.set_t(s)
                redata = [{"f": f, "t": t}]
                res = make_response(jsonify(redata), 200)
                return res
            f.append('warning 1 : testing')

        userid = attempted_username
        name = 'mangu'
        signupemail = 'mangu@gmail.com'
        userstatus = 'A'
        # entityid = 'bansss'
        countryid = '473874'
        if s <= 0:
            cur, s, f1 = processdb.delete_entity(con, cur, attempted_userid, attempted_entityId)
            if s <= 0:
                if s < 0:
                    f.append(f1)
                entityid = cur.fetchone()[0]
                print('last entity id =', entityid)
                print('entity database modify results:', s, f, t)

                getuserentities = {}
                getuserentities['keys'] = {}
                getuserentities['keys']['userid'] = attempted_username
                getuserentities['keys']['entitystatus'] = 'A'

                if s <= 0:
                    cur, s, f1 = processdb.get_user_entities(con, cur, getuserentities)
                    if s <= 0:
                        if s < 0:
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
                    insertuseraccess = dict()
                    insertuseraccess['values'] = dict()
                    insertuseraccess['values']['userid'] = attempted_username
                    insertuseraccess['values']['logintype'] = attempted_logintype
                    insertuseraccess['values']['usertype'] = attempted_usertype
                    insertuseraccess['values']['entityid'] = entityid
                    insertuseraccess['values']['entitybranchid'] = 'dummy'
                    insertuseraccess['values']['defaultindicator'] = 'N'
                    insertuseraccess['values']['roleid'] = attempted_roleid
                    insertuseraccess['values']['entitywebsite'] = attempted_entitywebsite
                    insertuseraccess['values']['accessstatus'] = 'A'

                    if db_rec is None:
                        print('do something over here')
                        insertuseraccess['action'] = 'update entity'
                        cur, s, f1 = processdb.insert_update_useraccess(con, cur, insertuseraccess)
                        print('useraccess database insert results:', f, t)
                        if s <= 0:
                            if s < 0:
                                f.append(f1)
                            con.commit()
                            print('update is successful')
                            redata = [{"userid": userid, "entityid": entityid}]
                            res = make_response(jsonify(redata), 200)
                            return res
                        else:
                            f.append(f1)
                            t = errhand.set_t(s)
                            redata = [{"f": f, "t": t}]
                            res = make_response(jsonify(redata), 200)
                            return res
                    else:
                        print("fetch results extracted")
                        insertuseraccess['action'] = 'insert'
                        cur, s, f1 = processdb.insert_update_useraccess(con, cur, insertuseraccess)
                        print('useraccess database insert results:', f, t)
                        if s <= 0:
                            if s < 0:
                                f.append(f1)
                            con.commit()
                            print('Insert is successful')
                            redata = [{"userid": userid, "entityid": entityid}]
                            res = make_response(jsonify(redata), 200)
                            return res
                        else:
                            f.append(f1)
                            t = errhand.set_t(s)
                            redata = [{"f": f, "t": t}]
                            res = make_response(jsonify(redata), 200)
                            return res
                else:
                    f.append(f1)
                    t = errhand.set_t(s)
                    redata = [{"f": f, "t": t}]
                    res = make_response(jsonify(redata), 200)
                    return res
            else:
                f.append(f1)
                t = errhand.set_t(s)
                redata = [{"f": f, "t": t}]
                res = make_response(jsonify(redata), 200)
                return res
            f.append('warning 1 : testing')

        print('here 2 s,f,t', s, f, t)
        print(cur)
