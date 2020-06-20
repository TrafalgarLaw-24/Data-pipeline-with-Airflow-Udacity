from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id = "",
                 tables = [],
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.check_stmts = check_stmts
        self.redshift_conn_id = redshift_conn_id

    def execute(self, context):
        redshift_hook = PostgresHook(self.redshift_conn_id)

        for stmt in self.check_stmts:
            result = int(redshift_hook.get_first(sql=stmt['sql'])[0])

            # check if it is equal
            if stmt['op'] == 'eq':
                if result != stmt['val']:
                    raise AssertionError(f"Check failed: {result} {stmt['op']} {stmt['val']}")
            # check if it is not equal
            elif stmt['op'] == 'ne':
                if result == stmt['val']:
                    raise AssertionError(f"Check failed: {result} {stmt['op']} {stmt['val']}")
            # check if it is greater than
            elif stmt['op'] == 'gt':
                if result <= stmt['val']:
                    raise AssertionError(f"Check failed: {result} {stmt['op']} {stmt['val']}")

            self.log.info(f"Check passed: {result} {stmt['op']} {stmt['val']}")
