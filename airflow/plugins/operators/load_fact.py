from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadFactOperator(BaseOperator):

    ui_color = '#F98866'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id = "",
                 table = "",
                 load_sql_stmt = "",
                 *args, **kwargs):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.load_sql_stmt = load_sql_stmt
    
    insert_sql_stmt = """
        INSERT INTO {}
        {};
        COMMIT;
    """
    
    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        self.log.info("Loading the fact table into Redshift")
        formatted_sql = LoadFactOperator.insert_sql_stmt.format(
            self.table,
            self.load_sql_stmt
        )
        redshift.run(formatted_sql)
