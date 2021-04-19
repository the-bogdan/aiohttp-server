import os
from alembic import command, config as alembic_config


class AlembicAgent:
    def __init__(self, alembic_conf: alembic_config.Config, versions_path: str):
        self.alembic_conf: alembic_config.Config = alembic_conf
        self.versions_path: str = versions_path

    @classmethod
    def setup(cls, manage_file_path: str) -> 'AlembicAgent':
        alembic_ini_path = os.path.join(manage_file_path, 'database/alembic/alembic.ini')
        versions_path = os.path.join(manage_file_path, 'database/alembic/versions/')
        alembic_conf = alembic_config.Config(alembic_ini_path)
        return cls(alembic_conf, versions_path)

    def make_migrations(self, message: str = None) -> None:
        command.revision(
            message=message,
            autogenerate=True,
            config=self.alembic_conf,
            version_path=self.versions_path
        )

    def upgrade(self) -> None:
        command.upgrade(
            revision='head',
            config=self.alembic_conf
        )

    def downgrade(self) -> None:
        command.downgrade(
            revision='-1',
            config=self.alembic_conf
        )
