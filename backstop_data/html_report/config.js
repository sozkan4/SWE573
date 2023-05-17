report({
  "testSuite": "BackstopJS",
  "tests": [
    {
      "pair": {
        "reference": "../bitmaps_reference/backstop_default_Homepage_0_body_0_desktop.png",
        "test": "../bitmaps_test/20230517-150900/backstop_default_Homepage_0_body_0_desktop.png",
        "selector": "body",
        "fileName": "backstop_default_Homepage_0_body_0_desktop.png",
        "label": "Homepage",
        "requireSameDimensions": true,
        "misMatchThreshold": 0.1,
        "url": "http://127.0.0.1",
        "expect": 0,
        "viewportLabel": "desktop",
        "diff": {
          "isSameDimensions": true,
          "dimensionDifference": {
            "width": 0,
            "height": 0
          },
          "rawMisMatchPercentage": 6.668402777777778,
          "misMatchPercentage": "6.67",
          "analysisTime": 45
        },
        "diffImage": "../bitmaps_test/20230517-150900/failed_diff_backstop_default_Homepage_0_body_0_desktop.png"
      },
      "status": "fail"
    }
  ],
  "id": "backstop_default"
});