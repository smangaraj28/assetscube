from . import bp_entitybranch
from flask import redirect, request, make_response, jsonify
from assetscube.common import dbfunc as db
from assetscube.common import error_logics as errhand
from assetscube.common import processdb


@bp_entitybranch.route('/entitybranch', methods=["GET", "POST", "PUT", "DELETE"])
def entity_branch():
    """ This method will handle GET, POST, UPDATE, DELETE request made from the frontend for an entity's branch.
        GET : It will return all the related entity's branches of a provided userid.
        POST : It will insert a new branch details in entitybranch table for an entity as well as it will
         assign that entity to the given useriid in useraccess table, if an entry exists for entitybranchid in
        useraccess table for tha same userid and it is't dummy then a new record will be inserted otherwise
        the entitybranchid field will be updated
    """
    if request.method == "GET":
        print("oentitybranch GET Call For Listing ALl Entitiy Branches Except 'PUBLIC' Entity ")

        # attempted_username = request.get_json(force=True)['username']
        # attempted_entityid = request.get_json(force=True)['entityid']
        attempted_username = 'df3a'
        attempted_entityid = 'EN1910201916'
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

        entitybranchstatus = 'A'
        getuserentitybranches = {}
        getuserentitybranches['keys'] = {}
        getuserentitybranches['keys']['userid'] = attempted_username
        getuserentitybranches['keys']['entityid'] = attempted_entityid
        getuserentitybranches['keys']['entitybranchstatus'] = entitybranchstatus

        if s <= 0:
            cur, s, f1 = processdb.get_user_entity_branches(con, cur, getuserentitybranches)
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
        print("entitybranch POST Call For Insert New Entity Branch")

        # attempted_username = request.get_json(force=True)['username']
        attempted_entityid = request.get_json(force=True)['entityid']
        attempted_entitybranchaddline1 = request.get_json(force=True)['entitybranchaddline1']
        attempted_entitybranchaddline2 = request.get_json(force=True)['entitybranchaddline2']
        attempted_entitybranchcategory = request.get_json(force=True)['entitybranchcategory']
        attempted_entitybranchcity = request.get_json(force=True)['entitybranchcity']
        attempted_entitybranchcountry = request.get_json(force=True)['entitybranchcountry']
        attempted_entitybranchdescription = request.get_json(force=True)['entitybranchdescription']
        attempted_entitybranchemail = request.get_json(force=True)['entitybranchemail']
        attempted_entitybranchfax = request.get_json(force=True)['entitybranchfax']
        attempted_entitybranchimageurl = request.get_json(force=True)['entitybranchimageurl']
        attempted_entitybranchmobile = request.get_json(force=True)['entitybranchmobile']
        attempted_entitybranchname = request.get_json(force=True)['entitybranchname']
        attempted_entitybranchphone = request.get_json(force=True)['entitybranchphone']
        attempted_entitybranchpincode = request.get_json(force=True)['entitybranchpincode']
        attempted_entitybranchshortname = request.get_json(force=True)['entitybranchshortname']
        attempted_entitybranchstartdate = request.get_json(force=True)['entitybranchstartdate']
        attempted_entitybranchstate = request.get_json(force=True)['entitybranchstate']
        attempted_entitybranchstatus = request.get_json(force=True)['entitybranchstatus']
        attempted_entitybranchwebsite = request.get_json(force=True)['entitybranchwebsite']
        attempted_userid = request.get_json(force=True)['userid']

        attempted_roleid = request.get_json(force=True)['roleid']
        attempted_logintype = request.get_json(force=True)['logintype']
        attempted_usertype = request.get_json(force=True)['usertype']
        print('userid', attempted_userid)
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

        insertentitybranch = {}
        insertentitybranch['values'] = {}
        insertentitybranch['values']['entityid'] = attempted_entityid
        insertentitybranch['values']['entitybranchaddline1'] = attempted_entitybranchaddline1
        insertentitybranch['values']['entitybranchaddline2'] = attempted_entitybranchaddline2
        insertentitybranch['values']['entitybranchcategory'] = attempted_entitybranchcategory
        insertentitybranch['values']['entitybranchcity'] = attempted_entitybranchcity
        insertentitybranch['values']['entitybranchcountry'] = attempted_entitybranchcountry
        insertentitybranch['values']['entitybranchdescription'] = attempted_entitybranchdescription
        insertentitybranch['values']['entitybranchemail'] = attempted_entitybranchemail
        insertentitybranch['values']['entitybranchfax'] = attempted_entitybranchfax
        insertentitybranch['values']['entitybranchimageurl'] = attempted_entitybranchimageurl
        insertentitybranch['values']['entitybranchmobile'] = attempted_entitybranchmobile
        insertentitybranch['values']['entitybranchname'] = attempted_entitybranchname
        insertentitybranch['values']['entitybranchphone'] = attempted_entitybranchphone
        insertentitybranch['values']['entitybranchpincode'] = attempted_entitybranchpincode
        insertentitybranch['values']['entitybranchshortname'] = attempted_entitybranchshortname
        insertentitybranch['values']['entitybranchstartdate'] = attempted_entitybranchstartdate
        insertentitybranch['values']['entitybranchstate'] = attempted_entitybranchstate
        insertentitybranch['values']['entitybranchstatus'] = attempted_entitybranchstatus
        insertentitybranch['values']['entitybranchwebsite'] = attempted_entitybranchwebsite
        insertentitybranch['values']['userid'] = attempted_userid

        if s <= 0:

            cur, s, f1 = processdb.insert_entity_branch(con, cur, insertentitybranch)

            if s <= 0:
                if s < 0:
                    f.append(f1)
                entitybranchid = cur.fetchone()[0]
                print('last entitybranch id =', entitybranchid)
                print('entitybranch database insert results:', s, f, t)

                getuserentitybranches = {}
                getuserentitybranches['keys'] = {}
                getuserentitybranches['keys']['userid'] = attempted_username
                getuserentitybranches['keys']['entityid'] = attempted_entityid
                getuserentitybranches['keys']['entitybranchstatus'] = 'A'

                if s <= 0:
                    cur, s, f1 = processdb.get_user_entity_branches(con, cur, getuserentitybranches)
                    if s <= 0:
                        if s < 0:
                            f.append(f1)
                        print('fetch is successful for entitybranch')
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
                    insertuseraccess['values']['entityid'] = attempted_entityid
                    insertuseraccess['values']['entitybranchid'] = entitybranchid
                    insertuseraccess['values']['defaultindicator'] = 'N'
                    insertuseraccess['values']['roleid'] = attempted_roleid
                    insertuseraccess['values']['entitywebsite'] = attempted_entitybranchwebsite
                    insertuseraccess['values']['accessstatus'] = 'A'

                    if db_rec is None:
                        print('do something over here')
                        insertuseraccess['action'] = 'update entitybranch'
                        cur, s, f1 = processdb.insert_update_useraccess(con, cur, insertuseraccess)
                        print('useraccess database insert results:', f, t)
                        if s <= 0:
                            if s < 0:
                                f.append(f1)
                            con.commit()
                            print('update is successful')
                            redata = [
                                {"userid": userid, "entityid": attempted_entityid, "entitybranchid": entitybranchid}]
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
                            redata = [
                                {"userid": userid, "entityid": attempted_entityid, "entitybranchid": entitybranchid}]
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
        print("entitybranch PUT Call For Modify Existing Entity Branch")

        attempted_username = request.get_json(force=True)['username']
        attempted_entityid = request.get_json(force=True)['entityid']
        attempted_entitybranchaddline1 = request.get_json(force=True)['entitybranchaddline1']
        attempted_entitybranchaddline2 = request.get_json(force=True)['entitybranchaddline2']
        attempted_entitybranchcategory = request.get_json(force=True)['entitybranchcategory']
        attempted_entitybranchcity = request.get_json(force=True)['entitybranchcity']
        attempted_entitybranchcountry = request.get_json(force=True)['entitybranchcountry']
        attempted_entitybranchdescription = request.get_json(force=True)['entitybranchdescription']
        attempted_entitybranchemail = request.get_json(force=True)['entitybranchemail']
        attempted_entitybranchfax = request.get_json(force=True)['entitybranchfax']
        attempted_entitybranchimageurl = request.get_json(force=True)['entitybranchimageurl']
        attempted_entitybranchmobile = request.get_json(force=True)['entitybranchmobile']
        attempted_entitybranchname = request.get_json(force=True)['entitybranchname']
        attempted_entitybranchphone = request.get_json(force=True)['entitybranchphone']
        attempted_entitybranchpincode = request.get_json(force=True)['entitybranchpincode']
        attempted_entitybranchshortname = request.get_json(force=True)['entitybranchshortname']
        attempted_entitybranchstartdate = request.get_json(force=True)['entitybranchstartdate']
        attempted_entitybranchstate = request.get_json(force=True)['entitybranchstate']
        attempted_entitybranchstatus = request.get_json(force=True)['entitybranchstatus']
        attempted_entitybranchwebsite = request.get_json(force=True)['entitybranchwebsite']
        attempted_userid = request.get_json(force=True)['userid']

        attempted_roleid = request.get_json(force=True)['roleid']
        attempted_logintype = request.get_json(force=True)['logintype']
        attempted_usertype = request.get_json(force=True)['usertype']
        print('userid',attempted_userid)
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

        modifyentitybranch = {}
        modifyentitybranch['values'] = {}
        modifyentitybranch['values']['entityid'] = attempted_entityid
        modifyentitybranch['values']['entitybranchaddline1'] = attempted_entitybranchaddline1
        modifyentitybranch['values']['entitybranchaddline2'] = attempted_entitybranchaddline2
        modifyentitybranch['values']['entitybranchcategory'] = attempted_entitybranchcategory
        modifyentitybranch['values']['entitybranchcity'] = attempted_entitybranchcity
        modifyentitybranch['values']['entitybranchcountry'] = attempted_entitybranchcountry
        modifyentitybranch['values']['entitybranchdescription'] = attempted_entitybranchdescription
        modifyentitybranch['values']['entitybranchemail'] = attempted_entitybranchemail
        modifyentitybranch['values']['entitybranchfax'] = attempted_entitybranchfax
        modifyentitybranch['values']['entitybranchimageurl'] = attempted_entitybranchimageurl
        modifyentitybranch['values']['entitybranchmobile'] = attempted_entitybranchmobile
        modifyentitybranch['values']['entitybranchname'] = attempted_entitybranchname
        modifyentitybranch['values']['entitybranchphone'] = attempted_entitybranchphone
        modifyentitybranch['values']['entitybranchpincode'] = attempted_entitybranchpincode
        modifyentitybranch['values']['entitybranchshortname'] = attempted_entitybranchshortname
        modifyentitybranch['values']['entitybranchstartdate'] = attempted_entitybranchstartdate
        modifyentitybranch['values']['entitybranchstate'] = attempted_entitybranchstate
        modifyentitybranch['values']['entitybranchstatus'] = attempted_entitybranchstatus
        modifyentitybranch['values']['entitybranchwebsite'] = attempted_entitybranchwebsite
        modifyentitybranch['values']['userid'] = attempted_userid

        if s <= 0:

            cur, s, f1 = processdb.modify_entity_branch(con, cur, modifyentitybranch)

            if s <= 0:
                if s < 0:
                    f.append(f1)
                entitybranchid = cur.fetchone()[0]
                print('last entitybranch id =', entitybranchid)
                print('entitybranch database insert results:', s, f, t)

                getuserentitybranches = {}
                getuserentitybranches['keys'] = {}
                getuserentitybranches['keys']['userid'] = attempted_username
                getuserentitybranches['keys']['entityid'] = attempted_entityid
                getuserentitybranches['keys']['entitybranchstatus'] = 'A'

                if s <= 0:
                    cur, s, f1 = processdb.get_user_entity_branches(con, cur, getuserentitybranches)
                    if s <= 0:
                        if s < 0:
                            f.append(f1)
                        print('fetch is successful for entitybranch')
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
                    insertuseraccess['values']['entityid'] = attempted_entityid
                    insertuseraccess['values']['entitybranchid'] = entitybranchid
                    insertuseraccess['values']['defaultindicator'] = 'N'
                    insertuseraccess['values']['roleid'] = attempted_roleid
                    insertuseraccess['values']['entitywebsite'] = attempted_entitybranchwebsite
                    insertuseraccess['values']['accessstatus'] = 'A'

                    if db_rec is None:
                        print('do something over here')
                        insertuseraccess['action'] = 'update entitybranch'
                        cur, s, f1 = processdb.insert_update_useraccess(con, cur, insertuseraccess)
                        print('useraccess database insert results:', f, t)
                        if s <= 0:
                            if s < 0:
                                f.append(f1)
                            con.commit()
                            print('update is successful')
                            redata = [
                                {"userid": userid, "entityid": attempted_entityid, "entitybranchid": entitybranchid}]
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
                            redata = [
                                {"userid": userid, "entityid": attempted_entityid, "entitybranchid": entitybranchid}]
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
        print("oentitybranch DELETE Call For Deleting Existing EntityBranch")
        attempted_entityId = request.args.get('entityid')
        attempted_entityBranchId = request.args.get('entitybranchid')
        print(attempted_entityId)
        print(attempted_entityBranchId)

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

        if s <= 0:
            cur, s, f1 = processdb.delete_entity_branch(con, cur, attempted_userid, attempted_entityId,
                                                        attempted_entityBranchId)
            if s <= 0:
                if s < 0:
                    f.append(f1)
                entitybranchid = cur.fetchone()[0]
                print('last entitybranch id =', entitybranchid)
                print('entitybranch database insert results:', s, f, t)

                getuserentitybranches = {}
                getuserentitybranches['keys'] = {}
                getuserentitybranches['keys']['userid'] = attempted_username
                getuserentitybranches['keys']['entityid'] = attempted_entityid
                getuserentitybranches['keys']['entitybranchstatus'] = 'A'

                if s <= 0:
                    cur, s, f1 = processdb.get_user_entity_branches(con, cur, getuserentitybranches)
                    if s <= 0:
                        if s < 0:
                            f.append(f1)
                        print('fetch is successful for entitybranch')
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
                    insertuseraccess['values']['entityid'] = attempted_entityid
                    insertuseraccess['values']['entitybranchid'] = entitybranchid
                    insertuseraccess['values']['defaultindicator'] = 'N'
                    insertuseraccess['values']['roleid'] = attempted_roleid
                    insertuseraccess['values']['entitywebsite'] = attempted_entitybranchwebsite
                    insertuseraccess['values']['accessstatus'] = 'A'

                    if db_rec is None:
                        print('do something over here')
                        insertuseraccess['action'] = 'update entitybranch'
                        cur, s, f1 = processdb.insert_update_useraccess(con, cur, insertuseraccess)
                        print('useraccess database insert results:', f, t)
                        if s <= 0:
                            if s < 0:
                                f.append(f1)
                            con.commit()
                            print('update is successful')
                            redata = [
                                {"userid": userid, "entityid": attempted_entityid, "entitybranchid": entitybranchid}]
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
                            redata = [
                                {"userid": userid, "entityid": attempted_entityid, "entitybranchid": entitybranchid}]
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
