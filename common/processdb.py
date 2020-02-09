from assetscube.common import dbfunc as db
from assetscube.common import error_logics as errhand


def get_user_entities(con, cur, getuserentities):
    command = cur.mogrify("""
                                                    SELECT json_agg(a) FROM (
                                                    SELECT entityid AS "entityId", entityname AS "entityName",
                                                    entityshortname AS "entityShortName", entitycategory AS "entityCategory",
                                                    entitystatus AS "entityStatus", entitydescription AS "entityDescription",
                                                    entityimageurl AS "entityImageUrl", entitylogo AS "entityLogo",
                                                    entityindustry AS "entityIndustry", entitytaxid AS "entityTaxID",
                                                    entityaddline1 AS "entityAddLine1", entityaddline2 AS "entityAddLine2",
                                                    entitycity AS "entityCity", entitystate AS "entityState", 
                                                    entitycountry AS "entityCountry", entitypincode AS "entityPinCode",
                                                    entityphone AS "entityPhone", entityfax AS "entityFax",
                                                    entitymobile AS "entityMobile", entitywebsite AS "entityWebsite",
                                                    entityemail AS "entityEmail", entitystartdate AS "entityStartDate",
                                                    entityfiscalyear AS "entityFiscalYear", entitytimezone AS "entityTimeZone",
                                                    octime AS "octTime", lmtime AS "lmtTime", userid AS "userId"
                                                    FROM unihot.entity
                                                    WHERE entityid in
                                                            (select entityid from unihot.useraccess
                                                             where userid = %s)
                                                          and entitystatus = %s
                                                    ) as a
                                                """, (getuserentities['keys']['userid'],
                                                      getuserentities['keys']['entitystatus'],))
    print(command)
    cur, s, f1 = db.mydbfunc(con, cur, command)
    return cur, s, f1


def insert_entity(con, cur, insertentitybranch):
    command = cur.mogrify("""
                                    INSERT INTO unihot.entity    (
                                     entityaddline1,
                                     entityaddline2,
                                     entitycategory,
                                     entitycity,
                                     entitycountry,
                                     entitydescription,
                                     entityemail,
                                     entityfax,
                                     entityfiscalyear,
                                     entityimageurl,
                                     entityindustry,
                                     entitylogo,
                                     entitymobile,
                                     entityname,
                                     entityphone,
                                     entitypincode,
                                     entityshortname,
                                     entitystartdate,
                                     entitystate,
                                     entitystatus,
                                     entitytaxid,
                                     entitytimezone,
                                     entitywebsite,
                                     lmtime,
                                     octime,
                                     userid
                                    )
                                    VALUES (%s,%s,%s,
                                            %s,%s,%s,
                                            %s,%s,%s,
                                            %s,%s,%s,
                                            %s,%s,%s,
                                            %s,%s,%s,
                                            %s,%s,%s,
                                            %s,%s,
                                            CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,%s
                                            ) RETURNING entityid;
                                    """,
                          (insertentitybranch['values']['entityaddline1'],
                           insertentitybranch['values']['entityaddline2'],
                           insertentitybranch['values']['entitycategory'],
                           insertentitybranch['values']['entitycity'],
                           insertentitybranch['values']['entitycountry'],
                           insertentitybranch['values']['entitydescription'],
                           insertentitybranch['values']['entityemail'],
                           insertentitybranch['values']['entityfax'],
                           insertentitybranch['values']['entityfiscalyear'],
                           insertentitybranch['values']['entityimageurl'],
                           insertentitybranch['values']['entityindustry'],
                           insertentitybranch['values']['entitylogo'],
                           insertentitybranch['values']['entitymobile'],
                           insertentitybranch['values']['entityname'],
                           insertentitybranch['values']['entityphone'],
                           insertentitybranch['values']['entitypincode'],
                           insertentitybranch['values']['entityshortname'],
                           insertentitybranch['values']['entitystartdate'],
                           insertentitybranch['values']['entitystate'],
                           insertentitybranch['values']['entitystatus'],
                           insertentitybranch['values']['entitytaxid'],
                           insertentitybranch['values']['entitytimezone'],
                           insertentitybranch['values']['entitywebsite'],
                           insertentitybranch['values']['userid']
                           ))

    print(command)
    cur, s, f1 = db.mydbfunc(con, cur, command)
    return cur, s, f1


def modify_entity(con, cur, modifyentitybranch):
    command = cur.mogrify("""
                                        UPDATE unihot.entity    
                                        SET 
                                         entityaddline1 = %s,
                                         entityaddline2 = %s,
                                         entitycategory = %s,
                                         entitycity = %s,
                                         entitycountry = %s,
                                         entitydescription = %s,
                                         entityemail = %s,
                                         entityfax = %s,
                                         entityfiscalyear = %s,
                                         entityimageurl = %s,
                                         entityindustry = %s,
                                         entitylogo = %s,
                                         entitymobile = %s,
                                         entityname = %s,
                                         entityphone = %s,
                                         entitypincode = %s,
                                         entityshortname = %s,
                                         entitystartdate = %s,
                                         entitystate = %s,
                                         entitystatus = %s,
                                         entitytaxid = %s,
                                         entitytimezone = %s,
                                         entitywebsite = %s,
                                         lmtime = CURRENT_TIMESTAMP,
                                         octime = %s,
                                         userid = %s
                                         WHERE entityid = %s
                                         RETURNING entityid;
                                        """,
                          (modifyentitybranch['values']['entityaddline1'],
                           modifyentitybranch['values']['entityaddline2'],
                           modifyentitybranch['values']['entitycategory'],
                           modifyentitybranch['values']['entitycity'],
                           modifyentitybranch['values']['entitycountry'],
                           modifyentitybranch['values']['entitydescription'],
                           modifyentitybranch['values']['entityemail'],
                           modifyentitybranch['values']['entityfax'],
                           modifyentitybranch['values']['entityfiscalyear'],
                           modifyentitybranch['values']['entityimageurl'],
                           modifyentitybranch['values']['entityindustry'],
                           modifyentitybranch['values']['entitylogo'],
                           modifyentitybranch['values']['entitymobile'],
                           modifyentitybranch['values']['entityname'],
                           modifyentitybranch['values']['entityphone'],
                           modifyentitybranch['values']['entitypincode'],
                           modifyentitybranch['values']['entityshortname'],
                           modifyentitybranch['values']['entitystartdate'],
                           modifyentitybranch['values']['entitystate'],
                           modifyentitybranch['values']['entitystatus'],
                           modifyentitybranch['values']['entitytaxid'],
                           modifyentitybranch['values']['entitytimezone'],
                           modifyentitybranch['values']['entitywebsite'],
                           modifyentitybranch['values']['octime'],
                           modifyentitybranch['values']['userid'],
                           modifyentitybranch['values']['entityid']
                           ))

    print(command)
    cur, s, f1 = db.mydbfunc(con, cur, command)
    return cur, s, f1


def delete_entity(con, cur, userid, entityid):
    print(entityid)
    command = cur.mogrify("""
                                        UPDATE unihot.entity    
                                        SET 
                                         entitystatus = %s,
                                         lmtime = CURRENT_TIMESTAMP,
                                         userid = %s
                                         WHERE entityid = %s
                                         RETURNING entityid;
                                        """,
                          ('D',
                           userid,
                           entityid
                           ))
    print(command)
    cur, s, f1 = db.mydbfunc(con, cur, command)
    return cur, s, f1


def insert_update_useraccess(con, cur, insertuseraccess):
    if insertuseraccess['action'] == 'insert':
        command = cur.mogrify("""
                                INSERT INTO unihot.useraccess (userid, logintype, usertype,
                                                                entityid, entitybranchid, defaultindicator,
                                                                 roleid, site, accessstatus,
                                                                  octime, lmtime)
                                VALUES (%s,%s,%s,
                                        %s,%s,%s,
                                         %s, %s, %s,
                                          CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
                                """, (
            insertuseraccess['values']['userid'],
            insertuseraccess['values']['logintype'],
            insertuseraccess['values']['usertype'],
            insertuseraccess['values']['entityid'],
            insertuseraccess['values']['entitybranchid'],
            insertuseraccess['values']['defaultindicator'],
            insertuseraccess['values']['roleid'],
            insertuseraccess['values']['entitywebsite'],
            insertuseraccess['values']['accessstatus'],))
        print(command)
        cur, s, f1 = db.mydbfunc(con, cur, command)
        return cur, s, f1
    elif insertuseraccess['action'] == 'update entity':
        command = cur.mogrify("""
                                UPDATE unihot.useraccess 
                                SET entityid = %s,
                                lmtime= CURRENT_TIMESTAMP
                                WHERE userid = %s
                                and   entityid = 'dummy'
                              """, (
            insertuseraccess['values']['entityid'],
            insertuseraccess['values']['userid'],
        ))
        print(command)
        cur, s, f1 = db.mydbfunc(con, cur, command)
        return cur, s, f1
    elif insertuseraccess['action'] == 'update entitybranch':
        command = cur.mogrify("""
                                UPDATE unihot.useraccess 
                                SET entitybranchid = %s,
                                lmtime= CURRENT_TIMESTAMP
                                WHERE userid = %s
                                and   entityid = %s
                                and   entitybranchid = 'dummy'
                              """, (
            insertuseraccess['values']['entitybranchid'],
            insertuseraccess['values']['userid'],
            insertuseraccess['values']['entityid']
        ))
        print(command)
        cur, s, f1 = db.mydbfunc(con, cur, command)
        return cur, s, f1
    else:
        return cur, 200, 'Action not defined for useraccess'


""" Methods related to entitybranch """


def get_user_entity_branches(con, cur, getuserentitybranches):
    command = cur.mogrify("""
                                                    SELECT json_agg(a) FROM (
                                                    SELECT entityid AS "entityName", entitybranchid AS "entityBranchId",
                                                    entitybranchname AS "entityBranchName", entitybranchshortname AS "entityBranchShortName",
                                                    entitybranchcategory AS "entityBranchCategory", entitybranchstatus AS "entityBranchStatus",
                                                    entitybranchdescription AS "entityBranchDescription", entitybranchimageurl AS "entityBranchImageUrl",
                                                    entitybranchaddline1 AS "entityBranchAddLine1", entitybranchaddline2 AS "entityBranchAddLine2",
                                                    entitybranchcity AS "entityBranchCity", entitybranchstate AS "entityBranchState",
                                                    entitybranchcountry AS "entityBranchCountry", entitybranchpincode AS "entityBranchPinCode",
                                                    entitybranchphone AS "entityBranchPhone", entitybranchfax AS "entityBranchFax",
                                                    entitybranchmobile AS "entityBranchMobile", entitybranchwebsite AS "entityBranchWebsite",
                                                    entitybranchemail AS "entityBranchEmail", entitybranchstartdate AS "entityBranchStartDate",
                                                    octime AS "octTime", lmtime AS "lmtTime", userid AS "userId"
                                                    FROM unihot.entity_branch
                                                    WHERE entitybranchid in
                                                            (select entitybranchid from unihot.useraccess
                                                             where userid = %s
                                                             and entityid =%s
                                                             )
                                                          and entitybranchstatus = %s
                                                          and entityid = %s
                                                    ) as a
                                                """, (getuserentitybranches['keys']['userid'],
                                                      getuserentitybranches['keys']['entityid'],
                                                      getuserentitybranches['keys']['entitybranchstatus'],
                                                      getuserentitybranches['keys']['entityid'],))
    print(command)
    cur, s, f1 = db.mydbfunc(con, cur, command)
    return cur, s, f1


def insert_entity_branch(con, cur, insertentitybranch):
    command = cur.mogrify("""
                        INSERT INTO unihot.entity_branch    (
                         entityid,
                         entitybranchaddline1,
                         entitybranchaddline2,
                         entitybranchcategory,
                         entitybranchcity,
                         entitybranchcountry,
                         entitybranchdescription,
                         entitybranchemail,
                         entitybranchfax,
                         entitybranchimageurl,
                         entitybranchmobile,
                         entitybranchname,
                         entitybranchphone,
                         entitybranchpincode,
                         entitybranchshortname,
                         entitybranchstartdate,
                         entitybranchstate,
                         entitybranchstatus,
                         entitybranchwebsite,
                         lmtime,
                         octime,
                         userid
                        ) 


                        VALUES (%s,%s,%s,
                                %s,%s,%s,
                                %s,%s,%s,
                                %s,%s,%s,
                                %s,%s,%s,
                                %s,%s,%s,
                                %s,
                                CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,%s
                                ) RETURNING entitybranchid;
                        """,
                          (
                              insertentitybranch['values']['entityid'],
                              insertentitybranch['values']['entitybranchaddline1'],
                              insertentitybranch['values']['entitybranchaddline2'],
                              insertentitybranch['values']['entitybranchcategory'],
                              insertentitybranch['values']['entitybranchcity'],
                              insertentitybranch['values']['entitybranchcountry'],
                              insertentitybranch['values']['entitybranchdescription'],
                              insertentitybranch['values']['entitybranchemail'],
                              insertentitybranch['values']['entitybranchfax'],
                              insertentitybranch['values']['entitybranchimageurl'],
                              insertentitybranch['values']['entitybranchmobile'],
                              insertentitybranch['values']['entitybranchname'],
                              insertentitybranch['values']['entitybranchphone'],
                              insertentitybranch['values']['entitybranchpincode'],
                              insertentitybranch['values']['entitybranchshortname'],
                              insertentitybranch['values']['entitybranchstartdate'],
                              insertentitybranch['values']['entitybranchstate'],
                              insertentitybranch['values']['entitybranchstatus'],
                              insertentitybranch['values']['entitybranchwebsite'],
                              insertentitybranch['values']['userid']
                          ))

    print(command)
    cur, s, f1 = db.mydbfunc(con, cur, command)
    return cur, s, f1


def modify_entity_branch(con, cur, modifyentitybranch):
    command = cur.mogrify("""
                        UPDATE unihot.entity_branch    
                        SET 
                         entityid = %s,
                         entitybranchaddline1 = %s,
                         entitybranchaddline2 = %s,
                         entitybranchcategory = %s,
                         entitybranchcity = %s,
                         entitybranchcountry = %s,
                         entitybranchdescription = %s,
                         entitybranchemail = %s,
                         entitybranchfax = %s,
                         entitybranchimageurl = %s,
                         entitybranchmobile = %s,
                         entitybranchname = %s,
                         entitybranchphone = %s,
                         entitybranchpincode = %s,
                         entitybranchshortname = %s,
                         entitybranchstartdate = %s,
                         entitybranchstate = %s,
                         entitybranchstatus = %s,
                         entitybranchwebsite = %s,
                         lmtime = CURRENT_TIMESTAMP,
                         octime = %s,
                         userid = %s 
                        WHERE entitybranchid = %s
                         RETURNING entitybranchid;
                        """,
                          (
                              modifyentitybranch['values']['entityid'],
                              modifyentitybranch['values']['entitybranchaddline1'],
                              modifyentitybranch['values']['entitybranchaddline2'],
                              modifyentitybranch['values']['entitybranchcategory'],
                              modifyentitybranch['values']['entitybranchcity'],
                              modifyentitybranch['values']['entitybranchcountry'],
                              modifyentitybranch['values']['entitybranchdescription'],
                              modifyentitybranch['values']['entitybranchemail'],
                              modifyentitybranch['values']['entitybranchfax'],
                              modifyentitybranch['values']['entitybranchimageurl'],
                              modifyentitybranch['values']['entitybranchmobile'],
                              modifyentitybranch['values']['entitybranchname'],
                              modifyentitybranch['values']['entitybranchphone'],
                              modifyentitybranch['values']['entitybranchpincode'],
                              modifyentitybranch['values']['entitybranchshortname'],
                              modifyentitybranch['values']['entitybranchstartdate'],
                              modifyentitybranch['values']['entitybranchstate'],
                              modifyentitybranch['values']['entitybranchstatus'],
                              modifyentitybranch['values']['entitybranchwebsite'],
                              modifyentitybranch['values']['octime'],
                              modifyentitybranch['values']['userid'],
                              modifyentitybranch['values']['entitybranchid']
                          ))

    print(command)
    cur, s, f1 = db.mydbfunc(con, cur, command)
    return cur, s, f1


def delete_entity_branch(con, cur, entityid, entitybranchid):
    print(entityid)
    print(entitybranchid)
    command = cur.mogrify("""
                                        UPDATE unihot.entity_branch    
                                        SET 
                                         entitybranchstatus = %s,
                                         lmtime = CURRENT_TIMESTAMP,
                                         userid = %s
                                         WHERE entityid = %s AND entitybranchid = %s
                                         RETURNING entityid;
                                        """,
                          ('D',
                           userid,
                           entityid, entitybranchid
                           ))
    print(command)
    cur, s, f1 = db.mydbfunc(con, cur, command)
    return cur, s, f1


def get_bullion_price(con, cur):
    command = cur.mogrify("""
                                                    SELECT json_agg(a) FROM (
                                                    SELECT * from nawg.ibjia
                                                    ) as a
                                                """)
    print(command)
    cur, s, f1 = db.mydbfunc(con, cur, command)
    return cur, s, f1
