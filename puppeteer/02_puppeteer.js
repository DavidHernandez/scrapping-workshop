const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    headless: true,
    executablePath: '/usr/bin/google-chrome',
    args: [
      "--disable-gpu",
      "--disable-dev-shm-usage",
      "--disable-setuid-sandbox",
      "--no-sandbox",
    ]
  })
  const page = await browser.newPage() 
  await page.goto('https://quehacenlosdiputados.es/diputados', {
    waitUntil: 'networkidle0',
  })

  const deputies = await page.evaluate(() => {
    const deputy_elements = document.querySelectorAll('.c-deputy-card h4')
    console.log(deputy_elements)
    return Array.from(deputy_elements, deputy_element => deputy_element.textContent)
  })

  console.log(deputies)

  await browser.close()
})()
