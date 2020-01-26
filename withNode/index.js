const puppeteer = require('puppeteer');
const fs = require('fs');

// 01. set parameter, agent, proxy, limit options >>>>>>>>>>>>>>>>>>>>>>>>>>>>
const TARGET_URL = 'https://www.google.co.kr/imghp';
const SEARCH_TXT = '고구마';
const SEARCH_IPT_SLT = '#sbtc > div > div.a4bIc > input';
const SEARCH_BTN_SLT = '#sbtc > button'
const SEARCH_RLT_ITEM_SLT = 'a.rg_l:not([href$="#"])';
const SEARCH_RLT_IMG_SLT = '//img[@class="rg_ic rg_i"]';
// <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

function save_from_base64(data, file_name) {
  fs.writeFile(file_name, data.split(';base64,').pop(), {encoding: 'base64'}, function(err) {
    console.log(err);
  })
}

(async () => {
  const browser = await puppeteer.launch({headless: false, devtools: true});
  const page = await browser.newPage();

  await page.setViewport({ width: 2560, height: 1440 });
  await page.goto(TARGET_URL, {waitUntil: 'networkidle2'});
  await page.type(SEARCH_IPT_SLT, SEARCH_TXT);
  await page.keyboard.press("Enter");

  await page.waitForNavigation();
  
  const items = await page.$$(SEARCH_RLT_ITEM_SLT);
  
  for (let i = 0;i < items.length;i++) {
    
    const image = await items[i].$('img');

    const src = await (await image.getProperty('src')).jsonValue();
    const file_name = `${SEARCH_TXT}.${i.toString().padStart(3,'0')}.jpg`

    if (src) {
      save_from_base64(src, file_name);
      console.log(file_name)
    }
  }
  
  console.log(items.length)

})();