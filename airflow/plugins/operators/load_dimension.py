from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id = "",
                 table = "",
                 load_sql_stmt = "",
                 append_only = False,
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.load_sql_stmt = load_sql_stmt
        self.append_only = append_only

    insert_sql_stmt = """
        INSERT INTO {}
        {};
        COMMIT;
    """
    truncate_sql_stmt = """
        TRUNCATE TABLE {};
    """

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        if not self.append_only:
            self.log.info(f"Truncate {self.table} dimension table")
            formatted_trunc_sql = LoadDimensionOperator.truncate_sql_stmt.format(
            self.table
            )
            redshift.run(formatted_trunc_sql)
        self.log.info(f"Loading the dimension table {self.table} into Redshift")
        formatted_sql = LoadDimensionOperator.insert_sql_stmt.format(
            self.table,
            self.load_sql_stmt
        )
        redshift.run(formatted_sql)
