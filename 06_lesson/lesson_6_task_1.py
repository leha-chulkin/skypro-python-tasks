const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  // Перейти на страницу
  await page.goto('http://uitestingplayground.com/ajax');

  // Нажать на синюю кнопку (на странице её может быть несколько, выберем по тексту)
  await page.click('button');

  // Ждать появления зеленой плашки (например, с классом 'label-success' или похожий)
  await page.waitForSelector('.bg-success'); // Например, по целевому классу

  // Получить текст из зеленой плашки
  const message = await page.$eval('.bg-success', el => el.innerText);

  console.log('Data loaded with AJAX get request.');

  await browser.close();
})();