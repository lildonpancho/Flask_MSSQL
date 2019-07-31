import pyodbc from flask

import current_app, _app_ctx_stack

class MSSQL(object):
    def _init__(self, app=None, **connect_args)
        self.connect_args=connect_args
        self.app = app
        if app is not None:
            self.init_app(app)


    def init_app(self, app):
        app.config.setdefault('MSSQL_DATABASE_DRIVER', '{ODBC Driver 17 for SQL Server}')
        app.config.setdefault('MSSQL_DATABASE_SERVER', None)
        app.config.setdefault('MSSQL_DATABASE_PORT', 49200)
        app.config.setdefault('MSSQL_DATABASE_DB', None)
        app.config.setdefault('MSSQL_DATABASE_USER', None)
        app.config.setdefault('MSSQL_DATABASE_PASSWORD', None)
        
        app.teardown_appcontext(self.teardown)

    def connect(self):
        if self.app.config['MSSQL_DATABASE_DRIVER']:
            self.connect_args['DRIVER'] = self.app.config['MSSQL_DATABASE_DRIVER']
        if self.app.config['MSSQL_DATABASE_SERVER']:
            self.connect_args[';SERVER'] = self.app.config['MSSQL_DATABASE_SERVER']
        if self.app.config['MSSQL_DATABASE_PORT']:
            self.connect_args[';PORT'] = self.app.config['MSSQL_DATABASE_PORT']
        if self.app.config['MSSQL_DATABASE_DB']:
            self.connect_args[';DATABASE'] = self.app.config['MSSQL_DATABASE_DB']
        if self.app.config['MSSQL_DATABASE_USER']:
            self.connect_args[';UID'] = self.app.config['MSSQL_DATABASE_USER']
        if self.app.config['MSSQL_DATABASE_PASSWORD']:
            self.connect_args[';PWD'] = self.app.config['MSSQL_DATABASE_PASSWORD']
        return pyodbc.connect(**self.connect_args)

    def teardown_request(self, exception):
        ctx = _app_ctx_stack.teardown_appcontext
        if hasattr(ctx, 'mssql_db'):
            ctx.mssql_db.close()

    def get_db(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not has attr(ctx, 'mssql_db'):
                ctx.mssql_db = self.connect()
            return ctx.mssql_db