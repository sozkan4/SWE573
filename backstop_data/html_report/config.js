report({
  "testSuite": "BackstopJS",
  "tests": [
    {
      "pair": {
        "reference": "../bitmaps_reference/backstop_default_Homepage_0_body_0_phone.png",
        "test": "../bitmaps_test/20230511-201504/backstop_default_Homepage_0_body_0_phone.png",
        "selector": "body",
        "fileName": "backstop_default_Homepage_0_body_0_phone.png",
        "label": "Homepage",
        "requireSameDimensions": true,
        "misMatchThreshold": 0.1,
        "url": "http://172.18.0.3:8000",
        "referenceUrl": "",
        "expect": 0,
        "viewportLabel": "phone",
        "engineErrorMsg": "Navigation timeout of 60000 ms exceeded",
        "error": "Reference file not found /Users/semihozkan/Desktop/SWE573/backstop_data/bitmaps_reference/backstop_default_Homepage_0_body_0_phone.png"
      },
      "status": "fail"
    },
    {
      "pair": {
        "reference": "../bitmaps_reference/backstop_default_Homepage_0_body_1_tablet.png",
        "test": "../bitmaps_test/20230511-201504/backstop_default_Homepage_0_body_1_tablet.png",
        "selector": "body",
        "fileName": "backstop_default_Homepage_0_body_1_tablet.png",
        "label": "Homepage",
        "requireSameDimensions": true,
        "misMatchThreshold": 0.1,
        "url": "http://172.18.0.3:8000",
        "referenceUrl": "",
        "expect": 0,
        "viewportLabel": "tablet",
        "engineErrorMsg": "Navigation timeout of 60000 ms exceeded",
        "error": "Reference file not found /Users/semihozkan/Desktop/SWE573/backstop_data/bitmaps_reference/backstop_default_Homepage_0_body_1_tablet.png"
      },
      "status": "fail"
    }
  ],
  "id": "backstop_default"
});