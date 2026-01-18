const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  await page.goto('http://uitestingplayground.com/textinput');

  // Ввести текст "SkyPro" в поле
  await page.type('#newButtonName', 'SkyPro');

  // Нажать на синюю кнопку (найдём по тексту или классу)
  await page.click('.btn-primary');

  // Ждём, пока текст кнопки изменится
  await page.waitForFunction(
    () => document.querySelector('.btn-primary').innerText.includes('SkyPro')
  );

  // Получить текст кнопки
  const buttonText = await page.$eval('.btn-primary', el => el.innerText);

  console.log(`"${buttonText}"`);

  await browser.close();
})();