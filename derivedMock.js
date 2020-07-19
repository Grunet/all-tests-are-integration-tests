const fs = require("fs");

function mock_indexOf() {
  const interceptedIOJson = fs.readFileSync("./interceptedIO.json", "utf-8"); //Ofc not ideal, but ok for the experiment
  const interceptedIOObj = JSON.parse(interceptedIOJson);
  const { testIO } = interceptedIOObj;

  const matchingTestCase = testIO.find(
    (testCase) =>
      deepCompare(this, testCase["thisValue"]) &&
      deepCompare([...arguments], testCase["args"])
  );
  if (matchingTestCase) {
    console.log("Mock successfully used");

    return matchingTestCase["returnValue"];
  } else {
    throw new Error("No matching test case found");
  }
}

function deepCompare(obj1, obj2) {
  //This isn't actually correct, but works for the purposes of this expeiment
  return JSON.stringify(obj1) === JSON.stringify(obj2);
}

module.exports = {
  mock_indexOf: mock_indexOf,
};
