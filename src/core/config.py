# -*- coding: utf-8 -*-
import ConfigParser

class Config:
    config = None

    @staticmethod
    def init(config_path):
        fp = open(config_path)
        config = ConfigParser.ConfigParser()
        config.readfp(fp)
        Config.config = config

    @staticmethod
    def get(scope, name):
        config = Config.config
        return config.get(scope, name)

    @staticmethod
    def set(scope, name, value=None):
        Config.config.set(scope, name, value)