class DBRouter():

    def db_for_read(self, model, **hints):
        if model._meta.db_table == 'MTCars':
            return 'DBMTCars'
        return None

    def db_for_write(self, model, **hints):
        """
        Permitir direcionar operações de escrita para o banco de dados correto.
        """
        if model._meta.db_table == 'MTCars':
            return 'DBMTCars'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.db_table == 'MTCars' or obj2._meta.db_table == 'MTCars':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'exemplo':
            return db == 'MTCars'
        return None