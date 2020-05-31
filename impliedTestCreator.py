from pathlib import Path
import shutil
import json

pathToOrigUnitTests = Path(__file__).parent / "originalUnitTests.py"
pathToNewTests = Path(__file__).parent / "impliedTests.py"

shutil.copy(pathToOrigUnitTests, pathToNewTests)

NEW_FUNC_NAME = "rstrip_C"

# Making sure impots/function calls get updated
origUnitTestText = pathToOrigUnitTests.read_text()
newFunctionTestText = origUnitTestText.replace("strip_C", NEW_FUNC_NAME)

pathToNewTests.write_text(newFunctionTestText)

# Creating the text for the implied tests from the logs
pathToLogs = Path(__file__).parent / "interceptedFuncIO.json"

with open(pathToLogs, "r") as f:
    logData = json.load(f)

impliedTests = []
for log in logData["logs"]:

    # Assuming only str arguments/output from here on

    # Wrapping all the strings in quotes so that they work as valid quotes
    for index, arg in enumerate(log["args"]):
        log["args"][index] = "'" + arg + "'"

    log["return"] = "'" + log["return"] + "'"

    # Ignoring since the example code doesn't use it
    # kwargs =

    testCode = (
        "self.assertEqual("
        + NEW_FUNC_NAME
        + "("
        + ",".join(log["args"])
        + "),"
        + log["return"]
        + ")"
    )

    impliedTests.append(testCode)

# Replacing the original tests with the implied tests in the new test file
fileContents = None

linesToReplace = []
with open(pathToNewTests, "r") as f:
    fileContents = f.readlines()

    for index, lineText in enumerate(fileContents):
        if "assert" in lineText:
            linesToReplace.append(index)

for index in linesToReplace:
    lineText = fileContents[index]

    startOfExpression = len(lineText) - len(lineText.lstrip())
    newExpression = impliedTests.pop(0)

    fileContents[index] = (
        lineText[:startOfExpression] + newExpression
    )  # Preserving indentation

with open(pathToNewTests, "w") as f:
    f.writelines(fileContents)
