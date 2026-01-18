const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  await page.goto('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html');

  // Ждем, пока все картинки загрузятся (например, что src не равен пустому)
  await page.waitForFunction(() => {
    const imgs = document.querySelectorAll('img');
    return Array.from(imgs).every(img => img.complete && img.naturalWidth !== 0);
  });

  // Получить src 3-й картинки (индекс 2)
  const srcValue = await page.$eval('img:nth-of-type(3)', img => img.getAttribute('src'));

  console.log(srcValue);

  await browser.close();
})();