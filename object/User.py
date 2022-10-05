class User:
    def __init__(self, user_id, login_s21, name, telegram_id, campus_id, role_id):
        self._id = user_id
        self._login_s21 = login_s21
        self._name = name
        self._telegram_id = telegram_id
        self._campus_id = campus_id
        self._role_id = role_id

    # make the getter method ID
    def get_id(self):
        return self._id

    # make the setter method ID
    def set_id(self, a):
        self._id = a

    # make the delete method ID
    def del_id(self):
        del self._id

    id = property(get_id, set_id, del_id)

    # make the getter method LOGIN_S21
    def get_login_s21(self):
        return self._login_s21

    # make the setter method LOGIN_S21
    def set_login_s21(self, a):
        self._login_s21 = a

    # make the delete method LOGIN_S21
    def del_login_s21(self):
        del self._login_s21

    login_s21 = property(get_login_s21, set_login_s21, del_login_s21)

    # make the getter method NAME
    def get_name(self):
        return self._name

    # make the setter method NAME
    def set_name(self, a):
        self._name = a

    # make the delete method NAME
    def del_name(self):
        del self._name

    name = property(get_name, set_name, del_name)

    # make the getter method TELEGRAM_ID
    def get_telegram_id(self):
        return self._telegram_id

    # make the setter method TELEGRAM_ID
    def set_telegram_id(self, a):
        self._telegram_id = a

    # make the delete method TELEGRAM_ID
    def del_telegram_id(self):
        del self._telegram_id

    telegram_id = property(get_telegram_id, set_telegram_id, del_telegram_id)

    # make the getter method CAMPUS_ID
    def get_campus_id(self):
        return self._campus_id

    # make the setter method CAMPUS_ID
    def set_campus_id(self, a):
        self._campus_id = a

    # make the delete method CAMPUS_ID
    def del_campus_id(self):
        del self._campus_id

    campus_id = property(get_campus_id, set_campus_id, del_campus_id)

    # make the getter method ROLE_ID
    def get_role_id(self):
        return self._role_id

    # make the setter method ROLE_ID
    def set_role_id(self, a):
        self._role_id = a

    # make the delete method ROLE_ID
    def del_role_id(self):
        del self._role_id
    role_id = property(get_role_id, set_role_id, del_role_id)
