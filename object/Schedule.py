class Schedule:
    def __init__(self, object_id, user_id, start_date, end_date, status_id):
        self._object_id = object_id
        self._user_id = user_id
        self._start_date = start_date
        self._end_date = end_date
        self._status_id = status_id

    # make the getter method OBJECT_ID
    def get_object_id(self):
        return self._object_id

    # make the setter method OBJECT_ID
    def set_object_id(self, a):
        self._object_id = a

    # make the delete method OBJECT_ID
    def del_object_id(self):
        del self._object_id

    object_id = property(get_object_id, set_object_id, del_object_id)

    # make the getter method USER_ID
    def get_user_id(self):
        return self._user_id

    # make the setter method USER_ID
    def set_user_id(self, a):
        self._user_id = a

    # make the delete method USER_ID
    def del_user_id(self):
        del self._user_id

    user_id = property(get_user_id, set_user_id, del_user_id)

    # make the getter method START_DATE
    def get_start_date(self):
        return self._start_date

    # make the setter method START_DATE
    def set_start_date(self, a):
        self._start_date = a

    # make the delete method START_DATE
    def del_start_date(self):
        del self._start_date

    start_date = property(get_start_date, set_start_date, del_start_date)

    # make the getter method END_DATE
    def get_end_date(self):
        return self._end_date

    # make the setter method END_DATE
    def set_end_date(self, a):
        self._end_date = a

    # make the delete method END_DATE
    def del_end_date(self):
        del self._end_date

    end_date = property(get_end_date, set_end_date, del_end_date)

    # make the getter method STATUS_ID
    def get_status_id(self):
        return self._status_id

    # make the setter method STATUS_ID
    def set_status_id(self, a):
        self._status_id = a

    # make the delete method STATUS_ID
    def del_status_id(self):
        del self._status_id

    status_id = property(get_status_id, set_status_id, del_status_id)
