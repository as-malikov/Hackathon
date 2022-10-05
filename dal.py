from object.connector import init_db, destruct_db
from object.Object import Object
import datetime


async def dal_verify_user(user):
    db = await init_db()
    cur = db.cursor()
    cur.execute("SELECT id,login_s21,name,campus_id,role_id \
                FROM users WHERE telegram_id ='%s'" % user.telegram_id)
    list = cur.fetchall()
    if len(list) == 0:
        user.telegram_id = 0
    else:
        user.id = list[0][0]
        user.login_s21 = list[0][1]
        user.name = list[0][2]
        user.campus_id = list[0][3]
        user.role_id = list[0][4]
    await destruct_db(db)
    return user


async def dal_get_object(user):
    db = await init_db()
    cur = db.cursor()
    cur.execute("SELECT \
                o.id, o.type_id, o.name, o.desc, o.img, o.floor, o.number \
                FROM types t, users u, link_type_to_role ltr, objects o, \
                link_object_to_campus loc \
                WHERE loc.object_id = o.id and loc.campus_id = u.campus_id \
                and o.type_id = t.id and ltr.type_id = t.id \
                and (ltr.role_id = u.role_id or ltr.role_id = 1) \
                and u.telegram_id = '%s'" % user._telegram_id)
    list = cur.fetchall()
    object_list = []
    if len(list) != 0:
        for i in range(len(list)):
            obj = Object(list[i][0],
                         list[i][1],
                         list[i][2],
                         list[i][3],
                         list[i][4],
                         list[i][5],
                         list[i][6])
            object_list.append(obj)
    await destruct_db(db)
    return object_list


async def dal_get_object_by_id(obj_id):
    db = await init_db()
    cur = db.cursor()
    sql = ("SELECT * FROM objects WHERE id = %s")
    data = (obj_id)
    cur.execute(sql, data)
    got_data = cur.fetchall()
    obj = Object(got_data[0][0],
                 got_data[0][1],
                 got_data[0][2],
                 got_data[0][3],
                 got_data[0][4],
                 got_data[0][5],
                 got_data[0][6])
    await destruct_db(db)
    return obj


async def dal_get_schedule(obj, choose_day):
    db = await init_db()
    cur = db.cursor()
    next_day = choose_day + datetime.timedelta(days=1)
    sql = ("SELECT HOUR(s.start_date) FROM schedule s \
            WHERE status_id = 1 and date(s.start_date) >= %s \
            and date(s.start_date) < %s and object_id = %s")
    data = (choose_day, next_day, obj.id)
    cur.execute(sql, data)
    schedule_list = cur.fetchall()
    await destruct_db(db)
    return schedule_list


async def dal_add_schedule(new_shedule):
    db = await init_db()
    cur = db.cursor()
    sql = ("INSERT INTO schedule "
           "(`object_id`,`user_id`,`start_date`,`end_date`,`status_id`)"
           " VALUES (%s,%s,%s,%s,%s)")
    data = (new_shedule.object_id,
            new_shedule.user_id,
            new_shedule.start_date,
            new_shedule.end_date,
            new_shedule.status_id)
    cur.execute(sql, data)
    cur.execute("COMMIT")
    await destruct_db(db)
