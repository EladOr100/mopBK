#!/usr/bin/env python3
import connexion
import logging
import pytest


def post_testByFile(TestFile):
    pytest.main([TestFile["fileName"]])

def post_testByMarks(Marker):
    pytest.main([Marker["fileName"],'-v','-m',Marker["marker"]])

def post_testByName(TestName):
    pytest.main([TestName["fileName"],'-k',TestName["testName"]])


logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__)
app.add_api('swagger.yaml')
application = app.app

if __name__ == '__main__':
    # run our standalone gevent server
    app.run(port=8080, server='gevent')
