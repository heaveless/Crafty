# Generated by database migrator
import peewee

def migrate(migrator, database, **kwargs):
    migrator.add_columns('users', email=peewee.CharField(default="default@example.com"))
    """
    Write your migrations here.
    """



def rollback(migrator, database, **kwargs):
    migrator.drop_columns('users', ['email']) 
    """
    Write your rollback migrations here.
    """