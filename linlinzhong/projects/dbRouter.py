class MySqlDbRouter(object):
    # Route projects app DB requests to MySql DB
    # Specify 'projects.dbRouter.MySqlDbRouter' 
    # in DATABASE_ROUTERS in settings.py
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'projects':
            return 'mysql_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'projects':
            return 'mysql_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'projects' or \
                obj2._meta.app_label == 'projects':
            return True
        return None

    def allow_migrate(self, db, model):
        app_list = ('projects',)
        if db == 'mysql_db':
            return model._meta.app_label in app_list
        elif model._meta.app_label in app_list:
            return False
        return None
