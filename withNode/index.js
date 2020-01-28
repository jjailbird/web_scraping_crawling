const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');
const url = require('url');
const queryString = require('querystring');
const download = require('download');

// 01. set parameter, agent, proxy, limit options >>>>>>>>>>>>>>>>>>>>>>>>>>>>
const parsedTbs = ''
const SEARCH_TXT = '설향';
const TARGET_URL = `https://www.google.com/search?q=${SEARCH_TXT}&source=lnms&tbm=isch&sa=X&tbs=${parsedTbs}`;
const SEARCH_IPT_SLT = '#sbtc > div > div.a4bIc > input';
const SEARCH_BTN_SLT = '#sbtc > button'
const SEARCH_RLT_ITEM_SLT = 'a.rg_l:not([href$="#"])';
const SEARCH_RLT_IMG_SLT = '//img[@class="rg_ic rg_i"]';
const SAVE_DIR = `../downloads/${SEARCH_TXT}`; 
// <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

function save_from_base64(data, file_name) {
  fs.writeFileSync(file_name, data.split(';base64,').pop(), {encoding: 'base64'}, function(err) {
    console.log(err);
  })
}

(async () => {

  !fs.existsSync(SAVE_DIR) && fs.mkdirSync(SAVE_DIR); 

  const browser = await puppeteer.launch({headless: true, devtools: false});
  const page = await browser.newPage();
  // await page.setBypassCSP(true);
  await page.setViewport({ width: 2560, height: 1440 });
  await page.goto(TARGET_URL, {waitUntil: 'networkidle2'});
  // await page.type(SEARCH_IPT_SLT, SEARCH_TXT);
  // await page.keyboard.press("Enter");
  // await page.waitForNavigation();
  // await page.waitFor(5000);
  await page.waitForSelector('#bfoot');
  
  const items = await page.$$(SEARCH_RLT_ITEM_SLT);
  
  for (let i = 0;i < items.length;i++) {
    
    const href_src = await (await items[i].getProperty('href')).jsonValue();
    const href_obj = url.parse(href_src);
    const href_q = queryString.parse(href_obj.query);
    // const file_name = `${SAVE_DIR}/${i.toString().padStart(3,'0')}.`;
    // if (href_q.imagurl)
    // console.log(href_q);
    if (href_q.imgurl) {
      try {
        await download(href_q.imgurl, SAVE_DIR);
      }
      catch (e) {
        console.log(href_q.imgurl);
        console.log(e.message);
      }
      // let file_name = path.basename(href_q.imgurl);
      // console.log(file_name);
      // console.log(`${i.toString().padStart(3,'0')}.${file_name.split('?').shift()}`);
    }
    if (href_q.imgrefurl) {
      // console.log(href_q.imgrefurl);
    }

    // console.log(href_src); 
    /*
    const image = await items[i].$('img');
    const src = await (await image.getProperty('src')).jsonValue();
    
    const file_name = `${SEARCH_TXT}.${i.toString().padStart(3,'0')}.jpg`
    if (src) {
      save_from_base64(src, file_name);
      console.log(file_name)
    }
    */
  }
  
  console.log(items.length)

})();