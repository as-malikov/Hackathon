from dal import (
    dal_verify_user,
    dal_get_object,
    dal_get_object_by_id,
    dal_get_schedule,
    dal_add_schedule
    )


async def verify_user(user):
    await dal_verify_user(user)


async def get_object(user):
    return await dal_get_object(user)


async def get_object_by_id(obj_id):
    return await dal_get_object_by_id(obj_id)


async def add_schedule(new_shedule):
    return await dal_add_schedule(new_shedule)


async def get_schedule(obj, choose_day):
    return await dal_get_schedule(obj, choose_day)
