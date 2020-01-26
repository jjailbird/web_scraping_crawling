const puppeteer = require('puppeteer')

// 01. set parameter, agent, proxy, limit options >>>>>>>>>>>>>>>>>>>>>>>>>>>>
const TARGET_URL = 'https://www.google.co.kr/imghp?hl=ko'
const SEARCH_TXT = '고구마'
const SEARCH_IPT_SLT = '#sbtc > div > div.a4bIc > input'
//const SEARCH_BTN_SLT = '//*[@id="sbtc"]/button'
const SEARCH_RLT_ITEM_SLT = '//a[@class="rg_l"]'
const SEARCH_RLT_IMG_SLT = '//img[@class="rg_ic rg_i"]'
// <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


(async () => {
  const browser = await puppeteer.launch({headless: false, devtools: true})
  const page = await browser.newPage()

  await page.goto(TARGET_URL, {waitUntil: 'networkidle2'})
  await page.type(SEARCH_IPT_SLT, SEARCH_TXT)  


})();