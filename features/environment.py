import time
from selenium import webdriver

from helper.helper import Helper


def before_all(context):
    context.helper = Helper()

def after_all(context):
    context.helper = Helper()
    context.helper.close()
