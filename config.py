"""Application configuration.

Secrets and database settings will be configured in the backend step.
"""


class Config:
    SECRET_KEY = "change-this-before-deployment"
    SQLALCHEMY_DATABASE_URI = "sqlite:///greenleaf.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
