"""
"""


PSQL_APPS = []


class DatabaseRouter:
    """
    """

    def db_for_read(self, model, **hints):
        """
        """
        if model._meta.app_label in PSQL_APPS:
            return 'postgres'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        """
        if model._meta.app_label in PSQL_APPS:
            return 'postgres'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        """
        if (obj1._meta.app_label in PSQL_APPS) == \
           (obj2._meta.app_label in PSQL_APPS):
           return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        """
        if app_label in PSQL_APPS:
            return db == 'postgres'
        return db == 'default'
