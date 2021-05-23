const cypress = require('cypress')

cypress
  .run({
    // the path is relative to the current working directory
    spec: './cypress/integration/iptv.spec.js',
    headless: true,
    config: {
        video: false,
      },
  })
  .then((results) => {
    console.log(results.runs[0].tests)
  })
  .catch((err) => {
    console.error(err)
  })