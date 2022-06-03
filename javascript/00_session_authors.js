const https = require('https')
const jsdom = require("jsdom")
const { JSDOM } = jsdom

const options = {
  hostname: '2022.drupalcamp.es',
  port: 443,
  path: '/programa',
  method: 'GET'
}

const req = https.request(options, res => {
  console.log(`statusCode: ${res.statusCode}`)

  res.on('data', html => {
    const dom = new JSDOM(html).window.document

    const author_elements = dom.querySelectorAll(".author")
    const authors = Array.from(author_elements).map(author => author.textContent) 

    console.log(authors)
  })
})

req.on('error', error => {
    console.error(error)
})

req.end()
