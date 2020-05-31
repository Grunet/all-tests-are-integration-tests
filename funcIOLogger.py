from os import path
import json


def logIO(func):
    def funcWithLogging(*args, **kwargs):

        output = func(*args, **kwargs)

        # Get any previous log data
        loggingPath = path.join(path.dirname(__file__), "interceptedFuncIO.json")

        try:
            with open(loggingPath, "r") as f:
                logData = json.load(f)
        except FileNotFoundError:
            logData = {}  # For the first time this is hit

        if "logs" not in logData:
            logData["logs"] = []

        # Create the log for this test
        newLog = {}

        newLog["args"] = []
        for arg in args:
            argThatCanBeSavedToFile = str(arg)

            newLog["args"].append(argThatCanBeSavedToFile)

        newLog["kwargs"] = kwargs

        newLog["return"] = output

        # Add in the log and save it off
        logData["logs"].append(newLog)

        with open(loggingPath, "w") as f:
            json.dump(logData, f, indent=4)

        return output

    return funcWithLogging
